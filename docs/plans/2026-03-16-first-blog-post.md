# "From Idea to Strategy in Minutes" Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Write and publish the first blog post walking through a real brainstorming-to-TikTok-strategy workflow, using our own agents and skills to create the post itself.

**Architecture:** Dog-food approach. We use the exact workflow we're writing about: brainstorm the TikTok example, hand off to the TikTok Strategist agent, then hand the blog writing to the Content Creator agent, and generate visuals with Nano Banana. Every tool we mention in the post is a tool we used to make it.

**Tech Stack:** Astro (Markdown posts), existing blog infrastructure, Superpowers brainstorming skill, TikTok Strategist agent, Content Creator agent, Nano Banana skill.

---

### Task 1: Run the real TikTok strategy example

**Purpose:** Generate authentic material for the blog post. We need real prompts, real agent responses, and real outputs.

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
- Any sections that would look great as visuals

Save a curated selection to `docs/plans/tiktok-example-curated.md`.

**Step 4: Commit raw materials**

```bash
git add docs/plans/tiktok-example-*.md
git commit -m "docs: capture real TikTok strategy example for blog post"
```

---

### Task 2: Generate visuals with Nano Banana

**Purpose:** Create images for the blog post using the Nano Banana skill instead of relying on screenshots alone.

**Step 1: Generate a hero image for the post**

Use the Nano Banana skill to generate a hero/header image that captures the concept of "idea to strategy." Something visual that represents brainstorming flowing into a concrete plan.

Save to `public/blog/from-idea-to-strategy-hero.png`.

**Step 2: Generate supporting visuals**

Use Nano Banana to create 1-2 additional images:
- A visual representing the "two layers" concept (brainstorming + specialist)
- A visual that fits alongside the TikTok strategy section (fitness/social media themed)

Save to `public/blog/` with descriptive names.

**Step 3: Commit images**

```bash
git add public/blog/
git commit -m "feat: generate blog post images with Nano Banana"
```

---

### Task 3: Write the blog post using Content Creator agent

**Purpose:** Use the Content Creator agent to draft the blog post, feeding it the curated TikTok example material and the design doc.

**Files:**
- Create: `src/content/blog/from-idea-to-strategy-in-minutes.md`

**Step 1: Invoke the Content Creator agent with full context**

Provide the Content Creator agent with:
- The design doc (`docs/plans/2026-03-16-first-blog-post-design.md`)
- The curated TikTok example (`docs/plans/tiktok-example-curated.md`)
- The generated images (paths from Task 2)
- The writing rules below

Prompt the Content Creator agent to write the full blog post following this structure:

**Frontmatter:**
```markdown
---
title: "From Idea to Strategy in Minutes"
description: "How I use AI agents to brainstorm ideas and hand them off to specialists. A real walkthrough of going from a vague idea to a full TikTok strategy."
pubDate: 2026-03-16
tags: ["ai", "workflow", "claude-code", "agents"]
---
```

**Section 1 - Opening (2-3 paragraphs):**
First person, casual. Set up the concept: you talk to one AI to refine your idea, then it hands the work to a specialist. Mention this is the first post in a series.

**Section 2 - The Setup (3-4 paragraphs):**
Explain the two layers:
1. Brainstorming layer (Superpowers skill)
2. Specialist layer (agents like TikTok Strategist)

Include install command: `claude plugin add superpowers`
Link to source: [Superpowers on Claude Code Marketplace](https://marketplace.claudecode.dev/plugins/superpowers)

**Section 3 - The Walkthrough (main content):**
Use the curated material. Structure:
1. Show the initial prompt (as a blockquote)
2. Show 2-3 brainstorming exchanges (as blockquotes with "**Claude:**" and "**Me:**" labels)
3. Show the handoff moment
4. Show the TikTok Strategist output (best parts, formatted cleanly)
5. Short honest reaction paragraph

Include the generated images from Task 2 at appropriate points.

**Section 4 - Series Teaser & Closing (2-3 paragraphs):**
List upcoming posts:
- Building a landing page from a Figma design
- Generating images and videos with AI (Nano Banana)
- Writing a full content strategy across platforms
- Optimizing an app store listing

End with install commands and links for all tools mentioned.

**Writing rules (STRICT - the Content Creator agent must follow these):**
- No em dashes (use commas, periods, or "and" instead)
- No AI-sounding phrases: "revolutionary", "game-changer", "leverage", "delve", "streamline", "harness", "cutting-edge", "elevate", "empower", "seamless"
- First person throughout
- Short paragraphs (2-3 sentences max)
- Conversational, like explaining to a friend
- As human as possible

**Step 2: Save the Content Creator's output**

Save to `src/content/blog/from-idea-to-strategy-in-minutes.md`.

**Step 3: Commit the blog post**

```bash
git add src/content/blog/from-idea-to-strategy-in-minutes.md
git commit -m "feat: add first blog post - From Idea to Strategy in Minutes"
```

---

### Task 4: Review and polish

**Step 1: Read the full post end to end**

Check for:
- Em dashes (replace all)
- AI-sounding phrases (replace all)
- Tone consistency (casual throughout, sounds human not AI-generated)
- Flow between sections
- All tools/skills/agents have install commands or download links
- Images are referenced correctly and exist in `public/blog/`
- Reading time is in the 5-7 minute range

**Step 2: Verify the post renders correctly**

Run: `npx astro dev`

Visit the post URL and check:
- Title and metadata display correctly
- Code blocks render properly
- Images load and display at proper sizes
- Tags work and link to tag pages
- Reading time shows up

**Step 3: Fix any issues found**

Apply fixes to `src/content/blog/from-idea-to-strategy-in-minutes.md`.

**Step 4: Final commit**

```bash
git add src/content/blog/from-idea-to-strategy-in-minutes.md
git commit -m "fix: polish first blog post - tone, formatting, links"
```
