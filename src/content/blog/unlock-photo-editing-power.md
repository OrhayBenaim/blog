---
title: "AI Photo Editing with Structured Prompts: Edit What You Want, Keep the Rest"
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

## Four JSON Extraction Prompts for Any Photo

Lighting is just one dimension. There are four specialized extraction prompts, each designed to break down a different aspect of any photo into structured, editable JSON.

**Lighting & Time of Day** captures every light source in the scene with its direction, color temperature, and intensity. It maps shadow behavior, estimates the time of day, and reads the overall mood. You've already seen this one in action above.

**Logos & Text** finds every visible text string and brand mark in the image. It pulls font styles, colors, exact placement, and the surface each element sits on. Useful when you want to swap branding or change copy on a product shot.

```json
{
  "text_elements": [
    {
      "text_string": "COLD BREW COFFEE",
      "font_style": "Sans-serif, geometric, all uppercase",
      "text_color": "Off-white (#F2F0E8)",
      "placement": "Upper-center of the product label"
    }
  ],
  "logos": [
    {
      "brand_name": "Stumptown Coffee Roasters",
      "logo_type": "Combination mark with illustration above wordmark",
      "placement": "Center of the bottle label"
    }
  ]
}
```

**Camera Perspective** breaks down the virtual camera setup. Focal length, lens type, camera height, depth of field, vanishing points, and any distortion. When you need to match a photo's perspective for compositing or recreate a specific cinematic look, this is what you reach for.

```json
{
  "focal_length_estimate": "Approximately 35mm equivalent",
  "lens_type": "Wide-angle",
  "perspective_type": "Low-angle eye-level",
  "depth_of_field": {
    "sharpest_zone": "Subject's face and upper body",
    "estimated_aperture": "Around f/4 to f/5.6"
  },
  "vanishing_points": {
    "type": "Two-point perspective",
    "horizon_line": "At approximately 40% from the top of the frame"
  }
}
```

**Objects for Compositing** catalogs every object in the scene with its bounding area, edge complexity, occlusion context, and shadow information. It even includes compositing tips for each object. This one is gold when you need to isolate, move, or replace specific elements.

```json
{
  "objects": [
    {
      "name": "Ceramic Coffee Mug",
      "bounding_area": {
        "left_edge": "62% from left",
        "approximate_width": "12% of frame width"
      },
      "edge_complexity": "Smooth and geometric, straightforward to mask",
      "shadow": {
        "direction": "Falls to the right",
        "softness": "Soft-edged contact shadow"
      },
      "compositing_notes": "Match the contact shadow in the target scene. Steam wisps should use Screen blending mode."
    }
  ]
}
```

## Why Structured Prompts Beat Natural Language for Photo Editing

JSON is precise. Natural language is vague. When you say "make it darker," the AI interprets freely and reimagines the whole scene. When you hand it specific color temperatures (2700K amber glow), shadow directions (projecting left from the floor lamp), and light source types (accent shelving lighting), it executes exactly what you specified.

You're not describing what you want in words and hoping the AI gets it. You're giving it a structured blueprint. The image stays the same. Only the fields you changed are different.

This is what controlled editing looks like. Not "make it nighttime." Instead: swap the light sources, shift the shadows, change the mood. Same scene, different atmosphere. Every time.
