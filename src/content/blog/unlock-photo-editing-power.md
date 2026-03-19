---
title: "AI Photo Editing Without the Chaos: A Structured Prompt Workflow"
description: "Stop getting completely different images when you ask AI for one change. This AI photo editing workflow uses structured JSON prompts to edit lighting, mood, or branding while keeping the rest of your scene intact."
pubDate: 2026-03-19
pubTime: "20:00"
tags: ["ai", "photo-editing", "workflow", "gemini", "image-generation", "structured-prompts", "json", "image-editing"]
---

You've been there. You have a photo that's almost perfect, but you want to change one thing. Maybe the lighting. Maybe the time of day. So you open up an AI image tool and type "make it nighttime."

And the AI delivers a completely different image. The furniture moved. The decorations vanished. The camera angle shifted. You asked for one change and got a new scene.

This happens because natural language is vague. The AI doesn't know what you want to keep. It just interprets your words and generates something new.

There's a better image editing workflow. One built on structured prompts and JSON extraction that lets you change exactly what you want and nothing else.

## The Image Editing Workflow: Extract, Modify, Regenerate

The approach is simple. Extract, modify, regenerate.

First, you send your image to Gemini with a specialized extraction prompt. It analyzes the photo and returns a structured JSON breakdown of specific features. Lighting, shadows, color temperatures, mood. All of it mapped out in precise, editable fields.

Second, you open that JSON and change only the fields you care about. Want nighttime? Swap the light sources. Adjust the shadow direction. Shift the color temperature. Leave everything else untouched.

Third, you send the original image plus the modified JSON to Nano Banana. It generates the result using the original as a reference, applying only your changes.

The key insight is that you're editing a data structure, not guessing with natural language. This is what makes AI photo editing actually reliable. You're telling the model exactly what changed and what stayed the same.

## AI Photo Editing in Action: Day to Night

Here's a real example. Start with this daytime living room.

![Original daytime living room photo before AI photo editing, bright natural daylight streaming through large windows with modern furniture and warm wood tones](/blog/blog/photo-editing-workflow-day.webp)

I fed this image to Gemini with a lighting extraction prompt. Here's what it returned:

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

Look at how much detail that captures. Every light source, every shadow characteristic, even the weather outside the window. All of it structured and editable.

Now here's what I changed. I swapped the natural daylight for warm artificial lamps. Added cool moonlight coming through the window instead of overcast sky. Introduced accent shelving lights in the background for depth. Shifted the shadows to be longer and darker, projecting from a floor lamp. Changed the time to late evening. Changed the mood from bright and inviting to cozy and intimate.

Here's the modified JSON:

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

I pasted the original image plus this modified JSON into Nano Banana. Here's the result.

![The same living room after AI photo editing with structured prompts, transformed to nighttime with warm lamp light and cozy evening atmosphere](/blog/blog/photo-editing-workflow-night.webp)

Same room. Same furniture. Same composition. Same camera angle. Only the lighting changed. That's what photo editing with AI looks like when you use structured prompts instead of guessing.

## Same Room, Different Sofa

Lighting is one dimension. But this works for anything the extraction prompts can capture. Here's another example using the same room. This time I extracted the objects and changed just the sofa, from the original grey linen to an olive green textured velvet.

Here's the relevant part of the modified JSON:

```json
{
  "name": "L-shaped Sectional Sofa",
  "colour": "Olive green",
  "material": "Textured velvet fiber",
  "position_in_room": "Center-left, primary seating area",
  "lighting_position": "Under ceiling spotlights"
}
```

Two fields changed. Color and material. Everything else in the scene stayed exactly where it was.

![The same living room with the sofa changed from grey linen to olive green velvet, all other furniture and decor unchanged](/blog/blog/photo-editing-workflow-sofa.webp)

Same coffee table. Same rug. Same gallery wall. Same plant in the corner. The sofa is different and nothing else moved. You're not regenerating a room. You're swapping one object's properties in a JSON file and letting the AI handle the rest.

## Five JSON Extraction Prompts for Any Photo

These are the five specialized extraction prompts that power this workflow. Each one breaks down a different aspect of any photo into structured, editable JSON. You've already seen lighting and objects in action above. Here's the full toolkit.

**General Scene & Objects**

This is the starting point. It extracts the room style, color palette, and every object with its color, material, and position. This is the prompt I used for the sofa swap example above.

```
Analyze the interior design image and convert all visual information into highly detailed structured JSON format. Focus specifically on isolating individual objects and lighting placements. For each key object, extract its precise colour (using descriptive names or hex codes) and its exact material (eg. matte leather, brushed steel, oak wood). Include JSON keys for 'room_style', 'overall_colour_palette', and an 'object' array containing 'name','colour','material', 'position_in_room' and 'lighting_position'. Output ONLY valid JSON and format the output as a copyable JSON code block using Markdown.
```

**Lighting & Time of Day**

