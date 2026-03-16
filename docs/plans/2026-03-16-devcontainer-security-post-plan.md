# Running Claude on Autopilot — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Publish a blog post about running Claude Code with `--dangerously-skip-permissions` safely using devcontainers.

**Architecture:** Astro 6 blog with markdown content in `src/content/blog/`, images in `public/blog/`. Posts use frontmatter (title, description, pubDate, tags). Multiple agents run in parallel for content, images, and SEO.

**Tech Stack:** Astro 6, Markdown, Nanobanana (image generation), Sharp (image optimization)

---

### Task 1: Fetch Reference Devcontainer Configs

**Purpose:** Get the actual devcontainer.json, Dockerfile, and init-firewall.sh from Anthropic's repo so we can include accurate, annotated snippets in the post.

**Files:**
- None created — research only

**Step 1: Fetch the three config files from GitHub**

Use the context-mode fetch tool to index:
- `https://raw.githubusercontent.com/anthropics/claude-code/main/.devcontainer/devcontainer.json`
- `https://raw.githubusercontent.com/anthropics/claude-code/main/.devcontainer/Dockerfile`
- `https://raw.githubusercontent.com/anthropics/claude-code/main/.devcontainer/init-firewall.sh`

**Step 2: Extract key snippets**

Search the indexed content for:
- Firewall whitelist domains
- Default-deny iptables rules
- Container isolation settings
- Volume mounts and security-relevant config

Save findings as notes for Task 3.

---

### Task 2: Generate Hero Image

**Purpose:** Create a hero image for the blog post using Nanobanana.

**Files:**
- Create: `public/blog/running-claude-on-autopilot-hero.png` (generated)
- Create: `public/blog/running-claude-on-autopilot-hero.webp` (optimized)

**Step 1: Generate image with Nanobanana skill**

Invoke the `nanobanana` skill to generate an image. Prompt concept: a secure container/sandbox visual — something that evokes "freedom within safety." Think a workspace inside a protective bubble or container, clean and modern aesthetic. Should match the blog's Coastal Sunset color palette (charcoal blue #264653, verdigris #2a9d8f, burnt peach #e76f51).

Save to `public/blog/running-claude-on-autopilot-hero.png`.

**Step 2: Optimize image with Image Optimizer skill**

Invoke the `image-optimizer` skill to convert the PNG to WebP format.

Output: `public/blog/running-claude-on-autopilot-hero.webp`

---

### Task 3: Draft Blog Post Content

**Purpose:** Write the full blog post markdown, matching the existing blog voice exactly.

**Files:**
- Create: `src/content/blog/running-claude-on-autopilot.md`

**Step 1: Draft with Content Creator agent**

Launch a **Content Creator** agent with the following brief:

**Voice reference:** Read `src/content/blog/from-idea-to-strategy-in-minutes.md` for exact tone. Key traits:
- First person, conversational, direct
- Opens with a relatable problem/aspiration
- Short paragraphs, no filler
- Honest about limitations ("Is it perfect? No...")
- Code blocks with brief annotations
- Human-like — zero AI feeling (no "In today's world...", no "Let's dive in...", no "In conclusion...")

**Structure (from design doc):**

1. **Opening Hook (2-3 paragraphs):** You want Claude to just do the work. `--dangerously-skip-permissions` gives you that. But the name exists for a reason. This post: getting the freedom without the risk.

2. **The Problem (1 paragraph):** What the flag actually does — execute any command, write any file, access network. On bare metal, Claude has the same access you do. Not fear-mongering, just honest.

3. **The Solution (1 paragraph):** A devcontainer IS your dev environment. Anthropic provides a reference one for Claude Code. You don't build this yourself.

4. **The Setup (the meat):** Tool-agnostic (VS Code, JetBrains, CLI, Codespaces). Four steps: install tooling, clone reference repo, open project, reopen in container. Show the three config files (devcontainer.json, Dockerfile, init-firewall.sh) with annotated snippets from Task 1 research. Explain the key parts.

5. **Isolation is the Point (2-3 paragraphs):** The container IS the sandbox. Host machine, credentials, other projects — unreachable. Firewall/default-deny as supporting details. Core message: isolation makes the danger flag safe.

6. **Get Started (2-3 sentences):** Honest take. Link to Anthropic reference repo and official docs.

**Frontmatter:**
```yaml
---
title: "Running Claude on Autopilot"
description: "[SEO-optimized — will be updated in Task 4]"
pubDate: 2026-03-16
tags: ["claude-code", "security", "devcontainers", "workflow"]
---
```

**Image references in post:**
- Hero: `![description](/blog/running-claude-on-autopilot-hero.webp)`

**Step 2: Review draft**

Read the output. Check:
- Does it sound like the existing post? No AI cliches?
- Are config snippets accurate (from Task 1)?
- Is the structure right?
- Fix anything that feels off.

**Step 3: Write the file**

Save final content to `src/content/blog/running-claude-on-autopilot.md`.

---

### Task 4: SEO Optimization

**Purpose:** Optimize the post for search discovery.

**Files:**
- Modify: `src/content/blog/running-claude-on-autopilot.md` (description, headings, content tweaks)

**Step 1: Run SEO Specialist agent**

Launch an **SEO Specialist** agent. Give it:
- The full blog post content from Task 3
- Target keywords: "claude code devcontainer", "claude dangerously-skip-permissions", "run claude securely", "claude code autopilot"
- Ask for: optimized meta description, heading improvements, keyword placement suggestions, any content tweaks

**Step 2: Apply SEO recommendations**

Update the post's `description` frontmatter field and apply any heading/content tweaks that don't compromise the human voice.

---

### Task 5: Final Assembly and Commit

**Purpose:** Verify everything is in place and commit.

**Files:**
- Verify: `src/content/blog/running-claude-on-autopilot.md`
- Verify: `public/blog/running-claude-on-autopilot-hero.webp`

**Step 1: Verify all files exist**

```bash
ls -la src/content/blog/running-claude-on-autopilot.md
ls -la public/blog/running-claude-on-autopilot-hero.webp
```

**Step 2: Build and verify**

```bash
npm run build
```

Expected: Clean build, no errors.

**Step 3: Commit**

```bash
git add src/content/blog/running-claude-on-autopilot.md public/blog/running-claude-on-autopilot-hero.webp
git commit -m "feat: add blog post - Running Claude on Autopilot"
```

---

## Parallelization Strategy

```
Task 1 (fetch configs) ──┐
                          ├──> Task 3 (draft content) ──> Task 4 (SEO) ──> Task 5 (commit)
Task 2 (generate image) ─┘
```

- **Tasks 1 & 2 run in parallel** — no dependencies between them
- **Task 3 depends on Task 1** — needs config snippets for accurate content
- **Task 4 depends on Task 3** — needs the draft to optimize
- **Task 5 depends on Tasks 2, 3, 4** — final assembly
