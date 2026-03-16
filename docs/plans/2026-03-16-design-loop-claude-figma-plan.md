# Design Loop Blog Post Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Write and publish a blog post about the design-to-code pipeline using Google Stitch, Figma Make, and Claude + Figma MCP.

**Architecture:** This is a content creation task, not a code feature. We build the fictional "Orbiter" landing page through the actual pipeline (Stitch -> Figma Make -> Claude+Figma MCP), capture screenshots at each stage, write the blog post content, and publish it to the Astro blog.

**Tech Stack:** Astro blog (markdown content collections), Google Stitch (browser), Figma Make (browser), Claude + Figma MCP, Content Creator agent, SEO agent, Nano Banana (image generation), sharp (image optimization)

---

### Task 1: Design Orbiter Landing Page Variations in Google Stitch

**Context:** Google Stitch is a browser-based tool for rapid design iteration. User will be logged in.

**Step 1: Open Google Stitch in browser**
Use the agent-browser skill to navigate to Google Stitch. User will have logged in already.

**Step 2: Generate Orbiter landing page variations**
Prompt Stitch to create multiple variations of a landing page for "Orbiter - a project management tool for remote teams." Try different visual directions: hero layouts, feature grids, color schemes. Aim for 5-10 variations.

**Step 3: Capture screenshot**
Take a screenshot showing the Stitch interface with multiple Orbiter variations visible. Save to `public/images/design-loop-stitch-variations.png`.

**Step 4: Pick the best direction**
Select the most promising variation to take forward to Figma Make.

---

### Task 2: Refine Design in Figma Make

**Context:** User has recorded a video of the Figma Make process. User will be logged in to Figma.

**Source video:** `C:\Users\Orhay\Downloads\Timeline 1.mov` - Copy this to the blog's public directory and convert to a web-friendly format (mp4/webm) for embedding in the post.

**Step 1: Copy and convert video**
Copy `C:\Users\Orhay\Downloads\Timeline 1.mov` to `public/videos/design-loop-figma-make.mp4`. Convert using ffmpeg if needed for web compatibility.

**Step 2: Move chosen design to Figma Make**
Use browser to open Figma Make with the selected Stitch direction. Refine spacing, typography, colors, and component structure.

**Step 3: Capture screenshot**
Take a screenshot of the refined Orbiter design in Figma Make, with the export button visible. Save to `public/images/design-loop-figma-make.png`.

**Step 4: Export screens**
Use Figma Make's export button to export each screen of the Orbiter landing page.

---

### Task 3: Implement Orbiter with Claude + Figma MCP

**Context:** This is the core demonstration. Use the Figma MCP to read the exported design and implement it.

**Step 1: Read design from Figma via MCP**
Use `get_design_context` and `get_screenshot` from the Figma MCP to pull the Orbiter design.

**Step 2: Implement the landing page**
Generate working HTML/CSS code that matches the Figma design. Use the @frontend-design skill for quality output. Save to a temporary location or the blog's public directory for screenshots.

**Step 3: Capture side-by-side screenshot**
Take a screenshot showing the Figma design next to the implemented code in the browser. Save to `public/images/design-loop-side-by-side.png`.

**Step 4: Demonstrate the refinement loop**
Make a change (e.g. adjust hero spacing), update both the code and push the change back to Figma using the MCP. Capture a screenshot showing this two-way update. Save to `public/images/design-loop-refinement.png`.

---

### Task 4: Generate Content and Assets with Agent Team

**Step 1: Dispatch Content Creator agent**
Use the Content Creator agent to write copy for the Orbiter landing page: headline, subheadline, feature descriptions, CTA text. This runs in parallel.

**Step 2: Dispatch SEO agent**
Use the SEO agent to optimize the blog post metadata, heading structure, and content for search. Runs in parallel with content creation.

**Step 3: Generate workflow diagram**
Use Nano Banana to create a visual diagram showing the parallel workflow: design loop in the center, Content Creator / SEO / image generation agents contributing around it. Save to `public/images/design-loop-agent-workflow.png`.

**Step 4: Capture final result**
Take a screenshot of the completed Orbiter landing page with real content in the browser. Save to `public/images/design-loop-final.png`.

---

### Task 5: Optimize All Images

**Files:**
- Process: all `public/images/design-loop-*.png` files

**Step 1: Convert images to WebP**
Use the @image-optimizer skill to convert all captured screenshots to WebP format for web delivery.

**Step 2: Verify optimized files exist**
Run: `ls public/images/design-loop-*.webp`
Expected: all 6 images present in WebP format.

---

### Task 6: Write the Blog Post Draft

**Files:**
- Create: `src/content/blog/design-loop-claude-figma.md`

**Step 1: Write the full blog post**
Create the markdown file with frontmatter and all 5 sections per the design doc. Follow these conventions:

Frontmatter format:
```yaml
---
title: "From Idea to Pixel-Perfect Code: The Design Loop with Claude and Figma"
description: "How I use Google Stitch, Figma Make, and Claude with Figma MCP to go from rough idea to production code, with design and code evolving together in a two-way loop."
pubDate: 2026-03-16
tags: ["ai", "workflow", "claude-code", "figma", "design"]
---
```

Writing rules:
- Conversational, peer-to-peer tone matching `from-idea-to-strategy-in-minutes.md`
- NO em dashes (use commas, colons, or restructured sentences instead)
- NO staccato AI patterns ("No X. No Y. No Z.")
- Images use format: `![alt text](/blog/blog/design-loop-filename.webp)`
- Embed the Figma Make video in Section 3: `<video src="/blog/videos/design-loop-figma-make.mp4" controls autoplay muted loop></video>` (or equivalent Astro-compatible embed)
- Section 4 (Claude + Figma MCP) gets ~60% of the content
- Show how you think about the process, not just the steps

**Step 2: Verify the post renders**
Run: `npx astro build` or `npx astro dev` and check the post appears correctly.

---

### Task 7: SEO Review of Blog Post

**Step 1: Dispatch SEO agent on the blog post**
Have the SEO agent review the final blog post markdown for:
- Title tag and meta description optimization
- Heading hierarchy (H1, H2, H3)
- Image alt text quality
- Internal linking opportunities to existing posts
- Keyword density and placement

**Step 2: Apply SEO suggestions**
Edit `src/content/blog/design-loop-claude-figma.md` with any improvements.

---

### Task 8: Final Review and Commit

**Step 1: Verify blog builds cleanly**
Run: `npx astro build`
Expected: clean build with no errors.

**Step 2: Review the post in dev server**
Run: `npx astro dev` and check the post visually in the browser.

**Step 3: Commit all changes**
```bash
git add src/content/blog/design-loop-claude-figma.md public/images/design-loop-*
git commit -m "feat: add blog post - The Design Loop with Claude and Figma"
```
