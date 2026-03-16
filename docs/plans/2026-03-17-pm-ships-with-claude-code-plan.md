# "How a Product Manager Ships with Claude Code" Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Write and publish a blog post showing product managers how to use Claude Code for PM workflows (spec writing, stakeholder videos, Jira tickets).

**Architecture:** Single markdown blog post with three assets (hero image, video embed, Jira screenshot placeholder). Follows the same voice, structure, and frontmatter conventions as existing posts.

**Tech Stack:** Astro content collections, Markdown, NanoBanana for image generation, image-optimizer skill for WebP conversion.

**Reference post for voice/structure:** `src/content/blog/from-idea-to-strategy-in-minutes.md`

---

### Task 1: Generate Hero Image

**Files:**
- Create: `public/blog/pm-ships-hero.webp`

**Step 1: Generate the image with NanoBanana**

Use the `nanobanana` skill to generate an image with this prompt:

> A product manager's modern workspace viewed from above at a slight angle. A laptop sits center-frame with a glowing terminal/chat interface on screen. Flowing outward from the laptop in a gentle arc are three artifacts: a clean spec document with visible text blocks and diagrams, a video player thumbnail showing a presentation slide, and a Jira-style kanban board with colored tickets. The artifacts appear to float slightly above the desk surface with soft shadows. Warm, natural lighting from a window on the left. Muted teal and sandy brown color palette. Photorealistic, editorial style, shallow depth of field on the edges. No text visible on screen or documents.

**Step 2: Optimize the image**

Use the `image-optimizer` skill to convert the generated image to WebP format at `public/blog/pm-ships-hero.webp`.

**Step 3: Commit**

```bash
git add public/blog/pm-ships-hero.webp
git commit -m "add hero image for PM blog post"
```

---

### Task 2: Copy Video Asset

**Files:**
- Source: `docs/pm/pubtime-feature.mp4`
- Create: `public/blog/pm-ships-pubtime-feature.mp4`

**Step 1: Copy the video to the public blog assets directory**

```bash
cp docs/pm/pubtime-feature.mp4 public/blog/pm-ships-pubtime-feature.mp4
```

**Step 2: Commit**

```bash
git add public/blog/pm-ships-pubtime-feature.mp4
git commit -m "add stakeholder video asset for PM blog post"
```

---

### Task 3: Write the Blog Post

**Files:**
- Create: `src/content/blog/pm-ships-with-claude-code.md`

**Writing guidelines (from memory + existing posts):**
- Conversational, direct address ("I", "you")
- Problem-first hook
- No em dashes (use periods, commas, or "and" instead)
- No staccato AI patterns (avoid short choppy sentences in sequence)
- Use blockquotes (`>`) for prompt/response exchanges
- Bold the speaker name in exchanges: `> **Me:**` and `> **Claude:**`
- Tables for structured data
- End with "Get Started" section with install commands and links

**Step 1: Create the blog post file**

Create `src/content/blog/pm-ships-with-claude-code.md` with the following structure and content:

