---
title: "How a Product Manager Ships with Claude Code"
description: "A product manager's real walkthrough: from a vague idea to a full spec, stakeholder video, and Jira tickets using Claude Code AI agents. No code written."
pubDate: 2026-03-16
pubTime: "18:00"
tags: ["ai", "workflow", "claude-code", "agents", "product-management", "ai-for-product-managers"]
---

Most people hear "Claude Code" and think it's a developer tool. Fair enough. The name has "code" in it, and the demos usually show someone generating React components or debugging Python scripts. But the thing that makes it actually powerful for a product manager isn't the code generation. It's the workflow loop. you think through what you need, hand it to a specialist agent, and get back real deliverables. That loop doesn't care if you're writing code or writing specs.

Even if you're not a PM by title, you've done the work. Figuring out what to build, why it matters, making sure the right people have the right context to go build it. That means specs, alignment artifacts, tickets. The kind of work that eats a full afternoon even for a small feature. So I started using Claude Code for this non-developer work, and the results were good enough that I want to walk you through the whole thing.

This post covers a real feature, start to finish. One idea, one conversation, and what came out the other side:

- A full feature spec with edge cases and acceptance criteria
- A stakeholder video generated automatically
- Jira tickets created directly from the spec
- Zero code written by me

![Product manager using Claude Code to generate a feature spec, stakeholder video, and Jira tickets from a single conversation](/blog/blog/pm-ships-hero.webp)

## The Idea: A Small Feature That Still Needs PM Work

I run a blog built with Astro. Four posts, all published on the same date. The homepage sort order was random because every post shared the same timestamp. Astro parses a bare date string as midnight UTC, so the sort expression returns zero for every pair and the display order depends on filesystem glob order. Not great.

The fix was simple, add a time field to each post's frontmatter so they sort in a predictable order. Not a big project. But even small features need a proper spec that an engineer can pick up, stakeholder alignment on why you're doing it, and Jira tickets to track the work. The kind of thing that eats a PM's afternoon.

## Brainstorming with AI Agents: Figuring Out What We Need

I started with the Superpowers plugin for Claude Code. If you've read [the previous post in this series](/blog/from-idea-to-strategy-in-minutes), you know how it works. It doesn't try to produce a solution right away. It asks clarifying questions one at a time, helps you think through the problem, and then builds a plan using whatever specialist agents are available.

I described the problem and it started digging into the details:

> **Me:** Blog posts all share the same date and the sort order is random on the homepage. I need a way to control the ordering.

> **Claude:** Should this be a schema-level change that adds a new field, or would you prefer to change the existing pubDate to accept full datetime strings? A new field keeps backward compatibility clean since existing posts won't need to change their pubDate format. Changing the existing field is simpler but means updating every post and potentially affecting date display.

> **Me:** New field. I don't want to touch the existing date format.

> **Claude:** Makes sense. For backward compatibility, should posts without the new time field still build and sort normally? I'd recommend making it optional and defaulting to midnight, so they sort last within their day.

> **Me:** Yes, optional with a midnight default.

Once the brainstorming layer had enough context, it produced an execution plan:

> **Step 1:** Use the Senior PM agent to write a full feature spec
>
> **Step 2:** Use Remotion to generate a stakeholder video explaining the feature
>
> **Step 3:** Use the Jira Manager to create development tickets from the spec

## "Execute this plan."

> **Me:** Execute this plan.

That single sentence is where I stopped thinking and the agent started doing. Everything from here forward happened without further input. The brainstorming layer dispatched the Senior PM agent, which handled the rest autonomously.

## What the AI Agents Delivered

### The Feature Spec

The Senior PM agent produced a full feature spec. Not a rough outline or a bullet list of ideas. A real document with context on why the change is needed, the technical approach, development tasks broken down by file, acceptance criteria for each task, and an edge cases table. The kind of spec an engineer could pick up and start building from without a single follow-up question.

From the spec:

> **Original requirement**: Blog posts should support a time field (in addition to the existing date) that is used only for sorting, not displayed in the UI.

