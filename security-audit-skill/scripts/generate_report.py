#!/usr/bin/env python3
"""
Security Audit - Report Generator
Generates both Markdown (for agent fix) and HTML (for user review) reports
from scan results.
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

SKILL_DIR = Path(__file__).parent.parent
HTML_TEMPLATE_PATH = SKILL_DIR / "assets" / "report_template.html"


def load_results(*result_files: str) -> dict:
    """Load and merge all scan result files."""
    merged = {
        "key_findings": {"obvious": [], "investigate": []},
        "vuln_findings": [],
        "needs_pentest": [],
        "scan_stats": {},
    }

    for filepath in result_files:
        if not filepath or not os.path.isfile(filepath):
            continue
        data = json.loads(Path(filepath).read_text(encoding="utf-8"))

        # Key scan results
        if "obvious" in data:
            merged["key_findings"]["obvious"].extend(data["obvious"])
            merged["key_findings"]["investigate"].extend(data.get("investigate", []))
            merged["scan_stats"]["key_scan"] = data.get("scan_stats", {})

        # Vulnerability scan results
        if "findings" in data:
            merged["vuln_findings"].extend(data["findings"])
            merged["needs_pentest"].extend(data.get("needs_pentest", []))
            merged["scan_stats"]["vuln_scan"] = data.get("stats", {})

    return merged


def severity_badge(severity: str) -> str:
    """Generate markdown severity badge."""
    icons = {
        "Critical": "CRITICAL",
        "High": "HIGH",
        "Medium": "MEDIUM",
        "Low": "LOW",
        "Info": "INFO",
    }
    return f"**[{icons.get(severity, severity)}]**"


def generate_markdown(results: dict, output_path: str, project_name: str = ""):
    """Generate Markdown report optimized for agent consumption (fixing issues)."""
    lines = []
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines.append(f"# Security Audit Report")
    if project_name:
        lines.append(f"**Project:** {project_name}")
    lines.append(f"**Generated:** {timestamp}")
    lines.append("")

    # Summary
    total_critical = len([f for f in results["key_findings"]["obvious"] if f.get("severity") == "Critical"])
    total_critical += len([f for f in results["vuln_findings"] if f.get("severity") == "Critical"])
    total_high = len([f for f in results["key_findings"]["obvious"] if f.get("severity") == "High"])
    total_high += len([f for f in results["vuln_findings"] if f.get("severity") == "High"])
    total_medium = len([f for f in results["key_findings"]["investigate"]])
    total_medium += len([f for f in results["vuln_findings"] if f.get("severity") == "Medium"])

    lines.append("## Summary")
    lines.append("")
    lines.append(f"| Severity | Count |")
    lines.append(f"|----------|-------|")
    lines.append(f"| Critical | {total_critical} |")
    lines.append(f"| High | {total_high} |")
    lines.append(f"| Medium | {total_medium} |")
    lines.append("")

    if total_critical > 0:
        lines.append("> **ACTION REQUIRED:** Critical findings must be fixed immediately before deployment.")
        lines.append("")

    # Exposed Keys - OBVIOUS
    if results["key_findings"]["obvious"]:
        lines.append("## Exposed Secrets (Immediate Fix Required)")
        lines.append("")
        for finding in results["key_findings"]["obvious"]:
            lines.append(f"### {severity_badge(finding['severity'])} {finding['name']}")
            lines.append("")
            lines.append(f"- **File:** `{finding['file']}:{finding['line']}`")
            lines.append(f"- **Match:** `{finding['matched']}`")
            lines.append(f"- **Severity:** {finding['severity']}")
            lines.append("")
            lines.append("**Remediation:**")
            lines.append("1. Remove the secret from source code immediately")
            lines.append("2. Move to environment variable or secrets manager")
            lines.append("3. Rotate the exposed credential")
            lines.append("4. Check access logs for unauthorized usage")
            lines.append("")

    # Exposed Keys - INVESTIGATE
    if results["key_findings"]["investigate"]:
        lines.append("## Keys Requiring Investigation")
        lines.append("")
        for finding in results["key_findings"]["investigate"]:
            lines.append(f"### {severity_badge(finding.get('severity', 'Medium'))} {finding['name']}")
            lines.append("")
            lines.append(f"- **File:** `{finding['file']}:{finding['line']}`")
            lines.append(f"- **Match:** `{finding['matched']}`")
            lines.append(f"- **Classification:** Needs permission check")
            lines.append("")
            lines.append("**Action:** Verify this key's permissions and determine if exposure is acceptable.")
            lines.append("")

    # Vulnerable Dependencies
    if results["vuln_findings"]:
        lines.append("## Vulnerable Dependencies")
        lines.append("")
        for finding in results["vuln_findings"]:
            msf_tag = " [MSF MODULE AVAILABLE]" if finding.get("has_msf_module") else ""
            lines.append(f"### {severity_badge(finding['severity'])} {finding['dependency']}{msf_tag}")
            lines.append("")
            lines.append(f"- **Vulnerability:** {finding['vulnerability_id']}")
            if finding.get("cve_ids"):
                lines.append(f"- **CVE:** {', '.join(finding['cve_ids'])}")
            lines.append(f"- **Severity:** {finding['severity']}")
            if finding.get("severity_vector") and finding["severity_vector"] != "Unknown":
                lines.append(f"- **CVSS Vector:** {finding['severity_vector']}")
            lines.append(f"- **Source:** `{finding.get('source_file', 'N/A')}`")
            lines.append("")
            lines.append(f"**Description:** {finding.get('summary', 'No description available.')}")
            lines.append("")

            if finding.get("msf_modules"):
                lines.append("**Metasploit Modules:**")
                for mod in finding["msf_modules"]:
                    lines.append(f"- `{mod['module_path']}`")
                lines.append("")

            lines.append("**Remediation:** Update to a patched version.")
            if finding.get("references"):
                lines.append("")
                lines.append("**References:**")
                for ref in finding["references"][:3]:
                    lines.append(f"- {ref}")
            lines.append("")

    # Pen test recommendations
    if results["needs_pentest"]:
        lines.append("## Recommended Pen Testing")
        lines.append("")
        lines.append("The following vulnerabilities have known Metasploit modules and should be actively tested:")
        lines.append("")
        for item in results["needs_pentest"]:
            lines.append(f"- **{item['dependency']}** - {item['vulnerability_id']} ({item['severity']})")
        lines.append("")

    # Write file
    Path(output_path).write_text("\n".join(lines), encoding="utf-8")
    return output_path


def generate_html(results: dict, output_path: str, project_name: str = ""):
    """Generate HTML report for user viewing."""
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    # Load HTML template
    if HTML_TEMPLATE_PATH.is_file():
        template = HTML_TEMPLATE_PATH.read_text(encoding="utf-8")
    else:
        template = DEFAULT_HTML_TEMPLATE

    # Build findings HTML
    findings_html = ""

    # Key findings
    all_key_findings = results["key_findings"]["obvious"] + results["key_findings"]["investigate"]
    for f in all_key_findings:
        sev = f.get("severity", "Medium")
        sev_class = sev.lower()
        findings_html += f"""
        <div class="finding {sev_class}">
            <div class="finding-header">
                <span class="severity-badge {sev_class}">{sev.upper()}</span>
                <span class="finding-title">{f['name']}</span>
            </div>
            <div class="finding-details">
                <div class="detail-row"><span class="label">File:</span> <code>{f['file']}:{f['line']}</code></div>
                <div class="detail-row"><span class="label">Match:</span> <code>{f['matched']}</code></div>
                <div class="detail-row"><span class="label">Classification:</span> {f['classification']}</div>
            </div>
        </div>
        """

    # Vulnerability findings
    for f in results["vuln_findings"]:
        sev = f.get("severity", "Medium")
        sev_class = sev.lower()
        msf_badge = '<span class="msf-badge">MSF</span>' if f.get("has_msf_module") else ""
        cve_text = ", ".join(f.get("cve_ids", [])) or f["vulnerability_id"]
        findings_html += f"""
        <div class="finding {sev_class}">
            <div class="finding-header">
                <span class="severity-badge {sev_class}">{sev.upper()}</span>
                <span class="finding-title">{f['dependency']}</span>
                {msf_badge}
            </div>
            <div class="finding-details">
                <div class="detail-row"><span class="label">CVE:</span> {cve_text}</div>
                <div class="detail-row"><span class="label">Description:</span> {f.get('summary', 'N/A')[:300]}</div>
                <div class="detail-row"><span class="label">Source:</span> <code>{f.get('source_file', 'N/A')}</code></div>
            </div>
        </div>
        """

    # Count stats
    total = len(all_key_findings) + len(results["vuln_findings"])
    critical = len([f for f in all_key_findings if f.get("severity") == "Critical"])
    critical += len([f for f in results["vuln_findings"] if f.get("severity") == "Critical"])
    high = len([f for f in all_key_findings if f.get("severity") == "High"])
    high += len([f for f in results["vuln_findings"] if f.get("severity") == "High"])

    # Replace placeholders in template
    html = template.replace("{{PROJECT_NAME}}", project_name or "Security Audit")
    html = html.replace("{{TIMESTAMP}}", timestamp)
    html = html.replace("{{TOTAL_FINDINGS}}", str(total))
    html = html.replace("{{CRITICAL_COUNT}}", str(critical))
    html = html.replace("{{HIGH_COUNT}}", str(high))
    html = html.replace("{{FINDINGS}}", findings_html)

    Path(output_path).write_text(html, encoding="utf-8")
    return output_path


DEFAULT_HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{PROJECT_NAME}} - Security Audit Report</title>
<style>
/* See assets/report_template.html for the full styled template */
body { font-family: system-ui, sans-serif; max-width: 900px; margin: 0 auto; padding: 2rem; background: #0a0a0a; color: #e0e0e0; }
.finding { border: 1px solid #333; border-radius: 8px; padding: 1rem; margin: 1rem 0; }
.finding.critical { border-left: 4px solid #ff4444; }
.finding.high { border-left: 4px solid #ff8800; }
.finding.medium { border-left: 4px solid #ffcc00; }
.finding.low { border-left: 4px solid #44aa44; }
.severity-badge { padding: 2px 8px; border-radius: 4px; font-size: 0.75rem; font-weight: bold; color: white; }
.severity-badge.critical { background: #ff4444; }
.severity-badge.high { background: #ff8800; }
.severity-badge.medium { background: #ffcc00; color: #000; }
.severity-badge.low { background: #44aa44; }
.msf-badge { background: #6644ff; color: white; padding: 2px 6px; border-radius: 4px; font-size: 0.7rem; margin-left: 0.5rem; }
.finding-header { display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem; }
.finding-title { font-weight: 600; }
.detail-row { margin: 0.25rem 0; font-size: 0.9rem; }
.label { color: #888; }
code { background: #1a1a2e; padding: 2px 6px; border-radius: 3px; font-size: 0.85rem; }
h1 { color: #ff4444; }
.stats { display: flex; gap: 2rem; margin: 1rem 0; }
.stat { text-align: center; }
.stat-num { font-size: 2rem; font-weight: bold; }
</style>
</head>
<body>
<h1>{{PROJECT_NAME}}</h1>
<p>Security Audit Report - {{TIMESTAMP}}</p>
<div class="stats">
<div class="stat"><div class="stat-num">{{TOTAL_FINDINGS}}</div><div>Total Findings</div></div>
<div class="stat"><div class="stat-num" style="color:#ff4444">{{CRITICAL_COUNT}}</div><div>Critical</div></div>
<div class="stat"><div class="stat-num" style="color:#ff8800">{{HIGH_COUNT}}</div><div>High</div></div>
</div>
<h2>Findings</h2>
{{FINDINGS}}
</body>
</html>"""


