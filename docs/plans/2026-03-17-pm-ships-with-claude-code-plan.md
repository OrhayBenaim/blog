# "How a Product Manager Ships with Claude Code" Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Write and publish a blog post showing product managers how to use Claude Code for PM workflows (spec writing, stakeholder videos, Jira tickets).

**Architecture:** Single markdown blog post with three assets (hero image, video embed, Jira screenshot placeholder). Uses specialist agents: Image Prompt Engineer for the hero image prompt, Content Creator for the post text, SEO Specialist for optimization. All content must read as human-written with zero AI patterns.

**Tech Stack:** Astro content collections, Markdown, NanoBanana for image generation, image-optimizer skill for WebP conversion.

**Reference post for voice/structure:** `src/content/blog/from-idea-to-strategy-in-minutes.md`

**Specialist Agents Used:**
- **Image Prompt Engineer** — crafts the hero image prompt for NanoBanana
- **Content Creator** — writes the blog post content
- **SEO Specialist** — reviews and optimizes for search

---

### Task 1: Generate Hero Image

**Files:**
- Create: `public/blog/pm-ships-hero.webp`

**Step 1: Craft the image prompt with Image Prompt Engineer agent**

Launch the `Image Prompt Engineer` agent (subagent_type: "Image Prompt Engineer") with this brief:

> Create a detailed photography prompt for AI image generation. The image is a hero/opener for a blog post titled "How a Product Manager Ships with Claude Code." The concept: a PM's workspace viewed from above at a slight angle, with a laptop center-frame showing a terminal/chat interface. Flowing outward from the laptop are three artifacts: a spec document, a video player thumbnail, and a Jira-style kanban board. Warm natural lighting, muted teal and sandy brown palette (matching the blog's Coastal Sunset theme: charcoal-blue #264653, verdigris #2a9d8f, jasmine #e9c46a, sandy-brown #f4a261). Photorealistic editorial style. No visible text on screen or documents.

Use the prompt the agent returns for the next step.

**Step 2: Generate the image with NanoBanana**

Use the `nanobanana` skill with the prompt from Step 1.

**Step 3: Optimize the image**

Use the `image-optimizer` skill to convert the generated image to WebP format at `public/blog/pm-ships-hero.webp`.

**Step 4: Commit**

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

### Task 3: Write the Blog Post with Content Creator Agent

**Files:**
- Create: `src/content/blog/pm-ships-with-claude-code.md`

**Step 1: Launch the Content Creator agent to write the post**

Launch the `Content Creator` agent with the full brief below. The agent writes the complete markdown file and saves it to `src/content/blog/pm-ships-with-claude-code.md`.

**Brief for Content Creator agent:**

