---
title: "From Idea to Strategy in Minutes"
description: "How I use AI agents to brainstorm ideas and hand them off to specialists. A real walkthrough of going from a vague idea to a full TikTok strategy."
pubDate: 2026-03-16
tags: ["ai", "workflow", "claude-code", "agents"]
---

I've been experimenting with a workflow that changed how I approach creative projects. The idea is simple: you talk to one AI to figure out what you actually want, and then it hands the refined idea to a specialist agent that builds the real thing. Think of it as having a brainstorming partner who also knows exactly which expert to call when you're ready to execute.

This is the first post in a series where I walk through real examples of this two-layer approach. Each post will cover a different use case with a different specialist. For this one, I'm building a TikTok content strategy for a fictional fitness brand called "PulseForm."

The whole thing took minutes. Here's how it works.

![A lightbulb with ideas flowing into a polished strategy document](/blog/blog/from-idea-to-strategy-hero.webp)

## The Setup: Two Layers

The workflow has two distinct layers, and understanding the split is what makes everything click.

**Layer 1: Brainstorming.** This is the Superpowers skill for Claude Code. It doesn't try to do the work for you. Instead, it asks questions, offers options, and helps you figure out what you actually need. It's a thinking partner, not a content machine. You can install it with:

```bash
claude plugin add superpowers
```

