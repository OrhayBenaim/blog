# Unlock the True Power of Photo Editing - Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Publish a blog post showing how to use structured JSON extraction prompts (via Gemini) + Nano Banana to surgically edit specific aspects of a photo without changing the scene.

**Architecture:** Blog post with two hero images (daytime/nighttime living room), JSON code blocks showing the extraction and modification, and an overview of 4 specialized extraction prompts. Content Creator agent writes the post, SEO Specialist reviews, images are optimized to WebP.

**Tech Stack:** Astro blog (Markdown), sharp (image optimization), WebP format

---

### Task 1: Optimize and Copy Images

**Files:**
- Source: `C:\Users\Orhay\Downloads\Generated Image March 19, 2026 - 5_26PM.jpg` (daytime)
- Source: `C:\Users\Orhay\Downloads\Generated Image March 19, 2026 - 7_19PM.jpg` (nighttime)
- Create: `.worktrees/photo-analysis-prompts/public/blog/photo-editing-workflow-day.webp`
- Create: `.worktrees/photo-analysis-prompts/public/blog/photo-editing-workflow-night.webp`

**Step 1: Optimize daytime image**

Use the `image-optimizer` skill to convert the daytime JPG to WebP at `public/blog/photo-editing-workflow-day.webp`. Target web quality.

**Step 2: Optimize nighttime image**

Use the `image-optimizer` skill to convert the nighttime JPG to WebP at `public/blog/photo-editing-workflow-night.webp`. Target web quality.

**Step 3: Verify both files exist**

```bash
ls -la .worktrees/photo-analysis-prompts/public/blog/photo-editing-workflow-*.webp
```

Expected: Both files present, reasonable file sizes (under 200KB each).

**Step 4: Commit**

```bash
cd .worktrees/photo-analysis-prompts && git add public/blog/photo-editing-workflow-day.webp public/blog/photo-editing-workflow-night.webp && git commit -m "feat: add photo editing workflow blog post images"
```

---

### Task 2: Write Blog Post Content

**Files:**
- Create: `.worktrees/photo-analysis-prompts/src/content/blog/unlock-photo-editing-power.md`

**Step 1: Draft blog post with Content Creator agent**

Use the **Content Creator agent** to write the blog post. Provide the agent with:

- The design doc at `docs/plans/2026-03-19-photo-editing-workflow-design.md`
- The writing style guidelines from CLAUDE.md (conversational, no em dashes, no AI words)
- The frontmatter format:
  ```yaml
  ---
  title: "Unlock the True Power of Photo Editing with AI and Structured Prompts"
  description: "[SEO-friendly description, ~150 chars]"
  pubDate: 2026-03-19
  pubTime: "20:00"
  tags: ["ai", "photo-editing", "workflow", "gemini", "image-generation"]
  ---
  ```

- Image references use `/blog/blog/` prefix:
  - `![Daytime living room](/blog/blog/photo-editing-workflow-day.webp)`
  - `![Nighttime living room](/blog/blog/photo-editing-workflow-night.webp)`

**Content structure the agent must follow:**

1. **Opening** - The frustration of AI reimagining your image when you just wanted to change one thing. Set up the problem naturally.

2. **## The Workflow** - Extract → Modify → Regenerate. Explain the three steps: Gemini with extraction prompt gives you JSON, you modify specific fields, Nano Banana takes original image + modified JSON and produces the result.

