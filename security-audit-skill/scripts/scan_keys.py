#!/usr/bin/env python3
"""
Security Audit - API Key Scanner
Scans source and build directories for exposed API keys and secrets.
Classifies findings as OBVIOUS (report immediately) or INVESTIGATE (check permissions).
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

# Key patterns: (name, regex, classification, severity_if_obvious)
KEY_PATTERNS = [
    # AWS
    ("AWS Access Key ID", r"AKIA[0-9A-Z]{16}", "OBVIOUS", "Critical"),
    ("AWS Secret Access Key", r"(?i)aws_secret_access_key\s*[=:]\s*[A-Za-z0-9/+=]{40}", "OBVIOUS", "Critical"),
    ("AWS Session Token", r"(?i)aws_session_token\s*[=:]\s*[A-Za-z0-9/+=]+", "OBVIOUS", "Critical"),

    # Google Cloud / Firebase
    ("GCP API Key", r"AIza[0-9A-Za-z\-_]{35}", "OBVIOUS", "High"),
    ("GCP Service Account JSON", r'"type"\s*:\s*"service_account"', "OBVIOUS", "Critical"),
    ("Firebase Client Config", r"(?i)firebase(?:Config|app).*apiKey", "INVESTIGATE", "Medium"),

    # GitHub
    ("GitHub Personal Access Token", r"ghp_[0-9a-zA-Z]{36}", "OBVIOUS", "Critical"),
    ("GitHub Fine-Grained PAT", r"github_pat_[0-9a-zA-Z_]{82}", "OBVIOUS", "Critical"),
    ("GitHub OAuth Token", r"gho_[0-9a-zA-Z]{36}", "OBVIOUS", "High"),
    ("GitHub App Installation Token", r"ghs_[0-9a-zA-Z]{36}", "OBVIOUS", "High"),

    # Stripe
    ("Stripe Secret Key", r"sk_live_[0-9a-zA-Z]{24,}", "OBVIOUS", "Critical"),
    ("Stripe Restricted Key", r"rk_live_[0-9a-zA-Z]{24,}", "OBVIOUS", "High"),
    ("Stripe Publishable Key", r"pk_live_[0-9a-zA-Z]{24,}", "INVESTIGATE", "Low"),

    # Supabase
    ("Supabase Service Role Key", r"(?i)supabase.*service.role.*eyJ[A-Za-z0-9_-]+\.eyJ[A-Za-z0-9_-]+", "OBVIOUS", "Critical"),
    ("Supabase Anon Key", r"(?i)supabase.*anon.*eyJ[A-Za-z0-9_-]+\.eyJ[A-Za-z0-9_-]+", "INVESTIGATE", "Medium"),

    # Database Connection Strings
    ("PostgreSQL Connection String", r"postgres(?:ql)?://[^:]+:[^@]+@[^/]+", "OBVIOUS", "Critical"),
    ("MongoDB Connection String", r"mongodb(?:\+srv)?://[^:]+:[^@]+@", "OBVIOUS", "Critical"),
    ("Redis URL with Password", r"redis://:[^@]+@", "OBVIOUS", "High"),
    ("MySQL Connection String", r"mysql://[^:]+:[^@]+@", "OBVIOUS", "Critical"),

    # JWT / Private Keys
    ("JWT Secret", r'(?i)(?:jwt_secret|jwt_key|secret_key)\s*[=:]\s*["\'][^"\']{8,}["\']', "OBVIOUS", "Critical"),
    ("Private Key Block", r"-----BEGIN (?:RSA|EC|DSA|OPENSSH) PRIVATE KEY-----", "OBVIOUS", "Critical"),

    # Email / SMS Services
    ("SendGrid API Key", r"SG\.[0-9A-Za-z\-_]{22}\.[0-9A-Za-z\-_]{43}", "OBVIOUS", "High"),
    ("Mailgun API Key", r"key-[0-9a-zA-Z]{32}", "OBVIOUS", "High"),
    ("Twilio Auth Token", r"(?i)twilio.*[0-9a-f]{32}", "OBVIOUS", "High"),

    # AI Services
    ("OpenAI API Key", r"sk-[0-9a-zA-Z]{20}T3BlbkFJ[0-9a-zA-Z]{20}", "OBVIOUS", "High"),
    ("OpenAI Project Key", r"sk-proj-[0-9a-zA-Z_-]{80,}", "OBVIOUS", "High"),
    ("Anthropic API Key", r"sk-ant-[0-9a-zA-Z_-]{80,}", "OBVIOUS", "High"),

    # Slack
    ("Slack Bot Token", r"xoxb-[0-9]{10,}-[0-9a-zA-Z]{24,}", "OBVIOUS", "High"),
    ("Slack User Token", r"xoxp-[0-9]{10,}-[0-9]{10,}-[0-9a-zA-Z]{24,}", "OBVIOUS", "Critical"),
    ("Slack Webhook URL", r"https://hooks\.slack\.com/services/T[0-9A-Z]+/B[0-9A-Z]+/[0-9a-zA-Z]+", "OBVIOUS", "Medium"),

    # Generic
    ("Generic API Key", r'(?i)(?:api_key|apikey|api_secret|secret_key)\s*[=:]\s*["\'][0-9a-zA-Z]{16,}["\']', "INVESTIGATE", "Medium"),
    ("Generic Password", r'(?i)(?:password|passwd|pwd)\s*[=:]\s*["\'][^"\']{8,}["\']', "INVESTIGATE", "Medium"),
    ("Hardcoded Bearer Token", r'(?i)(?:authorization|bearer)\s*[=:]\s*["\']Bearer\s+[0-9a-zA-Z._-]+["\']', "OBVIOUS", "High"),
]

# File extensions to skip (binary, images, etc.)
SKIP_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".ico", ".svg", ".webp",
    ".woff", ".woff2", ".ttf", ".eot", ".otf",
    ".mp3", ".mp4", ".wav", ".avi", ".mov",
    ".zip", ".tar", ".gz", ".rar", ".7z",
    ".exe", ".dll", ".so", ".dylib",
    ".pdf", ".doc", ".docx", ".xls", ".xlsx",
    ".pyc", ".pyo", ".class",
    ".lock",
}

# Files/dirs to always skip
SKIP_NAMES = {
    ".env", ".env.local", ".env.development", ".env.production", ".env.test",
    "node_modules", ".git", "__pycache__", ".venv", "venv",
}

# Placeholder patterns to ignore
PLACEHOLDER_PATTERNS = [
    r"(?i)your[_-]?api[_-]?key",
    r"(?i)changeme",
    r"(?i)placeholder",
    r"(?i)example",
    r"(?i)xxx+",
    r"(?i)insert[_-]?here",
    r"(?i)todo",
    r"(?i)replace[_-]?with",
    r"(?i)<[^>]+>",
]


def is_placeholder(value: str) -> bool:
    """Check if a matched value looks like a placeholder."""
    for pattern in PLACEHOLDER_PATTERNS:
        if re.search(pattern, value):
            return True
    return False


def should_skip_file(filepath: Path) -> bool:
    """Check if file should be skipped."""
    # Skip by extension
    if filepath.suffix.lower() in SKIP_EXTENSIONS:
        return True

    # Skip by name
    for part in filepath.parts:
        if part in SKIP_NAMES:
            return True

    return False


def scan_file(filepath: Path) -> list[dict]:
    """Scan a single file for key patterns."""
    findings = []

    try:
        content = filepath.read_text(encoding="utf-8", errors="ignore")
    except (PermissionError, OSError):
        return findings

    lines = content.split("\n")

    for line_num, line in enumerate(lines, 1):
        for name, pattern, classification, severity in KEY_PATTERNS:
            matches = re.finditer(pattern, line)
            for match in matches:
                matched_text = match.group(0)

                # Skip placeholders
                if is_placeholder(matched_text):
                    continue

                # Mask the key for reporting (show first/last 4 chars)
                if len(matched_text) > 12:
                    masked = matched_text[:4] + "..." + matched_text[-4:]
                else:
                    masked = matched_text[:4] + "..."

                findings.append({
                    "name": name,
                    "classification": classification,
                    "severity": severity,
                    "file": str(filepath),
                    "line": line_num,
                    "matched": masked,
                    "full_match": matched_text,
                    "context": line.strip()[:200],
                })

    return findings


def scan_directory(target_dir: str, changed_files: list[str] | None = None) -> dict:
    """
    Scan directory for exposed keys.

    Args:
        target_dir: Directory to scan
        changed_files: If provided, only scan these files (for git changes mode)

    Returns:
        Dict with 'obvious' and 'investigate' finding lists
    """
    results = {
        "obvious": [],
        "investigate": [],
        "scan_stats": {
            "files_scanned": 0,
            "files_skipped": 0,
            "total_findings": 0,
        }
    }

    if changed_files:
        files_to_scan = [Path(f) for f in changed_files if Path(f).is_file()]
    else:
        target = Path(target_dir)
        files_to_scan = [f for f in target.rglob("*") if f.is_file()]

    for filepath in files_to_scan:
        if should_skip_file(filepath):
            results["scan_stats"]["files_skipped"] += 1
            continue

        results["scan_stats"]["files_scanned"] += 1
        findings = scan_file(filepath)

        for finding in findings:
            if finding["classification"] == "OBVIOUS":
                results["obvious"].append(finding)
            else:
                results["investigate"].append(finding)

    results["scan_stats"]["total_findings"] = len(results["obvious"]) + len(results["investigate"])
    return results


def main():
    parser = argparse.ArgumentParser(description="Scan for exposed API keys and secrets")
    parser.add_argument("target", help="Directory to scan")
    parser.add_argument("--changed-files", nargs="*", help="Only scan specific files (git changes mode)")
    parser.add_argument("--output", "-o", help="Output JSON file path")
    args = parser.parse_args()

    if not os.path.isdir(args.target):
        print(f"Error: {args.target} is not a directory", file=sys.stderr)
        sys.exit(1)

    results = scan_directory(args.target, args.changed_files)

    output = json.dumps(results, indent=2, default=str)

    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
        print(f"Results written to {args.output}")
    else:
        print(output)

    # Exit with non-zero if critical findings
    if results["obvious"]:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