You can find it here: [Superpowers on Claude Code Marketplace](https://marketplace.claudecode.dev/plugins/superpowers)

**Layer 2: Specialist.** Once your idea is clear, the brainstorming layer hands it off to a specialist agent. In this case, a [TikTok Strategist](https://github.com/msitarzewski/agency-agents/blob/main/marketing/marketing-tiktok-strategist.md) from the [Agency Agents](https://github.com/msitarzewski/agency-agents) collection. These agents are built with deep knowledge of their specific domain. They don't ask you 20 questions. They take a clear brief and produce real, actionable output.

The brainstorming layer is the bridge between "I have a vague idea" and "here's a tight brief that a specialist can run with."

![Brainstorming scene flowing into a specialist workspace](/blog/blog/two-layers-concept.webp)

## The Walkthrough

Let me show you the actual process, from first prompt to finished strategy.

### Starting the Conversation

I kicked things off with a pretty standard brief:

> **Me:** I need a TikTok content strategy for "PulseForm" -- a fitness brand targeting 18-28 year olds. They sell resistance bands and home workout programs. Their voice is motivating but not preachy.

### Defining the Goal

Claude didn't just start generating a strategy. It asked what mattered most.

> **Claude:** What's PulseForm's main goal with TikTok?
>
> 1. **Brand awareness** - Get the name out there, build a following
> 2. **Direct sales** - Drive traffic to product pages
> 3. **Community building** - Create a tribe of PulseForm users
> 4. **Content-first approach** - Become a go-to fitness account that happens to sell products
>
> I'd lean toward option 4 since it tends to perform best on TikTok for brands targeting 18-28 year olds. Hard selling doesn't work well with that demographic on that platform.

> **Me:** Brand awareness. We want to get the name out there first.

That's already useful. I came in thinking "we need a TikTok strategy" and within one exchange I'd made a real decision about what the strategy should optimize for.

### Finding the Content Style

> **Claude:** What kind of content style fits PulseForm's "motivating but not preachy" voice best?
>
> 1. **Quick workout clips** - 15-30 second resistance band exercises. High utility, easy to share.
> 2. **Transformation/progress content** - Before/after stories, "day 1 vs day 30" style.
> 3. **Trend-riding fitness content** - Take trending TikTok sounds and formats, put a fitness spin on them. More entertainment, more reach.
> 4. **Creator-led personality content** - Build around 1-2 faces who become the brand.
>
> My recommendation would be a mix of 1 and 3. Quick workout clips give people a reason to follow (value), and trend-riding gives the algorithm a reason to push the content (discoverability).

> **Me:** Trend-riding fitness content. That's the play.

### Brand Presence Without Selling

> **Claude:** How should PulseForm show up in the content without being salesy?
>
> 1. **Product as prop** - The resistance bands just happen to be in every video. No callouts, no "link in bio" pressure.
> 2. **Branded challenges** - Create a signature move or challenge that uses the bands.
> 3. **Subtle watermark/aesthetic** - Consistent color scheme, logo placement, and visual style that makes every video instantly recognizable as PulseForm even on mute.
>
> I'd go with 1 as the foundation. On TikTok, the moment something feels like an ad, people scroll.

> **Me:** The consistent visual aesthetic approach. Strong branding without the hard sell.

Three exchanges. That's it. In about two minutes I went from "I need a TikTok strategy" to a clear brief: brand awareness through trend-riding fitness content with a strong visual identity and no hard selling.

### The Handoff

Here's the part I like most. The brainstorming layer packaged everything up and handed it to the TikTok Strategist agent. I didn't have to write a brief, copy-paste context, or re-explain anything. The specialist picked up right where the brainstorming left off.

<video src="/blog/blog/tiktok-strategy-fitness.mp4" autoplay loop muted playsinline style="max-width: 300px; margin: 0 auto; display: block; border-radius: 12px;"></video>

### What the Specialist Produced

The TikTok Strategist came back with a full strategy. Here are the best parts.

**Content Pillars (40/30/20/10 Split)**

| Pillar | Share | Series Name | What It Covers |
|--------|-------|-------------|----------------|
| Education | 40% | "Band Science" | Form tips, myth-busting, exercise breakdowns |
| Entertainment | 30% | "Band Life" | Trend remixes, gym humor, relatable home workout struggles |
| Inspiration | 20% | "Pulse Check" | Real transformation stories, personal journeys |
| Promotional | 10% | "The Drop" | Subtle product showcases that feel native to TikTok |

**Standout Content Ideas**

These were my favorites from the batch:

- **"POV: You try to work out at home but..."** - Comedy skit where the creator keeps getting interrupted. Final shot: one perfect rep, triumphant face.
- **"She said bands don't build real muscle"** - Creator doesn't argue. Just shows their workout, intense, sweating. No words needed.
- **"Resistance band ASMR but make it chaotic"** - Start with satisfying ASMR then escalate into chaos.

Every single one of these feels like something you'd actually watch. Not branded content that people skip past.

**Posting Schedule**

The strategy recommended 5-7 posts per week, with each day assigned to a specific content pillar. It also built in 1-2 "flex slots" per week for reactive trend content, which is critical on TikTok where timing is everything.

**Daily Trend-Riding Workflow**

This was surprisingly practical:

1. **Monitor** (20 min/morning) - Scan trending sounds and formats
2. **Evaluate** (5 min/trend) - Does this fit PulseForm's voice?
3. **Concept** (15 min) - Sketch the fitness spin
4. **Produce** (30-60 min) - Shoot and edit
5. **Post and Monitor** (immediate + 2 hours) - Publish and track early engagement

**Visual Identity**

- PulseForm Orange (#FF6B35) as the signature brand color
- Subtle watermark at 60-70% opacity
- Resistance bands visible in 80%+ of videos
- Consistent warm lighting, real spaces (not studios)

### My Honest Take

I was genuinely surprised by the quality. The content pillar split felt well-reasoned, not arbitrary. The specific video ideas were creative and actually felt like TikTok content, not repurposed Instagram posts. And the daily workflow for trend-riding was the kind of operational detail that usually takes a strategist hours to put together.

Is it perfect? No. You'd still want a human to review the ideas, adjust for what's actually trending right now, and add brand-specific context that no AI can fully understand. But as a starting point, it's better than most first drafts I've seen from real strategy decks.

## Get Started

If you want to try this workflow yourself, here's what you need:

**Superpowers** (the brainstorming layer):

```bash
claude plugin add superpowers
```

[Superpowers on Claude Code Marketplace](https://marketplace.claudecode.dev/plugins/superpowers)

**TikTok Strategist** (the specialist agent used in this post):

[TikTok Strategist on GitHub](https://github.com/msitarzewski/agency-agents/blob/main/marketing/marketing-tiktok-strategist.md) — part of the [Agency Agents](https://github.com/msitarzewski/agency-agents) collection, which includes specialists for SEO, content creation, brand strategy, and more.

The brainstorming layer will guide you through the rest, including finding and using the right specialist for whatever you're building.