The edge cases table covered scenarios I probably wouldn't have thought to document:

> | Post without pubTime | Treated as 00:00 UTC, sorts last within its day |
> | Post with invalid time like "2pm" | Zod regex rejects at build time |

The level of detail went further than I expected. A backward compatibility table explaining why a separate field was chosen over modifying the existing pubDate. Exact file paths for every change. A files changed summary distinguishing between modified and new files. Acceptance criteria per task, not per feature. This is the kind of thoroughness that takes real effort to produce manually, and it's usually the first thing that gets cut when you're trying to move fast.

### The Stakeholder Video

The agent used <a href="https://www.remotion.dev/" target="_blank" rel="noopener noreferrer">Remotion</a> to generate a short video explaining the feature and why it matters. This is the kind of artifact you'd normally spend time creating in Google Slides before a stakeholder review. The video covers the problem, the solution, and the scope of changes in a format that someone outside the engineering team can actually follow.

<video src="/blog/blog/pm-ships-pubtime-feature.mp4" autoplay loop muted playsinline style="max-width: 100%; margin: 0 auto; display: block; border-radius: 12px;"></video>

### The Jira Tickets

The agent used the <a href="https://github.com/OrhayBenaim/blog/tree/main/.claude/skills/jira-manager" target="_blank" rel="noopener noreferrer">Jira Manager skill</a> to create development tickets directly from the spec. Each task became a ticket with the right description, acceptance criteria, and priority. No copy-pasting between tools, no reformatting spec sections into ticket descriptions, no manually setting fields. The spec was the source of truth and the tickets came straight from it.

![Jira board showing development tickets automatically created from the AI-generated feature spec](/blog/blog/pm-ships-jira-tickets.webp)

## My Honest Take: What AI Does Well (and Where PMs Still Matter)

What surprised me was the spec quality. The edge cases table, the backward compatibility analysis, the file-by-file change summary with clear labels for new files versus modified ones. Anyone who's written specs knows the tedious part is always the completeness. Covering the edge cases, documenting what doesn't change, making sure an engineer won't have to come back and ask "what happens when this field is missing?" The agent handled that part well.

What still needs a human is the brainstorming layer. That's where your judgment matters most. The questions it asks are good, but you need to bring real product context. Why this approach over that one. What trade-offs matter for your specific product and team. The agent executes well with clear direction, but that direction has to come from someone who understands the product. The brainstorming conversation is short, but it's the part that actually determines whether the output is useful.

## Get Started: Set Up Claude Code for PM Workflows

If you want to try this workflow yourself, here's what you need:

**Superpowers** (the brainstorming layer):

```bash
claude plugin add superpowers
```

<a href="https://marketplace.claudecode.dev/plugins/superpowers" target="_blank" rel="noopener noreferrer">Superpowers on Claude Code Marketplace</a>

**Senior Project Manager agent** (the spec and coordination specialist):

The original comes from <a href="https://github.com/msitarzewski/agency-agents" target="_blank" rel="noopener noreferrer">Agency Agents</a>, a collection of specialist agents for marketing, project management, and more. I modified it for specific PM needs like spec writing, stakeholder artifact generation, and Jira integration.

<a href="https://github.com/OrhayBenaim/blog/blob/main/.claude/agents/project-manager-senior.md" target="_blank" rel="noopener noreferrer">Senior PM Agent on GitHub</a>

**Remotion skill** (video generation):

<a href="https://www.remotion.dev/docs/ai/skills" target="_blank" rel="noopener noreferrer">Remotion AI Skills</a>

**Jira Manager skill** (ticket creation from specs):

<a href="https://github.com/OrhayBenaim/blog/tree/main/.claude/skills/jira-manager" target="_blank" rel="noopener noreferrer">Jira Manager on GitHub</a>

The brainstorming layer handles the orchestration. You bring the product context, it figures out which tools to use and in what order.

Claude Code isn't just for developers. If you spend too much time on specs, tickets, and alignment artifacts, this workflow gives you that time back. The thinking is still yours. The execution doesn't have to be.
