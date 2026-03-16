#!/usr/bin/env python3
"""
Security Audit - Framework & Dependency Version Scanner
Extracts framework/library versions from package manifests and build artifacts.
Outputs structured JSON for cross-referencing with vulnerability databases.
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path


def scan_package_json(filepath: Path) -> list[dict]:
    """Extract dependencies from package.json."""
    deps = []
    try:
        data = json.loads(filepath.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return deps

    for dep_type in ["dependencies", "devDependencies"]:
        for name, version in data.get(dep_type, {}).items():
            # Clean version string (remove ^, ~, >=, etc.)
            clean_version = re.sub(r"^[\^~>=<]+", "", version)
            deps.append({
                "name": name,
                "version": clean_version,
                "raw_version": version,
                "source": str(filepath),
                "ecosystem": "npm",
                "dev": dep_type == "devDependencies",
            })
    return deps


def scan_package_lock(filepath: Path) -> list[dict]:
    """Extract resolved versions from package-lock.json (top-level only)."""
    deps = []
    try:
        data = json.loads(filepath.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return deps

    packages = data.get("packages", {})
    for pkg_path, info in packages.items():
        if pkg_path == "":
            continue
        # Only top-level: node_modules/<name> (no nested)
        parts = pkg_path.replace("node_modules/", "").split("/")
        if len(parts) <= 2:  # handle scoped packages @scope/name
            name = pkg_path.replace("node_modules/", "")
            version = info.get("version", "unknown")
            deps.append({
                "name": name,
                "version": version,
                "raw_version": version,
                "source": str(filepath),
                "ecosystem": "npm",
                "dev": info.get("dev", False),
            })
    return deps


def scan_requirements_txt(filepath: Path) -> list[dict]:
    """Extract dependencies from requirements.txt."""
    deps = []
    try:
        lines = filepath.read_text(encoding="utf-8").splitlines()
    except OSError:
        return deps

    for line in lines:
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("-"):
            continue
        # Handle name==version, name>=version, name~=version
        match = re.match(r"^([a-zA-Z0-9_-]+)\s*[=~<>!]+\s*([0-9][^\s;,]*)", line)
        if match:
            deps.append({
                "name": match.group(1),
                "version": match.group(2),
                "raw_version": line,
                "source": str(filepath),
                "ecosystem": "pypi",
                "dev": False,
            })
    return deps


def scan_pyproject_toml(filepath: Path) -> list[dict]:
    """Extract dependencies from pyproject.toml (basic parsing)."""
    deps = []
    try:
        content = filepath.read_text(encoding="utf-8")
    except OSError:
        return deps

    # Simple regex for dependencies = ["name>=version", ...]
    dep_matches = re.findall(r'"([a-zA-Z0-9_-]+)\s*[><=~!]+\s*([0-9][^"]*)"', content)
    for name, version in dep_matches:
        deps.append({
            "name": name,
            "version": version.strip(),
            "raw_version": f"{name}>={version}",
            "source": str(filepath),
            "ecosystem": "pypi",
            "dev": False,
        })
    return deps


def scan_gemfile_lock(filepath: Path) -> list[dict]:
    """Extract dependencies from Gemfile.lock."""
    deps = []
    try:
        content = filepath.read_text(encoding="utf-8")
    except OSError:
        return deps

    in_specs = False
    for line in content.splitlines():
        if line.strip() == "specs:":
            in_specs = True
            continue
        if in_specs:
            match = re.match(r"^\s{4}(\S+)\s+\(([^)]+)\)", line)
            if match:
                deps.append({
                    "name": match.group(1),
                    "version": match.group(2),
                    "raw_version": match.group(2),
                    "source": str(filepath),
                    "ecosystem": "rubygems",
                    "dev": False,
                })
            elif not line.startswith(" "):
                in_specs = False
    return deps


def scan_go_mod(filepath: Path) -> list[dict]:
    """Extract dependencies from go.mod."""
    deps = []
    try:
        content = filepath.read_text(encoding="utf-8")
    except OSError:
        return deps

    for match in re.finditer(r"^\s+(\S+)\s+(v[\d.]+\S*)", content, re.MULTILINE):
        deps.append({
            "name": match.group(1),
            "version": match.group(2),
            "raw_version": match.group(2),
            "source": str(filepath),
            "ecosystem": "go",
            "dev": False,
        })
    return deps


def scan_composer_json(filepath: Path) -> list[dict]:
    """Extract dependencies from composer.json (PHP)."""
    deps = []
    try:
        data = json.loads(filepath.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return deps

    for dep_type in ["require", "require-dev"]:
        for name, version in data.get(dep_type, {}).items():
            if name == "php":
                continue
            clean_version = re.sub(r"^[\^~>=<]+", "", version)
            deps.append({
                "name": name,
                "version": clean_version,
                "raw_version": version,
                "source": str(filepath),
                "ecosystem": "composer",
                "dev": dep_type == "require-dev",
            })
    return deps


def scan_build_artifacts(dist_dir: Path) -> list[dict]:
    """Scan built JS files for framework version strings."""
    deps = []
    version_patterns = [
        (r"React v?(\d+\.\d+\.\d+)", "react"),
        (r"vue(?:\.runtime)?\.(?:global|esm).*?(\d+\.\d+\.\d+)", "vue"),
        (r"Angular v?(\d+\.\d+\.\d+)", "@angular/core"),
        (r"Next\.js v?(\d+\.\d+\.\d+)", "next"),
        (r"Svelte v?(\d+\.\d+\.\d+)", "svelte"),
        (r"jQuery v?(\d+\.\d+\.\d+)", "jquery"),
        (r"lodash (\d+\.\d+\.\d+)", "lodash"),
        (r"Express (\d+\.\d+\.\d+)", "express"),
    ]

    for filepath in dist_dir.rglob("*.js"):
        try:
            content = filepath.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue

        for pattern, name in version_patterns:
            match = re.search(pattern, content)
            if match:
                deps.append({
                    "name": name,
                    "version": match.group(1),
                    "raw_version": match.group(0),
                    "source": str(filepath),
                    "ecosystem": "npm",
                    "dev": False,
                    "from_build": True,
                })
    return deps


SCANNERS = {
    "package.json": scan_package_json,
    "package-lock.json": scan_package_lock,
    "requirements.txt": scan_requirements_txt,
    "pyproject.toml": scan_pyproject_toml,
    "Gemfile.lock": scan_gemfile_lock,
    "go.mod": scan_go_mod,
    "composer.json": scan_composer_json,
}


def scan_directory(target_dir: str) -> dict:
    """Scan directory for all dependency manifests and build artifacts."""
    target = Path(target_dir)
    all_deps = []

    # Scan manifest files
    for filename, scanner in SCANNERS.items():
        for filepath in target.rglob(filename):
            # Skip node_modules
            if "node_modules" in filepath.parts:
                continue
            all_deps.extend(scanner(filepath))

    # Scan build directories
    for dist_name in ["dist", "build", "out", ".next", "public"]:
        dist_dir = target / dist_name
        if dist_dir.is_dir():
            all_deps.extend(scan_build_artifacts(dist_dir))

    # Deduplicate (prefer non-dev, prefer lock file versions)
    seen = {}
    for dep in all_deps:
        key = f"{dep['ecosystem']}:{dep['name']}"
        if key not in seen or (not dep.get("dev") and seen[key].get("dev")):
            seen[key] = dep

    unique_deps = list(seen.values())

    return {
        "dependencies": unique_deps,
        "stats": {
            "total": len(unique_deps),
            "by_ecosystem": {},
        }
    }


def main():
    parser = argparse.ArgumentParser(description="Scan for framework and dependency versions")
    parser.add_argument("target", help="Directory to scan")
    parser.add_argument("--output", "-o", help="Output JSON file path")
    args = parser.parse_args()

    if not os.path.isdir(args.target):
        print(f"Error: {args.target} is not a directory", file=sys.stderr)
        sys.exit(1)

    results = scan_directory(args.target)

    # Calculate ecosystem stats
    for dep in results["dependencies"]:
        eco = dep["ecosystem"]
        results["stats"]["by_ecosystem"][eco] = results["stats"]["by_ecosystem"].get(eco, 0) + 1

    output = json.dumps(results, indent=2, default=str)

    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
        print(f"Results written to {args.output}")
    else:
        print(output)


if __name__ == "__main__":
    main()