def main():
    parser = argparse.ArgumentParser(description="Generate security audit reports")
    parser.add_argument("--keys-result", help="Path to key scan results JSON")
    parser.add_argument("--vuln-result", help="Path to vulnerability scan results JSON")
    parser.add_argument("--output-dir", "-o", required=True, help="Output directory for reports")
    parser.add_argument("--project", default="", help="Project name for report header")
    args = parser.parse_args()

    # Create timestamped output directory under docs/audit/
    timestamp_dir = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H-%M-%S")
    output_dir = os.path.join(args.output_dir, "docs", "audit", timestamp_dir)
    os.makedirs(output_dir, exist_ok=True)

    results = load_results(args.keys_result, args.vuln_result)

    md_path = os.path.join(output_dir, "security-audit-report.md")
    html_path = os.path.join(output_dir, "security-audit-report.html")

    generate_markdown(results, md_path, args.project)
    generate_html(results, html_path, args.project)

    print(f"Reports generated:")
    print(f"  Markdown: {md_path}")
    print(f"  HTML:     {html_path}")

    # Check if any critical findings exist
    has_critical = any(
        f.get("severity") == "Critical"
        for f in results["key_findings"]["obvious"] + results["vuln_findings"]
    )
    sys.exit(1 if has_critical else 0)


if __name__ == "__main__":
    main()
