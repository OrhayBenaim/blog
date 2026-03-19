# NemoClaw Blog Post Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Publish a blog post about NVIDIA NemoClaw covering what it is, installation, use cases, and comparison with OpenClaw.

**Architecture:** Single blog post in Astro content collection with hero image. Content Creator agent writes text, Image Prompt Engineer + nanobanana for hero image, SEO Specialist reviews final output.

**Tech Stack:** Astro blog (Markdown), webp images in public/blog/

---

### Task 1: Create Worktree

**Step 1: Create a feature worktree**

Run:
```bash
cd C:/Users/Orhay/git/blog
git worktree add .worktrees/nemoclaw-post -b nemoclaw-post
```

**Step 2: Verify worktree**

Run: `ls .worktrees/nemoclaw-post/src/content/blog/`
Expected: existing blog posts listed

---

### Task 2: Write Blog Post Content

**Files:**
- Create: `.worktrees/nemoclaw-post/src/content/blog/nvidia-nemoclaw-secure-openclaw.md`

**Step 1: Content Creator agent writes the full blog post**

Use the Content Creator agent to write the blog post following the design doc at `docs/plans/2026-03-18-nemoclaw-design.md`.

Frontmatter format:
```markdown
---
title: "<SEO-friendly title about NemoClaw>"
description: "<1-2 sentence description for meta tags>"
pubDate: 2026-03-18
pubTime: "<current time HH:MM>"
tags: ["nemoclaw", "nvidia", "openclaw", "security", "ai-agents"]
---
```

Content structure (from design):
1. **Opening/Hook** - News angle: NVIDIA launched NemoClaw, open-source security for OpenClaw
2. **What is OpenClaw** - 2-3 paragraph primer for newcomers
3. **What is NemoClaw** - Components, OpenShell, four protection layers
4. **Installation** - Local/VM one-liner + cloud one-click, key commands
5. **Use Cases** - List with short descriptions + one practical snippet
6. **NemoClaw vs OpenClaw** - Comparison table
7. **Closing** - Honest take, early preview, what's useful now

Key references for content:
- NVIDIA product page: https://www.nvidia.com/en-us/ai/nemoclaw/
- GitHub repo: https://github.com/NVIDIA/NemoClaw
- One-click cloud deploy: https://brev.nvidia.com/launchable/deploy?launchableID=env-3Azt0aYgVNFEuz7opyx3gscmowS
- Install command: `curl -fsSL https://nvidia.com/nemoclaw.sh | bash`
- Model used: `nvidia/nemotron-3-super-120b-a12b` (NVIDIA Cloud API)
- Sandbox tech: Landlock + seccomp + netns
- Protection layers: Network (hot-reloadable), Filesystem (locked), Process (locked), Inference (hot-reloadable)
- CLI commands: `nemoclaw onboard`, `nemoclaw <name> connect/status/logs`, `openshell term`
- Deploy command: `nemoclaw deploy <instance>` (experimental, via Brev)
- Telegram bridge and tunnel via `nemoclaw start/stop/status`

Writing style rules (from CLAUDE.md):
- Human tone, conversational, no em dashes
- No "delve", "leverage", "utilize", "furthermore", "notably"
- Short punchy sentences mixed with longer ones
- Direct "you" address
- Honest takes, not hype
- Hero image after opening paragraph: `![alt text](/blog/blog/nvidia-nemoclaw-hero.webp)`

**Step 2: Review the output**

Read the generated file and verify:
- Frontmatter is correct
- All 7 sections are present
- Comparison table is properly formatted
- No em dashes or AI filler words
- Links are correct
- Hero image reference is included

**Step 3: Commit**

```bash
cd C:/Users/Orhay/git/blog/.worktrees/nemoclaw-post
git add src/content/blog/nvidia-nemoclaw-secure-openclaw.md
git commit -m "feat: add NemoClaw blog post draft"
```

---

### Task 3: Generate Hero Image

**Files:**
- Create: `.worktrees/nemoclaw-post/public/blog/nvidia-nemoclaw-hero.webp`

**Step 1: Image Prompt Engineer generates a photography prompt**

Use the Image Prompt Engineer agent to create a prompt for the hero image. The image should represent:
- AI agents running in a secure, sandboxed environment
- NVIDIA / green color theme
- Tech/security vibe matching existing blog hero images

**Step 2: Generate image with nanobanana skill**

Use the nanobanana skill to generate the image from the prompt.

**Step 3: Save to correct path**

Save as: `.worktrees/nemoclaw-post/public/blog/nvidia-nemoclaw-hero.webp`

**Step 4: Commit**

```bash
cd C:/Users/Orhay/git/blog/.worktrees/nemoclaw-post
git add public/blog/nvidia-nemoclaw-hero.webp
git commit -m "feat: add NemoClaw blog post hero image"
```

---

### Task 4: SEO Review

**Step 1: SEO Specialist agent reviews the post**

Use the SEO Specialist agent to review:
- Title tag and meta description
- Heading structure (H2/H3 hierarchy)
- Keyword usage (nemoclaw, openclaw, nvidia, ai agents, security)
- Internal linking opportunities to existing posts (e.g., running-claude-on-autopilot, securing-ai-apps)
- Alt text on hero image

**Step 2: Apply SEO recommendations**

Edit `.worktrees/nemoclaw-post/src/content/blog/nvidia-nemoclaw-secure-openclaw.md` with any changes.

**Step 3: Commit**

```bash
cd C:/Users/Orhay/git/blog/.worktrees/nemoclaw-post
git add src/content/blog/nvidia-nemoclaw-secure-openclaw.md
git commit -m "feat: apply SEO optimizations to NemoClaw post"
```

---

### Task 5: Final Review and Merge

**Step 1: Verify the post renders correctly**

Run:
```bash
cd C:/Users/Orhay/git/blog/.worktrees/nemoclaw-post
npm run build
```

Expected: Build succeeds with no errors.

**Step 2: Merge to main**

```bash
cd C:/Users/Orhay/git/blog
git merge nemoclaw-post
git worktree remove .worktrees/nemoclaw-post
git branch -d nemoclaw-post
```