```
You are a lighting analysis specialist for photography. Analyze the provided photo and extract all lighting information as structured JSON.

Examine every visible and inferred light source in the image. For each light source, describe its type (natural sunlight, overcast sky, tungsten lamp, fluorescent panel, neon sign, candle, etc.), the direction it comes from relative to the camera, its approximate color temperature as a descriptive label and Kelvin estimate, and its intensity relative to other sources in the scene.

Describe the shadows in the image: their direction, how soft or hard their edges are, their approximate length relative to the objects casting them, and their color tint.

Estimate the time of day based on light angle, color, and shadow behavior. Describe weather or atmospheric conditions that affect the light (overcast, haze, fog, clear sky, rain, dust particles catching light, etc.).

Assess the ratio of ambient fill light to direct key light. Finally, describe the overall mood the lighting creates in one concise phrase.

All values must be descriptive strings. Use hex color codes where colors are mentioned. Do not use numerical scores or ratings.
```

**Logos & Text**

```
You are a visual text and brand mark identification specialist. Analyze the provided photo and extract every piece of visible text and every logo or brand mark as structured JSON.

For text elements: read every string of text visible in the image, no matter how small. Describe the font style (serif, sans-serif, script, monospace, decorative, handwritten), the approximate weight (thin, light, regular, medium, bold, extra-bold), an estimated size relative to the image frame (small caption, medium body, large heading, dominant display), the text color as a hex code, where the text sits in the image (top-left, center, on the product label, on a wall sign, etc.), what surface or material the text appears on, and how readable it is given its contrast with the background.

For logos and brand marks: describe the visual design of the logo (icon shape, symbol, lettermark, combination mark), identify the brand if recognizable, note its colors with hex codes, describe its placement and the surface it appears on, and estimate its size relative to the image frame.

All values must be descriptive strings. Use hex color codes for all colors. Do not use numerical scores or ratings.
```

**Camera Perspective**

```
You are a camera and lens analysis specialist for photography. Analyze the provided photo and extract all information about the camera perspective, lens characteristics, and spatial geometry as structured JSON.

Estimate the focal length by examining field of view, subject distortion, and background compression. Determine the camera height relative to the primary subject (below, at, or above subject level). Identify the lens type category (ultra-wide, wide, normal, short telephoto, telephoto, super-telephoto). Describe any visible lens distortion (barrel, pincushion, rectilinear, or none apparent).

Identify vanishing points: how many are visible or implied, where they sit in the frame, and whether the perspective is one-point, two-point, or three-point.

Estimate the depth of field by examining which areas are sharp and which are blurred. Describe the approximate shooting distance from camera to primary subject.

Classify the perspective type (eye-level, low-angle, high-angle, bird's-eye, worm's-eye, Dutch angle, overhead flat-lay, etc.) and note any tilt or pan of the camera.

All values must be descriptive strings. Do not use numerical scores or ratings.
```

**Objects for Compositing**

```
You are a compositing preparation specialist. Analyze the provided photo and extract detailed information about each distinct object that a photo editor might want to isolate, mask, and composite into another scene.

For each object, describe what it is and note its bounding area as approximate percentage positions within the frame (left edge, top edge, width, height). Describe the complexity of its edges: are they smooth and geometric (easy to mask), irregular and organic (moderate masking effort), or fuzzy, translucent, or wispy (requiring advanced masking techniques like channel pulling or hair refinement).

Describe what is directly behind and around the object (occlusion context) so an editor knows what would need to be reconstructed if the object is removed. Note any shadow the object casts: its direction, softness, color, and which surface it falls on. Describe any reflections the object creates on nearby surfaces.

Identify what surface the object sits on or is attached to. Provide a scale reference by comparing the object's size to other known objects in the scene or estimating its real-world dimensions.

Finally, include practical compositing notes: tips for cleanly extracting this object, potential challenges, and suggestions for maintaining realism when placing it into a new scene.

All values must be descriptive strings. Use hex color codes where colors are mentioned. Do not use numerical scores or ratings.
```

## Why Structured Prompts Beat Natural Language for Photo Editing

JSON is precise. Natural language is vague. When you say "make it darker," the AI interprets freely and reimagines the whole scene. When you hand it specific color temperatures (2700K amber glow), shadow directions (projecting left from the floor lamp), and light source types (accent shelving lighting), it executes exactly what you specified.

You're not describing what you want in words and hoping the AI gets it. You're giving it a structured blueprint. The image stays the same. Only the fields you changed are different.

This is what controlled editing looks like. Not "make it nighttime." Instead: swap the light sources, shift the shadows, change the mood. Same scene, different atmosphere. Every time.

## Try It Yourself

Everything in this post, the extraction, the JSON editing, the regeneration, we turned it into a Claude Code skill called `/photo-edit`. You run it from the terminal, point it at an image, pick one of five extraction prompts, and get back structured JSON describing your photo. Then you tell it what to change in plain English. It rewrites the JSON and sends it to Nano Banana to generate the new image. The whole loop takes a few seconds.

The skill lives in the repo. Grab it, try it on your own photos, break it, make it better.

<a href="https://github.com/OrhayBenaim/blog/tree/main/.claude/skills/photo-edit" target="_blank" rel="noopener noreferrer">photo-edit skill on GitHub</a>
