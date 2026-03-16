#!/usr/bin/env node
/**
 * Pre-tool-use hook: blocks edits to project source files when on the main branch.
 *
 * Forces agents to create a worktree or feature branch before making changes.
 * Config/meta files (.claude/, AGENTS.md, CLAUDE.md, docs/plans/) are exempt
 * so planning and setup work can still happen on main.
 */

import { readFileSync } from 'fs';
import { execFileSync } from 'child_process';

let input;
try {
  input = JSON.parse(readFileSync(0, 'utf8'));
} catch {
  process.exit(0);
}

// Grab the file path from whichever tool is being used
const filePath =
  input.tool_input?.file_path ||
  input.tool_input?.path ||
  input.tool_input?.notebook_path ||
  '';

if (!filePath) process.exit(0);

// Normalize to forward slashes
const p = filePath.replace(/\\/g, '/');

// ── Exempt paths (allowed on main) ──────────────────────────────────────────
const EXEMPT = [
  /\.claude\//,             // Claude config/hooks/skills/settings
  /AGENTS\.md$/,            // Agent instructions
  /CLAUDE\.md$/,            // Claude instructions
  /docs\/plans\//,          // Plan documents
  /\.gitignore$/,           // Git config
  /package\.json$/,         // Dependency changes
  /package-lock\.json$/,
  /pnpm-lock\.yaml$/,
  /yarn\.lock$/,
  /tsconfig.*\.json$/,      // TS config
  /\.eslintrc/,             // Lint config
  /\.prettierrc/,           // Format config
  /memory\//,               // Claude memory files
  /MEMORY\.md$/,
];

const isExempt = EXEMPT.some((pattern) => pattern.test(p));
if (isExempt) process.exit(0);

// ── Check current branch ────────────────────────────────────────────────────
let branch;
try {
  branch = execFileSync('git', ['rev-parse', '--abbrev-ref', 'HEAD'], {
    encoding: 'utf8',
    timeout: 5000,
  }).trim();
} catch {
  // If we can't determine the branch, allow the edit
  process.exit(0);
}

if (branch === 'main' || branch === 'master') {
  const output = JSON.stringify({
    decision: "block",
    reason:
      `⛔  Cannot edit "${filePath}" on the ${branch} branch.\n` +
      `   You MUST create a worktree or feature branch first.\n\n` +
      `   Use the "using-git-worktrees" skill or run:\n` +
      `     git worktree add .worktrees/<feature-name> -b <feature-name>\n\n` +
      `   Then work inside that worktree directory.`
  });
  console.log(output);
  process.exit(0);
}

process.exit(0);
