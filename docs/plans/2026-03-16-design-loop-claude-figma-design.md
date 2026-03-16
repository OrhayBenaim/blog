# Blog Post Design: The Design Loop with Claude and Figma

**Date:** 2026-03-16
**Type:** Blog post (process overview)
**Approach:** "The Design Loop" (iterative focus, Approach B)

## Meta

- **Title:** "From Idea to Pixel-Perfect Code: The Design Loop with Claude and Figma"
- **Audience:** Both designers and developers, anyone building products
- **Narrative angle:** Process overview, not a tutorial. Shows the methodology with a fictional product (Orbiter, a project management tool for remote teams) as a running example.
- **Writing style:** Conversational, peer-to-peer, "how I do this" tone. Avoid em dashes and staccato AI patterns. Reference voice: `from-idea-to-strategy-in-minutes.md`.

## Pipeline / Tools

- **Google Stitch** - rapid design iteration (browser)
- **Figma Make** - refine designs into proper Figma files (user has video of this)
- **Claude + Figma MCP** - implement code from Figma, refine both code and design in a two-way loop
- **Content Creator agent** - blog/marketing copy for the fictional product
- **SEO agent** - optimization
- **Nano Banana / image generation** - visual assets as needed
- **Browser recording** - capturing screenshots of the process

## Structure

### Section 1: Opening Hook + Thesis (short)
Design and code have always been separate worlds with a painful handoff. What if the loop could close, where your AI assistant implements the design and refines it, pushing changes back to Figma as you go?

Introduce the pipeline: rapid ideation (Stitch) -> refinement (Figma Make) -> implementation + iteration (Claude + Figma MCP) with agents handling content/SEO/assets in parallel.

Introduce Orbiter as the running example.

### Section 2: Rapid Ideation with Google Stitch (light)
What Stitch is and why it's useful: throw an idea at it, get back multiple design variations fast. Generate 5-10 different takes on the Orbiter landing page in minutes. Goal is volume, not perfection. Looking for the spark.

**Image:** Screenshot of Stitch with several Orbiter variations side by side.

### Section 3: Refining in Figma Make (light)
Figma Make takes the rough direction and gives you a proper Figma file with real layers, components, structure. Tweak spacing, colors, typography. Key detail: export button lets you grab each screen cleanly for Claude.

**Image:** Screenshot of Orbiter in Figma Make with export option visible.
**Video:** User-provided video of Figma Make in action.

### Section 4: Claude + Figma MCP - The Two-Way Bridge (heavy, 3 sub-sections)

#### 4a: First Implementation
Claude reads the Figma file through MCP, understands layout/components/spacing/colors, generates working code that faithfully matches the design.

**Image:** Side-by-side of Figma design and implemented code in browser.

#### 4b: The Refinement Loop (the unique insight)
The core of the post. You give feedback, Claude updates code AND pushes changes back to Figma. Design file becomes a living document. The loop: Figma -> Code -> Feedback -> Code + Figma updated -> repeat. No handoff because design and code evolve together.

**Image:** Screenshot showing Claude updating both code and Figma in the same conversation.

#### 4c: Working With the Agent Team
Content Creator writes copy (headlines, features, CTAs). SEO agent optimizes metadata and structure. Image generation for custom visuals. Agents work in parallel, so content and assets are ready when design/code are solid.

**Image:** Diagram or screenshot showing parallel workflow: design loop center, agents contributing around it.

### Section 5: The Result + Closing (short)
Show the finished Orbiter landing page. Highlight: idea to production-ready code with a living Figma file that stayed in sync.

**Image:** Final screenshot of completed Orbiter landing page.

Closing thought: the takeaway is the loop closing. Design and code become fluid. Claude is the bridge. Specialized agents mean you build complete: design, code, content, SEO, assets all moving forward together.

No formal "steps to get started" section. Show how you think, let the reader draw conclusions.

## Weight Distribution
- Sections 1, 2, 3, 5: ~20% each (light)
- Section 4: ~60% (heavy, 3 sub-sections)

## Images (6 total)
1. Stitch variations of Orbiter
2. Figma Make refined design + export
3. Side-by-side Figma vs implemented code
4. Claude updating code and Figma simultaneously
5. Parallel agent workflow diagram
6. Final Orbiter landing page

## Video
- User-provided video of Figma Make process