> Write a blog post in markdown. Save it to `src/content/blog/pm-ships-with-claude-code.md`.
>
> **CRITICAL WRITING RULES:**
> - Write like a human. Zero AI feeling. This must read like a real person wrote it on their blog.
> - NEVER use em dashes (—). Use periods, commas, "and", or restructure the sentence.
> - No staccato AI patterns (avoid sequences of short choppy sentences).
> - Vary sentence length naturally. Mix short punchy lines with longer flowing ones.
> - Use contractions ("I've", "don't", "it's") naturally.
> - First person, conversational, direct.
> - No filler words like "delve", "leverage", "utilize", "streamline", "robust".
> - No hedging phrases like "it's worth noting", "it's important to mention".
>
> **Reference for voice:** Read `src/content/blog/from-idea-to-strategy-in-minutes.md` for the exact tone and style to match. That post follows the same brainstorm-to-execution arc.
>
> **Frontmatter (use exactly):**
> ```yaml
> ---
> title: "How a Product Manager Ships with Claude Code"
> description: "From a vague idea to a full spec, stakeholder video, and Jira tickets. A real walkthrough of PM workflows powered by AI agents."
> pubDate: 2026-03-16
> pubTime: "18:00"
> tags: ["ai", "workflow", "claude-code", "agents", "product-management"]
> ---
> ```
>
> **Structure and content direction:**
>
> **Section 1: Hook (2-3 paragraphs)**
> Open with the misconception that Claude Code is a developer tool. Pivot: the workflow that makes it powerful isn't writing code. It's the loop of thinking through what you need, handing it to a specialist, getting back real deliverables. That loop works for anyone who builds products. Set up that you're walking through a real PM workflow.
>
> **Section 2: Hero Image**
> Right after the hook, insert:
> ```
> ![A product manager's workspace with a spec, video, and Jira board flowing from a laptop](/blog/blog/pm-ships-hero.webp)
> ```
>
> **Section 3: "The Idea" (heading: ## The Idea, ~2 paragraphs)**
> Context: you run a blog built with Astro. Four posts, all published on the same date. The sort order on the homepage was random because every post shared the same timestamp. You needed a small feature: add a time field to each post so they sort in a predictable order. Not a big project. But it still needed a proper spec that an engineer could pick up, stakeholder alignment on why you're doing it, and Jira tickets to track the work. The kind of thing that eats a PM's afternoon.
>
> **Section 4: "Brainstorming: Figuring Out What We Need" (heading: ## Brainstorming: Figuring Out What We Need)**
> Introduce the brainstorming layer (Superpowers plugin for Claude Code). It asks clarifying questions one at a time rather than dumping a solution.
>
> Show 1-2 prompt/response exchanges using blockquote format:
> ```
> > **Me:** [prompt text]
>
> > **Claude:** [response text]
> ```
>
> The exchanges should cover:
> - Whether this should be a schema change or a different approach
> - Backward compatibility concerns (existing posts don't have the field)
>
> End with the plan the brainstorming layer produced. Show it as a blockquote:
> ```
> > **Step 1:** Use the Senior PM agent to write a full feature spec
> > **Step 2:** Use Remotion to generate a stakeholder video explaining the feature
> > **Step 3:** Use the Jira Manager to create development tickets from the spec
> ```
>
> **Section 5: The Handoff (heading: ## "Execute this plan.")**
> Show one sentence from the user: "Execute this plan." Then a short paragraph explaining what just happened. That single sentence is where you stop thinking and the agent starts doing. Everything from here forward happened without further input. The brainstorming layer dispatched the Senior PM agent, which handled the rest autonomously.
> This section should be SHORT. The brevity IS the point.
>
> **Section 6: What Came Back (heading: ## What Came Back)**
> No more prompt/response exchanges. Just outcomes.
>
> **Subheading: ### The Spec**
> Describe what the Senior PM agent produced: a full feature spec with context, technical approach, development tasks, acceptance criteria, and edge cases. Not a rough outline. A document an engineer could pick up and start building from.
> Quote from the actual spec at `docs/pm/tasks/add-time-field-for-sorting.md`:
> ```
> > **Original requirement**: Blog posts should support a time field (in addition to the existing date) that is used only for sorting, not displayed in the UI.
> ```
> And from the edge cases table:
> ```
> > | Post without pubTime | Treated as 00:00 UTC, sorts last within its day |
> > | Post with invalid time like "2pm" | Zod regex rejects at build time |
> ```
> Note the level of detail: backward compatibility table, exact file paths, acceptance criteria per task.
>
> **Subheading: ### The Stakeholder Video**
> The agent used Remotion to generate a short video explaining the feature and why it matters. The kind of artifact you'd normally spend time creating in Loom or a slide deck before a stakeholder review.
> Embed:
> ```html
> <video src="/blog/blog/pm-ships-pubtime-feature.mp4" autoplay loop muted playsinline style="max-width: 100%; margin: 0 auto; display: block; border-radius: 12px;"></video>
> ```
>
> **Subheading: ### The Jira Tickets**
> The agent used the Jira Manager skill to create development tickets directly from the spec. Each task became a ticket with the right description, acceptance criteria, and priority. No copy-pasting between tools.
> Insert image placeholder:
> ```
> ![Jira tickets created from the spec](/blog/blog/pm-ships-jira-tickets.webp)
> ```
>
> **Section 7: My Honest Take (heading: ## My Honest Take, ~2 paragraphs)**
> What surprised you: the spec quality. Edge cases table, backward compatibility analysis, file-by-file change summary. That thoroughness takes real effort to produce manually.
> What still needs a human: the brainstorming layer is where your judgment matters most. The questions are good but you need to bring real product context. The agent executes well with clear direction, but that direction has to come from someone who understands the product.
>
> **Section 8: Get Started (heading: ## Get Started)**
> "If you want to try this workflow yourself, here's what you need:"
>
> **Superpowers** (the brainstorming layer):
> ```bash
> claude plugin add superpowers
> ```
> Link: `<a href="https://marketplace.claudecode.dev/plugins/superpowers" target="_blank" rel="noopener noreferrer">Superpowers on Claude Code Marketplace</a>`
>
> **Senior Project Manager agent** (based on Agency Agents, modified):
> Text: The original comes from Agency Agents (link: `https://github.com/msitarzewski/agency-agents`), a collection of specialist agents for marketing, project management, and more. Modified for specific PM needs.
> Link to modified version: `<a href="https://github.com/OrhayBenaim/blog/blob/main/.claude/agents/project-manager-senior.md" target="_blank" rel="noopener noreferrer">Senior PM Agent on GitHub</a>`
>
> **Remotion skill** (video generation):
> Link: `<a href="https://www.remotion.dev/docs/ai/skills" target="_blank" rel="noopener noreferrer">Remotion AI Skills</a>`
>
> **Jira Manager skill** (ticket creation from specs):
> Link: `<a href="https://github.com/OrhayBenaim/blog/tree/main/.claude/skills/jira-manager" target="_blank" rel="noopener noreferrer">Jira Manager on GitHub</a>`
>
> Close with: The brainstorming layer handles the orchestration. You bring the product context, it figures out which tools to use and in what order.

**Step 2: Review the post**

Verify:
- [ ] Frontmatter matches exactly (title, description, pubDate, pubTime, tags)
- [ ] Hero image path: `/blog/blog/pm-ships-hero.webp`
- [ ] Video embed path: `/blog/blog/pm-ships-pubtime-feature.mp4`
- [ ] Jira screenshot placeholder present: `/blog/blog/pm-ships-jira-tickets.webp`
- [ ] ZERO em dashes (— or –) anywhere in the post
- [ ] No AI filler words (delve, leverage, utilize, streamline, robust)
- [ ] Natural contractions used (I've, don't, it's, you'd)
- [ ] Sentence length varies naturally
- [ ] All 4 Get Started links present and correct
- [ ] "My Honest Take" section included
- [ ] Voice matches `from-idea-to-strategy-in-minutes.md`

**Step 3: Commit**

```bash
git add src/content/blog/pm-ships-with-claude-code.md
git commit -m "add blog post: How a Product Manager Ships with Claude Code"
```

---

### Task 4: SEO Review with SEO Specialist Agent

**Files:**
- Modify: `src/content/blog/pm-ships-with-claude-code.md`

**Step 1: Launch the SEO Specialist agent for review**

Launch the `SEO Specialist` agent with this brief:

> Review the blog post at `src/content/blog/pm-ships-with-claude-code.md` for SEO optimization. The target audience is product managers exploring AI tools. The primary keyword target is "product manager claude code" with secondary targets around "AI for product managers", "PM workflow automation", and "claude code for non-developers".
>
> Review and suggest improvements for:
> - Title tag and meta description (the `title` and `description` frontmatter fields)
> - Heading hierarchy (H2/H3 structure)
> - Keyword placement in headings and opening paragraphs
> - Internal linking opportunities (other posts in `src/content/blog/`)
> - Alt text on images
> - Content structure for featured snippets
> - Reading flow and scanability
>
> IMPORTANT CONSTRAINTS:
> - Do NOT change the voice or tone. The post must still read as human-written and conversational.
> - Do NOT add em dashes (— or –).
> - Do NOT add filler words or make the writing sound corporate.
> - Keep changes minimal and surgical. SEO should enhance, not override, the writing.
>
> Apply approved changes directly to the file.

**Step 2: Review SEO changes**

Verify the agent's changes didn't:
- [ ] Introduce em dashes
- [ ] Add AI-sounding language
- [ ] Break the conversational tone
- [ ] Change the frontmatter structure

**Step 3: Commit**

```bash
git add src/content/blog/pm-ships-with-claude-code.md
git commit -m "apply SEO optimizations to PM blog post"
```

---

### Task 5: Verify Build

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

### Task 6: Add Jira Screenshot (User Action Required)

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
