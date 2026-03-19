# NemoClaw Blog Post Design

## Approach
"What's New" announcement style. Lead with the news, explain context, then guide readers through installation and practical use.

## Target Audience
Both developers who already use OpenClaw and newcomers curious about AI agents. Quick OpenClaw primer included for context.

## Post Structure

### 1. Opening / Hook
- Lead with the news: NVIDIA just launched NemoClaw
- Open-source security layer for OpenClaw
- One command to sandbox AI agents with real isolation (Landlock, seccomp, network namespaces)
- Why this matters: OpenClaw is popular but runs agents with broad access

### 2. What is OpenClaw (quick primer)
- 2-3 paragraphs max
- What OpenClaw is, why people use it
- The security gap: autonomous agents with broad system access
- Just enough for newcomers, skimmable for experienced users

### 3. What is NemoClaw
- What it does: open-source stack adding privacy and security controls to OpenClaw
- Key components: Plugin (TypeScript CLI), Blueprint (versioned Python artifact), Sandbox (isolated OpenShell container), Inference (NVIDIA cloud routing)
- OpenShell enforces policy-based guardrails
- Four protection layers explained practically:
  - Network: blocks unauthorized outbound connections (hot-reloadable)
  - Filesystem: prevents reads/writes outside /sandbox and /tmp (locked at creation)
  - Process: blocks privilege escalation and dangerous syscalls (locked at creation)
  - Inference: reroutes model API calls to controlled backends (hot-reloadable)
- TUI for monitoring and operator approvals

### 4. Installation
Show both paths with key commands and expected output (not a full tutorial):

**Local/VM:**
- `curl -fsSL https://nvidia.com/nemoclaw.sh | bash`
- `nemoclaw onboard` wizard
- Expected output summary (sandbox name, model, run/status/logs commands)

**Cloud (one-click):**
- NVIDIA's Brev deploy option
- `nemoclaw deploy <instance>` (experimental)

**Key commands after install:**
- `nemoclaw <name> connect` - interactive shell
- `nemoclaw <name> status` - health check
- `nemoclaw <name> logs --follow` - stream logs
- `openshell term` - TUI for monitoring/approvals

### 5. Use Cases
List several with short descriptions, one practical snippet:
- Secure coding assistants (sandboxed agent that can code but can't reach arbitrary endpoints)
- Always-on agents on RTX/DGX hardware (24/7 local compute)
- Team deployments with controlled egress (network policies)
- Telegram-bridged assistants (remote access to sandboxed agent)
- Practical snippet: setting up a sandboxed coding agent with network policies

### 6. NemoClaw vs OpenClaw
Comparison table format:
| Feature | OpenClaw | NemoClaw |
Rows: sandbox isolation, network control, filesystem restrictions, inference routing, process security, installation complexity, monitoring (TUI), cloud deploy

### 7. Closing
- Honest assessment: early preview, not everything is polished
- Where it fits in the AI agents landscape
- No hype, just what's useful now

## Content Guidelines
- Human tone matching blog style (see CLAUDE.md writing examples)
- No em dashes, no AI filler words
- Content Creator agent writes the text
- SEO Specialist agent reviews
- Image Prompt Engineer generates hero image prompt, use nanobanana to create it

## Tags
nemoclaw, nvidia, openclaw, security, ai-agents
