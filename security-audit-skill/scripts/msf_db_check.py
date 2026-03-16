#!/usr/bin/env python3
"""
Security Audit - Metasploit Database Vulnerability Checker
Cross-references detected framework versions against known vulnerabilities
using Metasploit's module database and CVE databases.

Requires: msfconsole available in PATH for active exploitation checks.
Uses: curl for CVE API lookups (no msfconsole needed for initial check).
"""

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path


# CVE API endpoints for vulnerability lookups
CVE_API_BASE = "https://services.nvd.nist.gov/rest/json/cves/2.0"
OSV_API_BASE = "https://api.osv.dev/v1"


def query_osv(ecosystem: str, package: str, version: str) -> list[dict]:
    """
    Query OSV.dev API for known vulnerabilities.
    OSV is free, no API key needed, and covers npm, PyPI, Go, etc.
    """
    ecosystem_map = {
        "npm": "npm",
        "pypi": "PyPI",
        "go": "Go",
        "rubygems": "RubyGems",
        "composer": "Packagist",
    }

    osv_ecosystem = ecosystem_map.get(ecosystem)
    if not osv_ecosystem:
        return []

    payload = json.dumps({
        "version": version,
        "package": {
            "name": package,
            "ecosystem": osv_ecosystem,
        }
    })

    try:
        result = subprocess.run(
            ["curl", "-s", "-X", "POST",
             f"{OSV_API_BASE}/query",
             "-H", "Content-Type: application/json",
             "-d", payload],
            capture_output=True, text=True, timeout=15
        )
        if result.returncode != 0:
            return []

        data = json.loads(result.stdout)
        vulns = []
        for vuln in data.get("vulns", []):
            severity = "Unknown"
            cvss_score = 0.0

            # Extract CVSS from severity array
            for sev in vuln.get("severity", []):
                if sev.get("type") == "CVSS_V3":
                    score_match = re.search(r"CVSS:3\.[01]/.*", sev.get("score", ""))
                    if score_match:
                        severity = sev["score"]

            # Extract from database_specific if available
            for ref in vuln.get("references", []):
                if "nvd.nist.gov" in ref.get("url", ""):
                    break

            vulns.append({
                "id": vuln.get("id", ""),
                "summary": vuln.get("summary", vuln.get("details", "")[:200]),
                "severity_vector": severity,
                "aliases": vuln.get("aliases", []),
                "published": vuln.get("published", ""),
                "modified": vuln.get("modified", ""),
                "references": [r.get("url") for r in vuln.get("references", [])[:5]],
                "has_msf_module": False,  # Will be checked separately
            })
        return vulns

    except (subprocess.TimeoutExpired, json.JSONDecodeError, OSError):
        return []


def check_msf_modules(cve_id: str) -> dict | None:
    """
    Check if Metasploit has a module for a given CVE.
    Requires msfconsole in PATH.
    """
    try:
        result = subprocess.run(
            ["msfconsole", "-q", "-x", f"search cve:{cve_id}; exit"],
            capture_output=True, text=True, timeout=60
        )
        output = result.stdout

        modules = []
        for line in output.splitlines():
            # Parse msfconsole search output
            match = re.match(r"\s*\d+\s+(exploit/\S+|auxiliary/\S+)", line)
            if match:
                modules.append({
                    "module_path": match.group(1),
                    "full_line": line.strip(),
                })

        if modules:
            return {
                "cve_id": cve_id,
                "modules": modules,
                "exploitable": any("exploit/" in m["module_path"] for m in modules),
            }
    except (subprocess.TimeoutExpired, FileNotFoundError, OSError):
        pass

    return None


def check_msf_available() -> bool:
    """Check if msfconsole is available."""
    try:
        result = subprocess.run(
            ["msfconsole", "--version"],
            capture_output=True, text=True, timeout=10
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired, OSError):
        return False


