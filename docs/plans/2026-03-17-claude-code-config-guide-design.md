# Blog Post Design: "Where Does This Go?" — A Guide to Claude Code's Config System

## Overview
A layered progression blog post that takes readers from a single CLAUDE.md file to a full config system with hooks, skills, agents, commands, and plugins. The core insight: each mechanism exists because of a tradeoff between "always available" and "context cost."

## Target Audience
Both beginners (just installed Claude Code) and intermediate users (have CLAUDE.md, want to level up). Layered structure lets readers stop at whatever depth matches their needs.

## Tone
Evolution angle opener — personal journey from a single CLAUDE.md to a full system. Real examples mixed with simplified ones. Writing style per CLAUDE.md conventions (conversational, no em dashes, no AI fluff).

## Structure

### Opening (Evolution angle)
Personal journey from a single CLAUDE.md to a full config system. The realization that cramming everything into one file costs context tokens every conversation.

### Layer 1: CLAUDE.md (The Foundation)
- Project instructions loaded into every conversation
- Belongs: personality, conventions, things Claude should always know
- Key insight: prime real estate, every line costs context tokens
- What to put: "treat this as greenfield", "always use pnpm", "never modify proto files"
- What NOT to put: step-by-step workflows, domain knowledge dumps
- Comparison: CLAUDE.md = your project's constitution. Short, high-level, always in effect.

### Layer 2: Rules (.claude/rules/)
- Conditional instructions loaded when relevant files match glob patterns
- Example: rule for *.test.ts that says "always use vitest, never mock the database"
- Comparison: CLAUDE.md = always loaded. Rules = loaded when relevant files are touched.

### Layer 3: Hooks (.claude/settings.json)
- Automated enforcement. Claude can ignore a rule. A hook runs real code.
- Real example (simplified): enforce-worktree blocking edits on main, protect-files guarding .env
- Pre-tool-use vs post-tool-use
- Comparison: Rules = "please do this." Hooks = "you literally can't do this."

### Layer 4: Commands (.claude/commands/)
- Reusable prompts triggered manually with /command-name
- Use for: repetitive workflows on demand like /commit or /deploy
- Comparison: Rules fire automatically. Commands fire when you ask.

### Layer 5: Skills (.claude/skills/ or plugins)
- Deep domain knowledge + structured workflows, too large for permanent context
- Why a skill not a rule: loaded on demand, can contain hundreds of lines, include checklists and decision trees
- Real example (simplified): nanobanana for image generation, jira-manager for tickets
- Comparison: Commands = "run this prompt." Skills = "become an expert at this domain."

### Layer 6: Agents (.claude/agents/)
- Specialized personas with their own system prompts, tool access, behavior
- Key differentiator: agents can consume skills, becoming specialists with deep domain knowledge running in their own context window
- When agent vs skill: agents are independent workers you delegate to, skills are knowledge you absorb
- Real example (simplified): Content Creator agent + writing skills, SEO Specialist + SEO skills
- Comparison: Skills = knowledge you use. Agents = workers you delegate to (who can use skills).

### Layer 7: Plugins & MCP Servers
- Connecting Claude to external tools and services
- Plugins bundle skills, agents, hooks, and commands as a package
- MCP servers give Claude new capabilities (Figma, PostHog, etc.)
- Comparison: Everything above customizes behavior. Plugins extend capabilities.

### The Context Budget (Aha Section)
- Each layer exists because of a tradeoff between "always available" and "context cost"
- CLAUDE.md loads every time. Skills load when triggered. Agents run in their own context.
- Your CLAUDE.md should be a steering wheel, not an encyclopedia

### Decision Guide (closing)
Inline comparison: want Claude to always know X → CLAUDE.md. Know X when working on Y files → Rule. Prevent X → Hook. Run X on demand → Command. Deeply understand X → Skill. Delegate X to a specialist → Agent.

## Metadata
- Estimated length: 1800-2200 words
- Tags: claude-code, workflow, ai, configuration, developer-tools
- Images: hero image needed
- SEO review required before publish
