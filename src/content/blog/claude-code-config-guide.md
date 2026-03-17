---
title: "Claude Code Config Guide: Where Every Setting Actually Belongs"
description: "A complete guide to Claude Code's seven config layers: CLAUDE.md, rules, hooks, commands, skills, agents, and plugins. What each one does, where it lives, and why keeping your config slim saves context tokens."
pubDate: 2026-03-17
pubTime: "12:00"
tags: ["claude-code", "workflow", "ai", "configuration", "developer-tools"]
---

My first Claude Code CLAUDE.md was a mess. Thirty lines of project conventions, then a hundred lines of step-by-step workflows, a full testing checklist, a list of every API endpoint in the app, and a paragraph about how to format commit messages. It worked. Claude followed it. But every single conversation started by loading all of that into context, whether it was relevant or not.

That's when it clicked. Context tokens aren't free. Every line in CLAUDE.md is a line that loads into every conversation, every time, no exceptions. My config file wasn't a config file anymore. It was a manual. And Claude was reading the entire manual before doing anything.

So I started pulling things out. Moved the testing rules into conditional files that only load when test files are involved. Turned the deployment workflow into a command I trigger manually. Extracted domain knowledge into skills that load on demand. Eventually, the system had layers, and each layer existed for a reason.

This post walks through all of them. Where each piece of config lives, what it does, and why you'd pick one over another.

