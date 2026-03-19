# Blog Post Design: Unlock the True Power of Photo Editing

**Date:** 2026-03-19
**Status:** Approved

## Concept

A blog post showing how to surgically edit specific aspects of a photo without changing the scene. The workflow uses structured JSON extraction prompts with Gemini to analyze an image, then feeds modified JSON + the original image to Nano Banana to regenerate with precise changes.

## Core Message

Natural language image editing is vague ("make it darker" gets reinterpreted). JSON extraction gives you surgical control. You edit a data structure, not guess with words.

## Workflow

1. **Image → Gemini** (with specialized extraction prompt) → structured JSON
2. **Modify the JSON** (change only the fields you want)
3. **Original image + modified JSON → Nano Banana** → regenerated image

## Post Structure

### Opening
The frustration of telling AI "make this nighttime" in plain text. It reimagines instead of editing. Furniture moves, decorations disappear, the vibe shifts. You wanted one change but got a different image.

### Section 1: The Workflow
Extract → Modify → Regenerate. Three steps. Gemini reads the image with a specialized prompt and returns a structured JSON breakdown. You tweak the specific fields you care about. Nano Banana takes the original image plus your modified JSON and produces the result.

### Section 2: The Example
Walk through the living room transformation:
- Show daytime image
- Show extracted lighting JSON (light sources, shadows, time of day, mood)
- Show what changed in the JSON (swapped daylight for warm lamps, added moonlight through window, shifted shadows, changed time to late evening)
- Show nighttime result
- Both images displayed for comparison

### Section 3: The Extraction Toolkit
Quick overview of the 4 specialized prompts:
- **Lighting & Time of Day** - light sources, shadows, color temperatures, mood
- **Logos & Text** - text strings, fonts, logos, brand marks
- **Camera Perspective** - focal length, lens type, vanishing points, depth of field
- **Objects for Compositing** - bounding areas, edge complexity, shadows, compositing tips

Show the JSON schema structure briefly for each. Not a full reference, just enough to show the range.

### Section 4: Why This Works
JSON is precise. Natural language is vague. When you say "make it darker," the AI interprets freely. When you hand it specific color temperatures, shadow directions, and light source types, it executes exactly what you asked.

## Assets

- Daytime living room image (original)
- Nighttime living room image (modified result)
- Both saved to public/blog/ as optimized WebP

## Follow-up

After the post is complete, create an agent that automates this entire flow (extract → modify → regenerate).