3. **## From Day to Night in One Edit** - The living room walkthrough:
   - Show daytime image
   - Show the extracted lighting JSON (the first JSON from user's example)
   - Explain what fields were changed and why
   - Show the modified nighttime JSON (the second JSON from user's example)
   - Show nighttime image result
   - Emphasize: same room, same furniture, same composition. Only the lighting changed.

4. **## The Extraction Toolkit** - Brief overview of 4 specialized prompts:
   - Lighting & Time of Day
   - Logos & Text
   - Camera Perspective
   - Objects for Compositing
   For each, describe what it extracts in 2-3 sentences and show a condensed example of the JSON structure (not the full schema, just key fields).

5. **## Why JSON Beats Natural Language** - JSON is precise, natural language is vague. "Make it darker" vs specific color temperatures and shadow directions. You're editing a data structure, not hoping the AI interprets your words correctly.

**The agent must include these exact JSON blocks in the post:**

Extracted daytime lighting:
```json
{
  "lighting_analysis": {
    "light_sources": [
      {
        "type": "Natural diffused daylight entering through a large glass window or door",
        "direction": "From camera left",
        "color_temperature": "Neutral to slightly cool daylight, approximately 5500K, casting a clean white light (#FFFFFF) with subtle cool undertones (#F0F8FF)",
        "relative_intensity": "Dominant key light providing the majority of the room's illumination"
      },
      {
        "type": "Recessed ceiling downlights (LED or Halogen)",
        "direction": "Top-down from the ceiling",
        "color_temperature": "Warm white, approximately 3000K, emitting a cozy yellow-orange hue (#FFE4B5)",
        "relative_intensity": "Moderate secondary fill light balancing the cooler daylight"
      }
    ],
    "shadows": {
      "direction": "Falling towards camera right and pooling directly underneath the furniture (sofa, coffee table, and console)",
      "edge_softness": "Very soft and highly diffused with gradual transitions",
      "relative_length": "Short to medium, mostly localized under the objects casting them rather than stretching across the floor",
      "color_tint": "Warm dark grey (#3A3530) influenced by the wooden floors and warm ambient light reflections"
    },
    "time_of_day_estimate": "Mid-day to early afternoon, indicated by the bright, even luminosity and lack of long, directional sun rays",
    "weather_conditions": "Bright overcast or heavily clouded sky, acting as a massive natural diffuser that softens the incoming sunlight",
    "ambient_fill_to_direct_key_ratio": "High ambient fill relative to the soft key light, resulting in a low-contrast, evenly exposed environment with rich shadow detail",
    "overall_mood": "Bright, inviting, and softly balanced"
  }
}
```

Modified nighttime lighting:
```json
{
  "lighting_analysis": {
    "light_sources": [
      {
        "type": "Warm artificial interior lighting (Floor lamp and recessed ceiling spots)",
        "direction": "Multi-directional; primarily from camera right (floor lamp) and top-down (ceiling spots)",
        "color_temperature": "Very warm incandescent/soft white, approximately 2700K, casting a rich amber-gold glow (#FFB347)",
        "relative_intensity": "Primary light source; creates high-contrast pools of light against the dark exterior"
      },
      {
        "type": "Ambient moonlight/nocturnal sky through window",
        "direction": "From camera left",
        "color_temperature": "Cool, deep blue/cyan, approximately 7500K-10000K (#191970)",
        "relative_intensity": "Low intensity; provides deep shadows and a silhouette effect for the trees outside"
      },
      {
        "type": "Accent shelving lighting",
        "direction": "From the background/bookcase area",
        "color_temperature": "Warm white, approximately 3000K (#FDF5E6)",
        "relative_intensity": "Subtle glow used to create depth in the background"
      }
    ],
    "shadows": {
      "direction": "Projecting away from the floor lamp toward camera left; deep shadows in the corners of the room",
      "edge_softness": "Moderately soft near the lamp, becoming very blurred and dark in the room's periphery",
      "relative_length": "Long and pronounced, stretching across the rug and sofa as the light source is lower and more directional",
      "color_tint": "Deep, desaturated umber or near-black (#1C1C1C)"
    },
    "time_of_day_estimate": "Late evening or night",
    "weather_conditions": "Clear night sky; no visible atmospheric diffusion from the outside, allowing for high contrast between indoor warmth and outdoor darkness",
    "ambient_fill_to_direct_key_ratio": "Low ambient fill; the scene relies on localized 'pools' of light, creating a dramatic contrast between the illuminated seating area and the dark window/corners",
    "overall_mood": "Cozy, intimate, and moody"
  }
}
```

**Step 2: Review the draft**

Read the generated post. Check for:
- No em dashes
- No AI words (delve, leverage, utilize, furthermore, notably)
- Conversational tone matching CLAUDE.md examples
- Both images properly embedded
- Both JSON blocks included
- Frontmatter is correct

**Step 3: Commit**

```bash
cd .worktrees/photo-analysis-prompts && git add src/content/blog/unlock-photo-editing-power.md && git commit -m "feat: add photo editing workflow blog post draft"
```

---

### Task 3: SEO Review

**Files:**
- Modify: `.worktrees/photo-analysis-prompts/src/content/blog/unlock-photo-editing-power.md`

**Step 1: Run SEO review**

Use the **SEO Specialist agent** to review the blog post. Provide:
- The post file path
- Target keywords: "AI photo editing", "structured prompts", "image editing workflow", "JSON image extraction"
- Ask for: title tag review, meta description, heading structure, keyword placement, internal linking suggestions

**Step 2: Apply SEO recommendations**

Edit the blog post to incorporate the SEO specialist's feedback. Focus on:
- Title and description optimization
- Heading hierarchy
- Keyword placement (natural, not stuffed)
- Image alt text quality

**Step 3: Commit**

```bash
cd .worktrees/photo-analysis-prompts && git add src/content/blog/unlock-photo-editing-power.md && git commit -m "feat: apply SEO optimizations to photo editing workflow post"
```

---

### Task 4: Final Review and Merge Readiness

**Step 1: Verify all files are in place**

```bash
cd .worktrees/photo-analysis-prompts && ls -la public/blog/photo-editing-workflow-*.webp && ls -la src/content/blog/unlock-photo-editing-power.md && ls -la docs/prompts/photo-analysis-extraction-prompts.md
```

Expected: All files present.

**Step 2: Review git log**

```bash
cd .worktrees/photo-analysis-prompts && git log --oneline main..HEAD
```

Expected: Clean commit history with image, post draft, and SEO optimization commits.

**Step 3: Notify ready for merge**

Tell the user the blog post is ready. Ask if they want to merge the worktree into main.