![Claude Code's seven configuration layers from CLAUDE.md to plugins, visualized as colorful stacked acrylic panels](/blog/blog/claude-code-config-guide-hero.webp)

Here's the quick overview. Each layer trades off between "always available" and "context cost":

| Layer | Location | When It Loads | Context Cost |
|-------|----------|---------------|--------------|
| CLAUDE.md | Project root | Every conversation | High |
| Rules | .claude/rules/ | When matching files are touched | Medium |
| Hooks | .claude/settings.json | On tool use events | None (runs scripts) |
| Commands | .claude/commands/ | When manually invoked | None until used |
| Skills | .claude/skills/ | On demand | None until loaded |
| Agents | .claude/agents/ | When delegated to | Separate context |
| Plugins/MCP | Installed packages | When capabilities needed | Varies |

## Layer 1: CLAUDE.md (The Foundation)

CLAUDE.md sits at the root of your project. It loads into every conversation automatically. No conditions, no triggers. Claude reads it before doing anything else.

This makes it prime real estate. Every line costs context tokens, and those tokens come out of the budget you'd rather spend on actual work. So the goal is to keep it tight. High-level project conventions. Personality and tone rules. The stuff Claude should never forget.

Good things to put here:

- Always use pnpm, not npm
- Never modify .proto files directly
- This project uses Astro with TypeScript
- Run tests with vitest before committing

Bad things to put here: a full tutorial on how your authentication system works, a step-by-step deploy checklist, or a wall of API documentation. Those belong somewhere else.

Think of CLAUDE.md as your project's constitution. Short, high-level, always in effect. If you're writing more than 40-50 lines, you're probably stuffing things in that should live in another layer.

## Layer 2: Rules (.claude/rules/)

Claude Code rules are conditional instructions. They live in `.claude/rules/` and each rule file has a glob pattern at the top. When Claude touches a file that matches the pattern, the rule loads. When it doesn't, the rule stays out of context entirely.

Here's a real example. Say you have a rule for test files:

```
---
globs: ["*.test.ts", "*.spec.ts"]
---
Always use vitest. Never mock the database, use the test database container instead. Every test file must have a describe block matching the module name.
```

Claude only sees this when it's working on test files. The rest of the time, these instructions don't exist as far as context is concerned.

CLAUDE.md loads every time. Rules load when relevant files are touched. That's the key difference. If an instruction only matters for certain file types, it's a rule, not a CLAUDE.md line.

## Layer 3: Hooks (.claude/settings.json)

Rules are suggestions. Claude reads them, usually follows them, but there's no enforcement mechanism. If you need a guarantee, you need a hook.

Claude Code hooks are defined in `.claude/settings.json` and they run actual code. Not prompts, not instructions. Real scripts that execute before or after Claude uses a tool.

There are two types. A `pre-tool-use` hook runs before Claude takes an action. You can use it to block things entirely. A `post-tool-use` hook runs after the action completes, useful for validation or cleanup.

Here's a real example. Say you want to prevent any file edits when you're on the main branch. You need two pieces: the hook config that tells Claude when to run the check, and the script that does the actual checking.

First, the hook definition in `.claude/settings.json`:

```json
{
  "hooks": {
    "pre-tool-use": [
      {
        "tool": "write|edit",
        "command": "bash .claude/hooks/enforce-worktree.sh"
      }
    ]
  }
}
```

This tells Claude: every time you're about to write or edit a file, run this script first. If the script fails, the action gets blocked.

Now the script itself at `.claude/hooks/enforce-worktree.sh`:

```bash
#!/bin/bash
branch=$(git rev-parse --abbrev-ref HEAD)
if [ "$branch" = "main" ]; then
  echo "Blocked: you're on main. Create a worktree or switch branches first."
  exit 1
fi
```

That's it. Six lines. The script checks which branch you're on. If it's main, it exits with an error and Claude can't write the file. No amount of prompting gets around it. Claude doesn't decide whether to follow this rule. The script runs, it fails, the edit never happens.

You could do the same thing for other scenarios. Guard `.env` files so they never get modified. Run a linter on every file write. Validate that new API routes follow your naming convention. Anything you can check in a shell script, you can enforce as a hook.

Hooks pair especially well with [running Claude on autopilot](/blog/running-claude-on-autopilot) since they give you hard guardrails even when Claude has full permissions. You're letting it move fast, but putting up walls where it matters.

Rules say "please do this." Hooks say "you literally can't do this." That's the difference.

## Layer 4: Commands (.claude/commands/)

Claude Code commands are reusable prompts you trigger manually by typing `/command-name` in the interface. They live in `.claude/commands/` as markdown files.

This is where your repetitive workflows go. Things you do regularly but not every conversation. A `/commit` command that writes conventional commit messages. A `/deploy` command that runs your staging pipeline. A `/review` command that checks the current diff against your team's code standards.

A simple command file looks like this:

```markdown
# /commit
Review the staged changes and write a conventional commit message. Use the format: type(scope): description. Keep the first line under 72 characters.
```

The important distinction from rules: rules fire automatically when file patterns match. Commands fire when you ask for them. They sit in your toolbox, cost zero context tokens until invoked, and run the same way every time.

If you find yourself typing the same multi-line prompt over and over, that's a command waiting to happen.

## Layer 5: Skills (.claude/skills/)

Skills are where things get interesting. A skill is a deep knowledge document, sometimes hundreds of lines, that contains structured workflows, checklists, decision trees, and domain expertise. Too large to live in CLAUDE.md, too specialized to load every conversation.

Skills live in `.claude/skills/` or come bundled with plugins. Claude Code loads them on demand when a task calls for that specific knowledge.

In my setup, I have a skill called nanobanana that handles AI image generation. It contains the full workflow: how to construct prompts, what aspect ratios to use for different contexts, which API to call, where to save the output, and how to optimize the result. That's easily 200+ lines of structured knowledge. If all of that sat in CLAUDE.md, every conversation about fixing a typo would start by loading an image generation manual.

Another example: a jira-manager skill that knows how to create tickets, link them to epics, set priorities, and follow our team's Jira conventions. Loaded when I'm doing project management work. Invisible when I'm writing code.

Commands say "run this prompt." Skills say "become an expert at this domain." A command is a one-shot instruction. A skill is a body of knowledge that changes how Claude approaches an entire category of work.

## Layer 6: Agents (.claude/agents/)

Agents are specialized personas. Each one has its own system prompt, its own behavior rules, and its own focus area. They live in `.claude/agents/` and you can delegate tasks to them.

But here's the part that matters most: agents can consume skills. So when you create a Content Creator agent, it doesn't just have a system prompt that says "write well." It loads writing skills, brand voice guidelines, SEO checklists, and style references. You get a specialist worker with deep domain knowledge running in its own context window.

In my blog workflow, I have a Content Creator agent that handles all writing. It knows my tone, my style rules, my conventions. I have an SEO Specialist agent that reviews posts for search optimization. An Image Prompt Engineer agent that generates prompts for visuals. Each one is focused, each one carries the skills it needs, and none of them pollute the main context with knowledge the others don't care about.

The decision between a skill and an agent comes down to this: skills are knowledge you absorb. You read them, you use them. Agents are workers you delegate to. They operate independently, carry their own context, and come back with results. When the task needs a different perspective or a different set of priorities, that's an agent. When you just need to know more about a topic, that's a skill.

## Layer 7: Plugins and MCP Servers

Everything up to this point customizes how Claude Code behaves. Plugins and MCP servers extend what it can do.

A plugin is a package that bundles skills, agents, hooks, and commands together. Someone builds a plugin for, say, a design system, and you install it. You get the skills, the commands, the agents, all wired up and ready. It's config as a package.

MCP servers go further. They give Claude entirely new capabilities by connecting it to external services. A Figma MCP server lets Claude [pull designs directly from your Figma files](/blog/design-loop-claude-figma). A PostHog server lets it query analytics data. A GitHub server gives it richer access to pull requests and issues beyond what the CLI provides.

The mental model: everything from CLAUDE.md through agents is about shaping Claude's behavior within its existing capabilities. Plugins and MCP servers are about giving it new ones.

## The Context Budget

Every layer in Claude Code's configuration system exists because of one tradeoff: always available versus context cost.

CLAUDE.md loads every conversation. That's powerful but expensive. Rules load conditionally, so they're cheaper. Commands cost nothing until invoked. Skills load on demand. Agents run in their own context window entirely, so they don't eat into yours at all.

Your CLAUDE.md should be a steering wheel, not an encyclopedia. If you're over 50 lines, start asking which of those lines could be a rule, a command, or a skill instead. The goal isn't to cram everything Claude might need into the smallest file possible. The goal is to put each piece of config in the layer where it costs the least while still being available when it matters.

## Wrapping Up

Start with CLAUDE.md. Most projects don't need all seven layers. But when your config file starts getting long and every conversation feels like it's burning tokens on instructions that aren't relevant, you'll know it's time to move things into the layer where they actually belong.

The pattern is always the same. You notice something in CLAUDE.md that only matters sometimes. You move it to a rule, a command, or a skill. Your context gets lighter, Claude gets faster, and the instructions that remain are the ones that actually matter for the task at hand. It's a gradual process, not a weekend project.

If you're starting fresh, write a CLAUDE.md with your top 10 project conventions and stop there. Use it for a week. Pay attention to which instructions feel wasteful in certain conversations. Those are the ones ready to move. The layers will make sense when you feel the problem they solve.
