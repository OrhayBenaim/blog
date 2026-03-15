# "From Idea to Strategy in Minutes" Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Write and publish the first blog post walking through a real brainstorming-to-TikTok-strategy workflow.

**Architecture:** Content-first approach. Run the real TikTok strategy example first to capture authentic prompts and outputs. Then write the blog post around that real material. Finally, add images/screenshots and verify everything renders correctly.

**Tech Stack:** Astro (Markdown posts), existing blog infrastructure, TikTok Strategist agent, Superpowers brainstorming skill.

---

### Task 1: Run the real TikTok strategy example

**Purpose:** Generate authentic material for the blog post. We need real prompts, real agent responses, and real outputs to screenshot.

**Step 1: Start a brainstorming session for a fictional fitness brand's TikTok presence**

Use the Superpowers brainstorming skill with a prompt like:
```
I need a TikTok content strategy for "PulseForm" -- a fitness brand targeting 18-28 year olds.
They sell resistance bands and home workout programs. Their voice is motivating but not preachy.
```

Capture the back-and-forth (2-3 exchanges). Save the raw conversation to `docs/plans/tiktok-example-brainstorm.md`.

**Step 2: Hand off to TikTok Strategist agent**

Once brainstorming produces a clear direction, invoke the TikTok Strategist agent:
```
Use the TikTok Strategist agent to create a full TikTok content strategy for PulseForm based on the brainstorming output.
```

Save the full agent output to `docs/plans/tiktok-example-output.md`.

**Step 3: Review and pick the best bits**

Read through both files. Pick:
- 2-3 brainstorming exchanges that show the narrowing-down process
- The most interesting parts of the TikTok strategy output (content ideas, hooks, posting schedule)
- Any sections that would look great as screenshots or visuals

Save a curated selection to `docs/plans/tiktok-example-curated.md`.

**Step 4: Commit raw materials**

```bash
git add docs/plans/tiktok-example-*.md
git commit -m "docs: capture real TikTok strategy example for blog post"
```

---

### Task 2: Write the blog post

**Files:**
- Create: `src/content/blog/from-idea-to-strategy-in-minutes.md`

**Step 1: Write the frontmatter and Section 1 (Opening)**

```markdown
---
title: "From Idea to Strategy in Minutes"
description: "How I use AI agents to brainstorm ideas and hand them off to specialists. A real walkthrough of going from a vague idea to a full TikTok strategy."
pubDate: 2026-03-16
tags: ["ai", "workflow", "claude-code", "agents"]
---
```

Write the opening (2-3 paragraphs). First person, casual. Set up the two-layer concept without explaining it yet. Mention this is the first post in a series.

**Writing rules (apply to ALL sections):**
- No em dashes (use commas, periods, or "and" instead)
- No AI-sounding phrases: "revolutionary", "game-changer", "leverage", "delve", "streamline", "harness", "cutting-edge"
- First person throughout
- Short paragraphs (2-3 sentences max)
- Conversational, like explaining to a friend

**Step 2: Write Section 2 (The Setup)**

Explain the two layers:
1. Brainstorming layer (Superpowers skill)
2. Specialist layer (agents like TikTok Strategist)

Include install command:
```
claude plugin add superpowers
```

Link to source repository. Keep it to 3-4 short paragraphs.

**Step 3: Write Section 3 (The Walkthrough)**

This is the main content. Use the curated material from Task 1.

Structure:
1. Show the initial prompt (as a code block or blockquote)
2. Show 2-3 brainstorming exchanges (as blockquotes with labels like "**Claude:**" and "**Me:**")
3. Show the handoff moment
4. Show the TikTok Strategist output (the best parts, formatted cleanly)
5. Write a short honest reaction paragraph

Mark places where images/screenshots will go with placeholder comments:
```markdown
<!-- screenshot: brainstorming conversation -->
<!-- screenshot: tiktok strategy output -->
```

**Step 4: Write Section 4 (Series Teaser & Closing)**

Zoom out. List upcoming posts:
- Building a landing page from a Figma design
- Generating images and videos with AI (Nano Banana)
- Writing a full content strategy across platforms
- Optimizing an app store listing

End with install commands and links:
- `claude plugin add superpowers` - [Superpowers on GitHub](https://github.com/anthropics/claude-plugins-official)
- TikTok Strategist agent - include download/install instructions
- Brief mention of where to find other agents

**Step 5: Commit the blog post**

```bash
git add src/content/blog/from-idea-to-strategy-in-minutes.md
git commit -m "feat: add first blog post - From Idea to Strategy in Minutes"
```

---

### Task 3: Review and polish

**Step 1: Read the full post end to end**

Check for:
- Em dashes (replace all)
- AI-sounding phrases (replace all)
- Tone consistency (casual throughout)
- Flow between sections
- All tools/skills/agents have install commands or download links
- Reading time is in the 5-7 minute range

**Step 2: Verify the post renders correctly**

Run: `npx astro dev`

Visit the post URL and check:
- Title and metadata display correctly
- Code blocks render properly
- Tags work and link to tag pages
- Reading time shows up
- Image placeholders are clearly marked for future replacement

**Step 3: Fix any issues found**

Apply fixes to `src/content/blog/from-idea-to-strategy-in-minutes.md`.

**Step 4: Final commit**

```bash
git add src/content/blog/from-idea-to-strategy-in-minutes.md
git commit -m "fix: polish first blog post - tone, formatting, links"
```

---

### Task 4: Add images and screenshots (requires user input)

**Note:** This task requires the user to provide or approve screenshots/images from their actual workflow.

**Step 1: Identify all image placeholder locations in the post**

Search for `<!-- screenshot:` comments in the post.

**Step 2: Work with user to capture or create images**

Options:
- Screenshots of actual Claude Code conversations
- Screenshots of agent output
- Generated images using Nano Banana if appropriate for mockups

**Step 3: Add images to the post**

Place images in `public/blog/` directory. Update markdown to reference them:
```markdown
![Brainstorming conversation](/blog/brainstorm-screenshot.png)
```

**Step 4: Final commit with images**

```bash
git add public/blog/ src/content/blog/from-idea-to-strategy-in-minutes.md
git commit -m "feat: add screenshots to first blog post"
```
