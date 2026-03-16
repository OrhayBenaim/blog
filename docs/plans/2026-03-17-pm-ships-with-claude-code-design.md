# Design: "How a Product Manager Ships with Claude Code"

## Overview

Blog post targeting product managers, showing that Claude Code isn't just for developers. Walks through a real PM workflow: brainstorming a feature idea, handing it off to a Senior PM agent that produces a spec, stakeholder video, and Jira tickets.

## Decisions

- **Angle**: "Claude Code isn't just for developers" - PM discovers they can use the same tool their engineering team uses
- **Technical level**: Hybrid - show 1-2 prompt exchanges during brainstorming, then shift to outcomes for agent execution
- **Handoff moment**: "Execute this plan" single sentence as the inflection point (matches TikTok strategy post pattern)
- **Title**: "How a Product Manager Ships with Claude Code"
- **Opener image**: PM workspace with artifacts (spec, video, Jira board) flowing out from a laptop

## Frontmatter

```yaml
title: "How a Product Manager Ships with Claude Code"
description: "From a vague idea to a full spec, stakeholder video, and Jira tickets. A real walkthrough of PM workflows powered by AI agents."
pubDate: 2026-03-16
pubTime: "18:00"
tags: ["ai", "workflow", "claude-code", "agents", "product-management"]
```

## Structure

### 1. Hook (2-3 paragraphs)
Open with the misconception: Claude Code is a developer tool. Pivot: the workflow that makes it powerful isn't writing code, it's the loop of thinking through what you need, handing it to a specialist, getting back real deliverables. That loop works for anyone. Set up the PM walkthrough.

### 2. Hero Image
PM workspace with artifacts flowing out. Generated with NanoBanana.

### 3. "The Idea" (~2 paragraphs)
Context: blog with four posts sharing the same date, posts sorting randomly, need a `pubTime` field. A small feature that still needs a spec, stakeholder buy-in, and tickets. The kind of thing that eats a PM's afternoon.

### 4. "Brainstorming: Figuring Out What We Need" (~4-5 exchanges shown)
Show 1-2 actual prompt/response exchanges. The brainstorming layer asks clarifying questions (schema change? backward compatibility?). User makes decisions. Within minutes, a clear picture. End with the plan: spec, stakeholder video, Jira tickets.

### 5. "Execute this plan." (The Handoff)
One sentence prompt. Short paragraph: you stopped thinking, the agent started doing. Clear dividing line between human-driven and agent-driven work.

### 6. "What Came Back" (Outcomes, no prompts shown)
Three subsections:

- **The Spec**: What the Senior PM agent produced (`add-time-field-for-sorting.md`). Quote 2-3 lines to show quality.
- **The Stakeholder Video**: Embed `pubtime-feature.mp4`. The agent created a Remotion video explaining the feature for stakeholders.
- **The Jira Tickets**: Screenshot (user will add). Tickets created automatically from the spec.

### 7. "My Honest Take" (~2 paragraphs)
What surprised me, what's still rough, where a human still needs to step in. Grounded, consistent with other posts.

### 8. "Get Started"
Links to all tools used:

- **Superpowers** (brainstorming layer): `claude plugin add superpowers` — [Superpowers on Claude Code Marketplace](https://marketplace.claudecode.dev/plugins/superpowers)
- **Senior Project Manager agent**: Based on [Agency Agents](https://github.com/msitarzewski/agency-agents/blob/main/project-management/project-manager-senior.md), modified — [Senior PM Agent on GitHub](https://github.com/OrhayBenaim/blog/blob/main/.claude/agents/project-manager-senior.md)
- **Remotion skill** (video generation): [Remotion AI Skills](https://www.remotion.dev/docs/ai/skills)
- **Jira Manager skill** (ticket creation): [Jira Manager on GitHub](https://github.com/OrhayBenaim/blog/tree/main/.claude/skills/jira-manager)

## Assets

| Asset | Source | Status |
|---|---|---|
| Hero image (PM workspace with artifacts) | Generate with NanoBanana | Needed |
| Stakeholder video (`pubtime-feature.mp4`) | Already exists at `docs/pm/pubtime-feature.mp4` | Ready |
| Jira tickets screenshot | User will provide | Pending |

## Writing Guidelines

- Match existing blog voice: conversational, problem-first, honest
- No em dashes (per feedback memory)
- No staccato AI patterns
- Include "My Honest Take" section consistent with other posts
