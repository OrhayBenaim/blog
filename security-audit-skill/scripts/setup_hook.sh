#!/bin/bash
# Security Audit - Git Pre-Commit Hook Installer
# Installs a pre-commit hook that runs the security audit on staged changes.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(dirname "$SCRIPT_DIR")"

# Find git root
GIT_ROOT=$(git rev-parse --show-toplevel 2>/dev/null)
if [ -z "$GIT_ROOT" ]; then
    echo "Error: Not in a git repository"
    exit 1
fi

HOOKS_DIR="$GIT_ROOT/.git/hooks"
HOOK_FILE="$HOOKS_DIR/pre-commit"

# Check if pre-commit hook already exists
if [ -f "$HOOK_FILE" ]; then
    if grep -q "security-audit" "$HOOK_FILE"; then
        echo "Security audit hook already installed."
        exit 0
    fi
    echo "Existing pre-commit hook found. Appending security audit..."
    echo "" >> "$HOOK_FILE"
else
    echo "#!/bin/bash" > "$HOOK_FILE"
    chmod +x "$HOOK_FILE"
fi

# Append the security audit hook
cat >> "$HOOK_FILE" << 'HOOK_CONTENT'

# === Security Audit Pre-Commit Hook ===
# Scans staged files for exposed secrets before allowing commit

security_audit_precommit() {
    # Get list of staged files (only added/modified, not deleted)
    STAGED_FILES=$(git diff --cached --name-only --diff-filter=ACM)

    if [ -z "$STAGED_FILES" ]; then
        return 0
    fi

    # Find the scan_keys.py script
    SCAN_SCRIPT="$HOME/.claude/skills/security-audit/scripts/scan_keys.py"

    if [ ! -f "$SCAN_SCRIPT" ]; then
        echo "[security-audit] Warning: scan_keys.py not found at $SCAN_SCRIPT"
        return 0
    fi

    echo "[security-audit] Scanning staged files for exposed secrets..."

    # Create temp file for results
    RESULT_FILE=$(mktemp)

    # Run key scanner on staged files
    python3 "$SCAN_SCRIPT" "$(git rev-parse --show-toplevel)" \
        --changed-files $STAGED_FILES \
        --output "$RESULT_FILE" 2>/dev/null

    EXIT_CODE=$?

    if [ $EXIT_CODE -ne 0 ]; then
        echo ""
        echo "========================================="
        echo "  SECURITY AUDIT: SECRETS DETECTED!"
        echo "========================================="
        echo ""

        # Parse and display findings
        if command -v python3 &> /dev/null; then
            python3 -c "
import json, sys
data = json.load(open('$RESULT_FILE'))
for f in data.get('obvious', []):
    print(f\"  CRITICAL: {f['name']} in {f['file']}:{f['line']}\")
    print(f\"            Match: {f['matched']}\")
    print()
for f in data.get('investigate', []):
    print(f\"  WARNING:  {f['name']} in {f['file']}:{f['line']}\")
    print(f\"            Match: {f['matched']}\")
    print()
" 2>/dev/null
        fi

        echo "Commit blocked. Remove secrets before committing."
        echo "To bypass (NOT recommended): git commit --no-verify"
        echo ""

        rm -f "$RESULT_FILE"
        return 1
    fi

    rm -f "$RESULT_FILE"
    echo "[security-audit] No secrets detected. Proceeding with commit."
    return 0
}

security_audit_precommit
if [ $? -ne 0 ]; then
    exit 1
fi
# === End Security Audit Hook ===
HOOK_CONTENT

echo "Security audit pre-commit hook installed at: $HOOK_FILE"
echo ""
echo "The hook will scan staged files for exposed secrets before each commit."
echo "To bypass (not recommended): git commit --no-verify"