def assess_vulnerability(dep: dict, vulns: list[dict], msf_available: bool) -> list[dict]:
    """Assess each vulnerability and assign severity."""
    findings = []

    for vuln in vulns:
        # Determine severity from CVSS vector or aliases
        severity = "Medium"  # Default
        cvss_score = 0.0

        if vuln["severity_vector"] != "Unknown":
            # Try to extract base score
            score_match = re.search(r"/AV:\w/AC:\w", vuln["severity_vector"])
            if score_match:
                # Rough estimation from vector
                vector = vuln["severity_vector"]
                if "AV:N" in vector and "AC:L" in vector and "PR:N" in vector:
                    severity = "Critical"
                    cvss_score = 9.0
                elif "AV:N" in vector and "AC:L" in vector:
                    severity = "High"
                    cvss_score = 7.5
                elif "AV:N" in vector:
                    severity = "Medium"
                    cvss_score = 5.5
                else:
                    severity = "Low"
                    cvss_score = 3.0

        # Check for Metasploit modules (upgrades severity)
        msf_info = None
        cve_ids = [a for a in vuln.get("aliases", []) if a.startswith("CVE-")]
        if not cve_ids and vuln["id"].startswith("CVE-"):
            cve_ids = [vuln["id"]]

        if msf_available and cve_ids:
            for cve_id in cve_ids[:3]:  # Check up to 3 CVEs
                msf_info = check_msf_modules(cve_id)
                if msf_info:
                    vuln["has_msf_module"] = True
                    if msf_info["exploitable"]:
                        # Upgrade severity if exploit exists
                        if severity in ("Medium", "Low"):
                            severity = "High"
                            cvss_score = max(cvss_score, 7.5)
                    break

        findings.append({
            "dependency": f"{dep['ecosystem']}:{dep['name']}@{dep['version']}",
            "vulnerability_id": vuln["id"],
            "cve_ids": cve_ids,
            "summary": vuln["summary"],
            "severity": severity,
            "cvss_score": cvss_score,
            "severity_vector": vuln["severity_vector"],
            "has_msf_module": vuln["has_msf_module"],
            "msf_modules": msf_info["modules"] if msf_info else [],
            "references": vuln["references"],
            "source_file": dep.get("source", ""),
            "needs_pentest": vuln["has_msf_module"],
        })

    return findings


def scan_dependencies(deps_file: str) -> dict:
    """
    Cross-reference dependencies against vulnerability databases.

    Args:
        deps_file: Path to JSON output from scan_frameworks.py
    """
    deps_data = json.loads(Path(deps_file).read_text(encoding="utf-8"))
    dependencies = deps_data.get("dependencies", [])

    msf_available = check_msf_available()

    results = {
        "msf_available": msf_available,
        "findings": [],
        "needs_pentest": [],
        "stats": {
            "deps_checked": 0,
            "vulns_found": 0,
            "with_msf_modules": 0,
        }
    }

    for dep in dependencies:
        results["stats"]["deps_checked"] += 1

        # Query OSV for vulnerabilities
        vulns = query_osv(dep["ecosystem"], dep["name"], dep["version"])

        if vulns:
            findings = assess_vulnerability(dep, vulns, msf_available)
            results["findings"].extend(findings)
            results["stats"]["vulns_found"] += len(findings)

            # Track items needing pen test
            for f in findings:
                if f["needs_pentest"]:
                    results["needs_pentest"].append(f)
                    results["stats"]["with_msf_modules"] += 1

    # Sort findings by severity
    severity_order = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3}
    results["findings"].sort(key=lambda x: severity_order.get(x["severity"], 4))

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Check dependencies against Metasploit DB and CVE databases"
    )
    parser.add_argument("deps_file", help="Path to dependencies JSON from scan_frameworks.py")
    parser.add_argument("--output", "-o", help="Output JSON file path")
    parser.add_argument("--skip-msf", action="store_true", help="Skip Metasploit checks")
    args = parser.parse_args()

    if not os.path.isfile(args.deps_file):
        print(f"Error: {args.deps_file} not found", file=sys.stderr)
        sys.exit(1)

    results = scan_dependencies(args.deps_file)

    output = json.dumps(results, indent=2, default=str)

    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
        print(f"Results written to {args.output}")
    else:
        print(output)

    # Exit with non-zero if critical/high findings
    critical_high = [f for f in results["findings"] if f["severity"] in ("Critical", "High")]
    if critical_high:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
