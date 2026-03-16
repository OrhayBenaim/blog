# Blog Post Design: Running Claude on Autopilot

## Summary

A blog post about running Claude Code with `--dangerously-skip-permissions` safely using devcontainers. Positive framing — focused on the aspiration (full autopilot) and how devcontainers make it safe through isolation.

## Audience

Developers and users who want to run Claude with the `--dangerously-skip-permissions` flag responsibly.

## Tone & Style

- Match existing blog voice: conversational, first-person, honest, practical
- Human-like — no AI feeling
- Direct, no fluff
- Show real configs with annotations
- Honest about limitations

## Post Structure

### 1. Opening Hook
- Title: "Running Claude on Autopilot"
- The aspiration: you want Claude to just do the work without approving every action
- `--dangerously-skip-permissions` gives you that, but the flag name exists for a reason
- This post is about getting the freedom without the risk
- 2-3 paragraphs, same energy as "From Idea to Strategy" opener

### 2. The Problem (short)
- What `--dangerously-skip-permissions` actually does: execute any command, write any file, access network
- On bare metal, Claude has the same access you do
- For trusted repos the risk is low, but there's a smarter way
- One paragraph, honest not fear-mongering

### 3. The Solution — Devcontainers (1 paragraph)
- Brief: a container that IS your dev environment
- Anthropic provides a reference devcontainer specifically for Claude Code
- You don't have to build this yourself
- Keep it short — one paragraph

### 4. The Setup — 4 Steps
- Tool-agnostic (VS Code, JetBrains, CLI `devcontainer up`, Codespaces, etc.)
- Steps: install devcontainer tooling, clone reference repo, open project, reopen in container
- Show the three config files: devcontainer.json, Dockerfile, init-firewall.sh
- Annotated config snippets explaining key parts
- This is the meat of the post

### 5. Isolation is the Point
- Core message: isolation is what makes running the danger flag safe
- Your host machine, credentials, other projects — unreachable from inside the container
- Brief mention of firewall/default-deny as supporting details
- Focus: the container IS the sandbox, that's why this works

### 6. Closing — Get Started
- Short honest take
- Link to Anthropic reference repo and official docs
- 2-3 sentences, no fluff

## Technical Details to Cover

- devcontainer.json: container settings, extensions, volume mounts
- Dockerfile: container image and installed tools
- init-firewall.sh: network security rules
- Firewall whitelist (npm, GitHub, Claude API)
- Default-deny policy
- Startup verification

## Agents to Use During Implementation

- **Content Creator agent**: Draft the blog post text matching existing voice
- **Nanobanana skill**: Generate hero image and concept images for the post
- **SEO Specialist agent**: Optimize title, description, tags, and content for search
- **Image Optimizer skill**: Convert generated images to WebP for the blog

## Tags

["claude-code", "security", "devcontainers", "workflow"]