```markdown
---
title: "How a Product Manager Ships with Claude Code"
description: "From a vague idea to a full spec, stakeholder video, and Jira tickets. A real walkthrough of PM workflows powered by AI agents."
pubDate: 2026-03-16
pubTime: "18:00"
tags: ["ai", "workflow", "claude-code", "agents", "product-management"]
---

[SECTION 1: Hook - 2-3 paragraphs]

Open with: Most people think of Claude Code as a developer tool. Engineers use it
to write code, debug, refactor. That framing misses something important. The core
workflow that makes Claude Code powerful is not about code at all. It is the loop:
think through what you need, hand it to a specialist, get back real deliverables.
That loop works for anyone who builds products.

Pivot to: I am a product manager. My days are filled with writing specs, getting
stakeholder buy-in, and creating Jira tickets. The kind of work that is important
but repetitive. I wanted to see what happens when you point Claude Code at PM
workflows instead of engineering ones.

Set up: Here is what happened when I took a small feature idea and let Claude Code
run the full PM cycle: brainstorming, spec writing, stakeholder video, and ticket
creation.

![A product manager's workspace with a spec, video, and Jira board flowing from a laptop](/blog/blog/pm-ships-hero.webp)

[SECTION 2: The Idea - 2 paragraphs]

Context: I run a blog built with Astro. Four posts, all published on the same date.
The sort order on the homepage was random because every post shared the same
timestamp. I needed a small feature: add a time field to each post so they sort
in a predictable order. Not a big project. But it still needed a proper spec that
an engineer could pick up, stakeholder alignment on why we are doing it, and Jira
tickets to track the work. That is easily an afternoon of PM busywork.

[SECTION 3: Brainstorming - show 1-2 exchanges]

Heading: ## Brainstorming: Figuring Out What We Need

Introduce the brainstorming layer (Superpowers plugin). Show how it asks clarifying
questions one at a time rather than dumping a solution.

Show 1-2 prompt/response exchanges where Claude asks about:
- Whether this should be a schema change or a different approach
- Backward compatibility concerns (existing posts without the field)

End with the plan Claude produced: three deliverables (spec, stakeholder video,
Jira tickets) with the right tools assigned to each.

Include the plan summary in a blockquote:
> Step 1: Use the Senior PM agent to write a full feature spec
> Step 2: Use Remotion to generate a stakeholder video explaining the feature
> Step 3: Use the Jira Manager to create development tickets from the spec

[SECTION 4: The Handoff]

Heading: ## "Execute this plan."

One sentence prompt from the user. Then a short paragraph explaining the moment:
that single sentence is where you stop thinking and the agent starts doing. Everything
from here forward happened without further input. The brainstorming layer dispatched
the Senior PM agent, which handled the rest autonomously.

This section should be short and punchy. The brevity IS the point.

[SECTION 5: What Came Back - outcomes only, no prompts]

Heading: ## What Came Back

### The Spec

Describe what the Senior PM agent produced: a full feature spec with context,
technical approach, development tasks, acceptance criteria, and edge cases. Not a
rough outline but a document an engineer could pick up and start building from.

Quote 2-3 lines from the actual spec (docs/pm/tasks/add-time-field-for-sorting.md):

> **Original requirement**: Blog posts should support a time field (in addition
> to the existing date) that is used only for sorting, not displayed in the UI.

And from the edge cases table:

> | Post without pubTime | Treated as 00:00 UTC, sorts last within its day |
> | Post with invalid time like "2pm" | Zod regex rejects at build time |

Note the level of detail: backward compatibility table, exact file paths,
acceptance criteria per task. This is spec quality that usually takes an hour
or more of focused PM work.

### The Stakeholder Video

The agent did not stop at the spec. It used Remotion to generate a short video
explaining the feature and why it matters. The kind of artifact you would normally
spend time creating in Loom or a slide deck before bringing a feature to a
stakeholder review.

Embed the video:
<video src="/blog/blog/pm-ships-pubtime-feature.mp4" autoplay loop muted playsinline style="max-width: 100%; margin: 0 auto; display: block; border-radius: 12px;"></video>

### The Jira Tickets

With the spec written and approved, the agent used the Jira Manager skill to create
development tickets directly from the spec. Each task from the spec became a ticket
with the right description, acceptance criteria, and priority.

[INSERT JIRA SCREENSHOT: ![Jira tickets created from the spec](/blog/blog/pm-ships-jira-tickets.webp)]

No copy-pasting between tools. No reformatting acceptance criteria into ticket
descriptions. The spec was the source of truth and the tickets were derived from it.

[SECTION 6: My Honest Take - 2 paragraphs]

Heading: ## My Honest Take

What surprised me: the spec quality. The edge cases table, the backward compatibility
analysis, the file-by-file change summary. That is the kind of thoroughness that
takes real effort to produce manually, and it came out of a single agent run.

What still needs a human: the brainstorming layer is where your judgment matters most.
The questions it asks are good, but you need to bring real product context. "Should
this be backward compatible?" is the right question, but only you know whether your
users would tolerate a breaking change. The agent executes well once it has clear
direction, but that direction has to come from someone who understands the product.

[SECTION 7: Get Started]

Heading: ## Get Started

If you want to try this workflow yourself, here is what you need:

**Superpowers** (the brainstorming layer):
```bash
claude plugin add superpowers
```
<a href="https://marketplace.claudecode.dev/plugins/superpowers" target="_blank" rel="noopener noreferrer">Superpowers on Claude Code Marketplace</a>

**Senior Project Manager agent** (based on the Agency Agents collection, modified for this workflow):

The original comes from <a href="https://github.com/msitarzewski/agency-agents" target="_blank" rel="noopener noreferrer">Agency Agents</a>, a collection of specialist agents for marketing, project management, and more. I modified it for my specific PM needs. You can grab my version here:

<a href="https://github.com/OrhayBenaim/blog/blob/main/.claude/agents/project-manager-senior.md" target="_blank" rel="noopener noreferrer">Senior PM Agent on GitHub</a>

**Remotion skill** (video generation):

<a href="https://www.remotion.dev/docs/ai/skills" target="_blank" rel="noopener noreferrer">Remotion AI Skills</a>

**Jira Manager skill** (ticket creation from specs):

<a href="https://github.com/OrhayBenaim/blog/tree/main/.claude/skills/jira-manager" target="_blank" rel="noopener noreferrer">Jira Manager on GitHub</a>

The brainstorming layer handles the orchestration. You bring the product context,
it figures out which tools to use and in what order.
```

