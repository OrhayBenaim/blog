# Claude Code Config Guide Blog Post — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Create a blog post that guides readers through Claude Code's layered config system (CLAUDE.md, rules, hooks, commands, skills, agents, plugins) with a "context budget" mental model.

**Architecture:** Single markdown blog post with hero image. Content Creator agent writes the post, Image Prompt Engineer + nanobanana generates the hero, SEO Specialist reviews before merge.

**Tech Stack:** Astro blog (markdown + frontmatter), WebP images in public/blog/

---

### Task 1: Create Worktree

**Step 1: Create feature branch worktree**

Run:
```bash
cd C:/Users/Orhay/git/blog && git worktree add .worktrees/claude-code-config-guide -b claude-code-config-guide
```
Expected: New worktree at `.worktrees/claude-code-config-guide/`

All subsequent file operations happen inside `.worktrees/claude-code-config-guide/`.

---

### Task 2: Write Blog Post Content

**Files:**
- Create: `.worktrees/claude-code-config-guide/src/content/blog/claude-code-config-guide.md`

**Step 1: Use Content Creator agent to write the blog post**

Dispatch the Content Creator agent with the following brief:
- Design doc: `docs/plans/2026-03-17-claude-code-config-guide-design.md`
- Reference post for tone/style: `src/content/blog/running-claude-on-autopilot.md`
- Writing style rules from CLAUDE.md (no em dashes, conversational, human tone)
- Frontmatter format:
```yaml
---
title: "Where Does This Go? A Guide to Claude Code's Config System"
description: "CLAUDE.md, rules, hooks, commands, skills, agents, plugins. What each one does, where it lives, and why keeping your config slim saves you context tokens."
pubDate: 2026-03-17
pubTime: "12:00"
tags: ["claude-code", "workflow", "ai", "configuration", "developer-tools"]
---
```
- Post must follow the layered progression structure from the design doc
- Include comparison points woven throughout (not a single big table)
- Target 1800-2200 words
- Include a placeholder for hero image: `![Hero image alt text](/blog/blog/claude-code-config-guide-hero.webp)`
- Real examples from the author's setup mixed with simplified generic ones
- The agents section must include: agents can consume skills, so you get a specialist worker with deep domain knowledge running in its own context window

**Step 2: Review the output**

Read the generated file and verify:
- Frontmatter is correct
- All 7 layers are covered plus the Context Budget section and Decision Guide
- Tone matches existing posts (no em dashes, no AI fluff words)
- Hero image placeholder is present
- Word count is in range

---

### Task 3: Generate Hero Image

**Files:**
- Create: `.worktrees/claude-code-config-guide/public/blog/claude-code-config-guide-hero.webp`

**Step 1: Use Image Prompt Engineer agent to create a hero image prompt**

Brief for the Image Prompt Engineer:
- Blog post topic: Claude Code's layered config system
- Visual concept: layers/progression from simple to complex, config files, developer workspace
- Style: modern, clean, tech-focused, suitable as a blog hero image
- Aspect ratio: 16:9 landscape (blog hero)
- The image should feel approachable, not intimidating

**Step 2: Use nanobanana skill to generate the image**

Use the prompt from Step 1 to generate the hero image via nanobanana.

**Step 3: Save to correct path**

Save as: `.worktrees/claude-code-config-guide/public/blog/claude-code-config-guide-hero.webp`

If the image is not already WebP, use the image-optimizer skill to convert it.

---

### Task 4: SEO Review

**Step 1: Use SEO Specialist agent to review the post**

Send the complete blog post to the SEO Specialist agent for review:
- Check title tag and meta description
- Check heading structure (H2s for layers, logical progression)
- Check keyword usage (claude code, configuration, hooks, skills, agents, CLAUDE.md)
- Check readability and content structure
- Suggest improvements if needed

**Step 2: Apply SEO feedback**

Edit the blog post to incorporate any SEO improvements. Common fixes:
- Adjust title/description for search intent
- Add or refine heading keywords
- Improve internal linking if other relevant posts exist

---

### Task 5: Commit and Wrap Up

**Step 1: Stage and commit all files**

Run:
```bash
cd C:/Users/Orhay/git/blog/.worktrees/claude-code-config-guide
git add src/content/blog/claude-code-config-guide.md public/blog/claude-code-config-guide-hero.webp
git commit -m "add blog post: Claude Code config system guide"
```

**Step 2: Verify**

Run:
```bash
cd C:/Users/Orhay/git/blog/.worktrees/claude-code-config-guide && git log --oneline -3
```
Expected: Latest commit shows the blog post addition.