**Step 2: Review the post content against the design doc**

Verify:
- [ ] Frontmatter matches design doc (title, description, pubDate, pubTime, tags)
- [ ] Hero image path is correct: `/blog/blog/pm-ships-hero.webp`
- [ ] Video embed path is correct: `/blog/blog/pm-ships-pubtime-feature.mp4`
- [ ] Jira screenshot placeholder is present (user will add the actual image later)
- [ ] No em dashes anywhere in the post
- [ ] All 4 Get Started links are present and correct
- [ ] "My Honest Take" section is included
- [ ] Blockquote exchanges use `> **Me:**` and `> **Claude:**` format
- [ ] Voice matches existing posts (conversational, first person, problem-first)

**Step 3: Commit**

```bash
git add src/content/blog/pm-ships-with-claude-code.md
git commit -m "add blog post: How a Product Manager Ships with Claude Code"
```

---

### Task 4: Verify Build

**Step 1: Run the Astro build**

```bash
npm run build
```

Expected: Build succeeds with no errors. The new post appears in the output.

**Step 2: Run the dev server and verify**

```bash
npm run dev
```

Check:
- [ ] New post appears on the homepage
- [ ] Post sorts above all other posts (pubTime "18:00" is latest)
- [ ] Hero image renders
- [ ] Video plays
- [ ] Jira screenshot placeholder is visible (or gracefully missing if not yet added)
- [ ] Tags page shows "product-management" tag with this post
- [ ] RSS feed includes the new post

**Step 3: Commit any fixes if needed**

---

### Task 5: Add Jira Screenshot (User Action Required)

**Files:**
- Create: `public/blog/pm-ships-jira-tickets.webp`

This task is blocked on the user providing the Jira screenshot. Once provided:

**Step 1: Optimize the screenshot**

Use the `image-optimizer` skill to convert to WebP at `public/blog/pm-ships-jira-tickets.webp`.

**Step 2: Verify the image renders in the post**

Run dev server and check the "Jira Tickets" section.

**Step 3: Commit**

```bash
git add public/blog/pm-ships-jira-tickets.webp
git commit -m "add Jira tickets screenshot for PM blog post"
```
