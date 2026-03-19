# Photo Analysis Extraction Prompts

Specialized prompts for extracting structured features from photos as JSON. Designed for photo editing and compositing workflows.

---

## PROMPT 0: General Scene & Objects

### Instruction Prompt

Analyze the interior design image and convert all visual information into highly detailed structured JSON format. Focus specifically on isolating individual objects and lighting placements. For each key object, extract its precise colour (using descriptive names or hex codes) and its exact material (eg. matte leather, brushed steel, oak wood). Include JSON keys for 'room_style', 'overall_colour_palette', and an 'object' array containing 'name','colour','material', 'position_in_room' and 'lighting_position'. Output ONLY valid JSON and format the output as a copyable JSON code block using Markdown.

### Example JSON Output

```json
{
  "room_style": "Transitional Rustic / Organic Modern",
  "overall_colour_palette": [
    "Warm Beige (#E8E4D9)",
    "Natural Tan (#D2B48C)",
    "Rustic Brown (#6b4423)",
    "Charcoal Grey (#36454F)",
    "Leaf Green (#4A5D23)",
    "Soft White (#F8F8F8)",
    "Matte Black (#1C1C1C)"
  ],
  "objects": [
    {
      "name": "L-Shaped Sectional Sofa",
      "colour": "Warm Beige / Oatmeal",
      "material": "Textured Linen or Heavy Woven Cotton",
      "position_in_room": "Dominating the left to center of the room space",
      "lighting_position": "Illuminated by natural daylight from the windows located behind and to its left"
    },
    {
      "name": "Coffee Table",
      "colour": "Rustic Medium Brown",
      "material": "Distressed Reclaimed Wood (Likely Pine or Oak)",
      "position_in_room": "Center foreground, placed over the rug parallel to the sofa",
      "lighting_position": "Top-lit by diffused natural room light, casting soft shadows directly underneath onto the rug"
    }
  ]
}
```

---

## PROMPT 1: Lighting & Time of Day

### Instruction Prompt

You are a lighting analysis specialist for photography. Analyze the provided photo and extract all lighting information as structured JSON.

Examine every visible and inferred light source in the image. For each light source, describe its type (natural sunlight, overcast sky, tungsten lamp, fluorescent panel, neon sign, candle, etc.), the direction it comes from relative to the camera, its approximate color temperature as a descriptive label and Kelvin estimate, and its intensity relative to other sources in the scene.

Describe the shadows in the image: their direction, how soft or hard their edges are, their approximate length relative to the objects casting them, and their color tint.

Estimate the time of day based on light angle, color, and shadow behavior. Describe weather or atmospheric conditions that affect the light (overcast, haze, fog, clear sky, rain, dust particles catching light, etc.).

Assess the ratio of ambient fill light to direct key light. Finally, describe the overall mood the lighting creates in one concise phrase.

All values must be descriptive strings. Use hex color codes where colors are mentioned. Do not use numerical scores or ratings.

### Example JSON Output

```json
{
  "time_of_day": "Late afternoon, approximately 4:30-5:30 PM based on low sun angle and warm color cast",
  "weather_conditions": "Clear sky with thin high-altitude cirrus clouds, no atmospheric haze at ground level",
  "overall_light_mood": "Warm, nostalgic golden hour with long dramatic shadows",
  "ambient_to_direct_ratio": "Ambient fill is roughly one-third the intensity of the direct key light, creating moderate contrast with visible shadow detail",
  "light_sources": [
    {
      "name": "Direct Sunlight (Key Light)",
      "type": "Natural sunlight, low angle late afternoon",
      "direction": "Coming from camera-left at approximately 30 degrees above the horizon, striking the scene from the west-southwest",
      "color_temperature": "Warm golden, approximately 3500K (#FFB347)",
      "intensity": "Strong and dominant, the primary light source driving all major highlights and shadows",
      "quality": "Semi-hard with defined but not razor-sharp shadow edges due to slight atmospheric diffusion",
      "coverage": "Illuminates the right side of the subject's face and the upper surfaces of all horizontal objects"
    },
    {
      "name": "Open Sky Fill (Ambient)",
      "type": "Natural sky dome, scattered blue light from the opposite side of the sun",
      "direction": "Diffused from above and camera-right, acting as a soft fill on shadow sides",
      "color_temperature": "Cool blue, approximately 7000K (#8DB4D6)",
      "intensity": "Subtle, providing just enough fill to retain detail in shadowed areas without flattening contrast",
      "quality": "Very soft and wraparound, no defined edges",
      "coverage": "Fills shadow areas on the left side of the subject and underside of objects"
    },
    {
      "name": "Ground Bounce",
      "type": "Reflected sunlight bouncing off light-colored sandy ground surface",
      "direction": "Coming from below and slightly in front of the subject",
      "color_temperature": "Neutral warm, approximately 4500K (#F5E6C8)",
      "intensity": "Faint, visible mainly as a slight lift in shadows under the chin and lower facial features",
      "quality": "Very diffused and even",
      "coverage": "Primarily affects the underside of the subject's jawline and the bottom surfaces of nearby objects"
    }
  ],
  "shadows": {
    "primary_direction": "Shadows fall to the right and slightly toward the camera, consistent with low-angle sun from camera-left",
    "edge_softness": "Moderately soft, the penumbra is visible but the shadow core remains well-defined, typical of direct sun partially softened by atmosphere",
    "length": "Long shadows, approximately 2.5 to 3 times the height of the objects casting them, consistent with low sun angle",
    "color_tint": "Shadows carry a cool blue-purple tint (#6B7B8D) from the open sky fill, contrasting with the warm highlights",
    "density": "Semi-transparent, shadow areas retain texture and color detail in the underlying surfaces"
  }
}
```

---

## PROMPT 2: Logos & Text

### Instruction Prompt

You are a visual text and brand mark identification specialist. Analyze the provided photo and extract every piece of visible text and every logo or brand mark as structured JSON.

For text elements: read every string of text visible in the image, no matter how small. Describe the font style (serif, sans-serif, script, monospace, decorative, handwritten), the approximate weight (thin, light, regular, medium, bold, extra-bold), an estimated size relative to the image frame (small caption, medium body, large heading, dominant display), the text color as a hex code, where the text sits in the image (top-left, center, on the product label, on a wall sign, etc.), what surface or material the text appears on, and how readable it is given its contrast with the background.

For logos and brand marks: describe the visual design of the logo (icon shape, symbol, lettermark, combination mark), identify the brand if recognizable, note its colors with hex codes, describe its placement and the surface it appears on, and estimate its size relative to the image frame.

All values must be descriptive strings. Use hex color codes for all colors. Do not use numerical scores or ratings.

### Example JSON Output

```json
{
  "text_elements": [
    {
      "text_string": "COLD BREW COFFEE",
      "font_style": "Sans-serif, geometric, all uppercase with wide letter-spacing",
      "font_weight": "Bold",
      "estimated_size": "Medium heading, occupying roughly 8% of the image width",
      "text_color": "Off-white (#F2F0E8)",
      "placement": "Upper-center of the product label, front-facing on the bottle",
      "surface": "Printed on a matte dark brown paper label wrapped around a glass bottle",
      "readability": "High contrast against the dark label background, fully legible with clean edges"
    },
    {
      "text_string": "12 FL OZ (355 mL)",
      "font_style": "Sans-serif, condensed, uppercase",
      "font_weight": "Regular",
      "estimated_size": "Small caption, very small relative to the frame, roughly 2% of image width",
      "text_color": "Muted tan (#C4B59A)",
      "placement": "Bottom-center of the product label, below the main branding",
      "surface": "Same matte paper label as the main text",
      "readability": "Low contrast against the brown label, legible only on close inspection"
    },
    {
      "text_string": "PORTLAND, OREGON",
      "font_style": "Serif, small caps with generous tracking",
      "font_weight": "Light",
      "estimated_size": "Small, roughly 3% of image width",
      "text_color": "Warm gold (#C9A84C)",
      "placement": "Centered directly beneath the logo mark on the label",
      "surface": "Printed on the same matte paper label",
      "readability": "Moderate, the gold on brown contrast is subtle but readable at close distance"
    }
  ],
  "logos": [
    {
      "brand_name": "Stumptown Coffee Roasters",
      "logo_type": "Combination mark with a stylized illustration above a wordmark",
      "visual_description": "A vintage-style illustration of a woman riding a bicycle, drawn in a single line weight, enclosed in a rough circular frame, positioned above the brand wordmark in serif lettering",
      "colors": [
        "Off-white line art (#F2F0E8)",
        "Dark brown background showing through (#3B2415)"
      ],
      "placement": "Center of the bottle label, serving as the primary visual anchor of the packaging",
      "surface": "Printed on the matte paper product label",
      "estimated_size": "Medium, the logo occupies approximately 15% of the total image area"
    },
    {
      "brand_name": "Unknown / Custom",
      "logo_type": "Small icon mark, appears to be a certification or quality seal",
      "visual_description": "A circular seal with a leaf motif inside, resembling an organic or fair-trade certification badge",
      "colors": [
        "Forest green (#2D5F2D)",
        "White inner detail (#FFFFFF)"
      ],
      "placement": "Lower-right corner of the product label, next to the volume text",
      "surface": "Printed on the matte paper label",
      "estimated_size": "Very small, less than 2% of the image area"
    }
  ]
}
```

---

## PROMPT 3: Camera Perspective

### Instruction Prompt

You are a camera and lens analysis specialist for photography. Analyze the provided photo and extract all information about the camera perspective, lens characteristics, and spatial geometry as structured JSON.

Estimate the focal length by examining field of view, subject distortion, and background compression. Determine the camera height relative to the primary subject (below, at, or above subject level). Identify the lens type category (ultra-wide, wide, normal, short telephoto, telephoto, super-telephoto). Describe any visible lens distortion (barrel, pincushion, rectilinear, or none apparent).

Identify vanishing points: how many are visible or implied, where they sit in the frame, and whether the perspective is one-point, two-point, or three-point.

Estimate the depth of field by examining which areas are sharp and which are blurred. Describe the approximate shooting distance from camera to primary subject.

Classify the perspective type (eye-level, low-angle, high-angle, bird's-eye, worm's-eye, Dutch angle, overhead flat-lay, etc.) and note any tilt or pan of the camera.

All values must be descriptive strings. Do not use numerical scores or ratings.

### Example JSON Output

```json
{
  "focal_length_estimate": "Approximately 35mm equivalent, based on the moderately wide field of view that captures the full room width while showing mild perspective convergence on vertical lines",
  "camera_height": "Slightly below average standing eye level, approximately chest height at around 120cm from the floor, looking slightly upward at the subject",
  "lens_type": "Wide-angle, between 28mm and 40mm equivalent range",
  "perspective_type": "Low-angle eye-level, the camera is positioned lower than the subject's eyes creating a subtle sense of presence and authority",
  "shooting_distance": "Approximately 2.5 to 3 meters from the primary subject, close enough for environmental portrait framing while including substantial room context",
  "depth_of_field": {
    "overall_description": "Moderate depth of field, the subject and objects within roughly one meter in front and behind are acceptably sharp, while the far wall and window details show gentle softening",
    "sharpest_zone": "The subject's face and upper body, positioned roughly one-third into the scene from the camera",
    "near_blur": "Minimal, a coffee table in the immediate foreground shows only very slight softness on its nearest edge",
    "far_blur": "Gradual falloff, the bookshelf on the far wall is noticeably soft but still identifiable, the window frame is slightly softer still",
    "estimated_aperture": "Around f/4 to f/5.6, enough to keep the main subject zone sharp while allowing background separation"
  },
  "vanishing_points": {
    "type": "Two-point perspective",
    "primary_vanishing_point": "Located off-frame to the right, implied by the converging lines of the ceiling beam and floor edge running from left to right",
    "secondary_vanishing_point": "Located off-frame far to the left, implied by the receding wall on the right side of the frame",
    "horizon_line": "Sits at approximately 40% from the top of the frame, consistent with the slightly low camera position"
  },
  "distortion": {
    "type": "Mild barrel distortion",
    "description": "Slight outward bowing visible on the vertical door frame near the left edge of the image, straight lines near center remain true",
    "correction_notes": "Appears to be partially corrected in-camera or via lens profile, residual distortion only visible at the extreme edges"
  },
  "tilt_angle": "Camera is tilted upward approximately 5 to 8 degrees from level, causing mild vertical convergence where the walls lean slightly inward at the top of the frame",
  "pan_angle": "Camera is panned approximately 15 degrees to the left of the room's central axis, placing the subject off-center to the right in the frame"
}
```

---

## PROMPT 4: Object Extraction (for Compositing)

### Instruction Prompt

You are a compositing preparation specialist. Analyze the provided photo and extract detailed information about each distinct object that a photo editor might want to isolate, mask, and composite into another scene.

For each object, describe what it is and note its bounding area as approximate percentage positions within the frame (left edge, top edge, width, height). Describe the complexity of its edges: are they smooth and geometric (easy to mask), irregular and organic (moderate masking effort), or fuzzy, translucent, or wispy (requiring advanced masking techniques like channel pulling or hair refinement).

Describe what is directly behind and around the object (occlusion context) so an editor knows what would need to be reconstructed if the object is removed. Note any shadow the object casts: its direction, softness, color, and which surface it falls on. Describe any reflections the object creates on nearby surfaces.

Identify what surface the object sits on or is attached to. Provide a scale reference by comparing the object's size to other known objects in the scene or estimating its real-world dimensions.

Finally, include practical compositing notes: tips for cleanly extracting this object, potential challenges, and suggestions for maintaining realism when placing it into a new scene.

All values must be descriptive strings. Use hex color codes where colors are mentioned. Do not use numerical scores or ratings.

### Example JSON Output

```json
{
  "scene_description": "A styled desktop workspace shot from a slightly elevated angle, featuring several objects arranged on a light wood surface under soft natural window light",
  "objects": [
    {
      "name": "Ceramic Coffee Mug",
      "description": "A handmade ceramic mug with an uneven matte glaze in speckled cream, filled with dark coffee, slight steam visible above the rim",
      "bounding_area": {
        "left_edge": "62% from left",
        "top_edge": "45% from top",
        "approximate_width": "12% of frame width",
        "approximate_height": "18% of frame height"
      },
      "edge_complexity": "Mostly smooth and geometric along the mug body, clean curves that are straightforward to mask. The handle has a slightly organic shape but remains well-defined. The steam wisps above the rim are translucent and diffuse, requiring careful masking with feathered edges or a luminosity-based selection",
      "occlusion_context": {
        "behind": "Light oak wood desk surface is directly behind and beneath the mug, the wood grain pattern would need to be reconstructed via clone stamp or content-aware fill if the mug is removed",
        "overlapping": "The mug partially overlaps the corner of a closed notebook to its left by approximately 1cm, and the handle slightly overlaps the desk edge"
      },
      "shadow": {
        "direction": "Shadow falls to the right and slightly toward the camera, consistent with window light from the upper-left",
        "softness": "Soft-edged contact shadow directly under the base transitioning to a more diffused cast shadow extending roughly 3cm to the right",
        "color": "Neutral cool grey (#B0B0B0) on the warm wood surface, creating a subtle complementary contrast",
        "surface": "Cast onto the light oak wood desk surface"
      },
      "reflections": "A faint warm reflection of the mug's cream body is visible on the polished surface of the closed laptop screen positioned 15cm to the right, very subtle and only noticeable at close inspection",
      "surface_contact": "Sitting flat on the light oak wood desk, full base contact with no visible gap or tilt",
      "scale_reference": "Standard coffee mug size, approximately 9cm tall and 8cm in diameter, roughly two-thirds the height of the closed notebook beside it",
      "compositing_notes": "The mug body is clean to extract with any pen tool or edge detection method. Match the contact shadow carefully in the target scene as it reveals the light direction. The steam wisps should be extracted separately on their own layer using Screen or Lighten blending mode rather than a hard mask. When placing in a new scene, ensure the light direction comes from the upper-left to match the highlight on the rim and the shadow direction. The warm reflection on the ceramic surface should shift to match the new environment's color palette."
    },
    {
      "name": "Open Hardcover Notebook",
      "description": "A navy blue linen-covered hardcover notebook, open to a page with handwritten notes in blue ink, pages slightly curled at the corners, a fabric ribbon bookmark visible between pages",
      "bounding_area": {
        "left_edge": "30% from left",
        "top_edge": "35% from top",
        "approximate_width": "28% of frame width",
        "approximate_height": "30% of frame height"
      },
      "edge_complexity": "The outer cover edges are straight and geometric, very clean to mask. The open page edges are slightly irregular with natural paper curl, requiring a slightly more careful path. The fabric ribbon bookmark has soft frayed edges at its tip that need a feathered mask",
      "occlusion_context": {
        "behind": "Desk surface visible around all sides of the notebook, the wood grain continues underneath. The right side of the notebook is partially overlapped by the ceramic mug",
        "overlapping": "The notebook sits on top of a partially visible magazine beneath it, the magazine's bottom-right corner extends beyond the notebook's lower edge"
      },
      "shadow": {
        "direction": "Dual shadow: a thin contact shadow all around the base where it meets the desk, plus a slightly lifted shadow on the right side where the open cover raises the pages off the surface",
        "softness": "Contact shadow is very tight and sharp, the elevated cover shadow is softer and wider with approximately 1cm of penumbra",
        "color": "Dark neutral (#7A7A7A) blending into the desk surface",
        "surface": "Cast onto the light oak wood desk and slightly onto the magazine beneath"
      },
      "reflections": "No significant reflections, the matte linen cover and paper surfaces are non-reflective",
      "surface_contact": "Lying flat-open on the desk surface with the spine acting as a central hinge, the right cover slightly elevated by page thickness",
      "scale_reference": "Standard A5 notebook size, approximately 21cm tall and 15cm wide per page when open, roughly the width of a standard laptop trackpad",
      "compositing_notes": "Extract the notebook as a single unit including both open pages and the visible cover. The slight page curl creates a thin shadow line along the inner spine that adds realism and should be preserved. The handwritten text on the pages ties this object to a specific context, so consider whether it needs to be legible or can be slightly blurred in the target scene. The fabric bookmark should be masked separately with soft edges. When compositing, the notebook's flat orientation means it must sit on a horizontal surface, and the light catching the page texture should match the new scene's overhead light angle."
    },
    {
      "name": "Potted Succulent Plant",
      "description": "A small echeveria succulent with dusty sage-green rosette leaves (#8FAE8B) in a minimal white ceramic pot with a matte finish, sitting on a small cork coaster",
      "bounding_area": {
        "left_edge": "10% from left",
        "top_edge": "25% from top",
        "approximate_width": "14% of frame width",
        "approximate_height": "22% of frame height"
      },
      "edge_complexity": "The ceramic pot has clean smooth edges, simple to mask. The succulent leaves have organic but well-defined edges with smooth rounded tips. No fuzzy or translucent elements. The overall silhouette is compact and contained, making this one of the easier objects in the scene to isolate",
      "occlusion_context": {
        "behind": "Clear desk surface behind and on all sides, no objects directly overlapping. A portion of the desk edge and blurred background wall are visible behind the top of the plant",
        "overlapping": "Completely freestanding, no overlap with other objects"
      },
      "shadow": {
        "direction": "Shadow falls to the right, consistent with the window light source from upper-left",
        "softness": "Medium-soft shadow, the edges are diffused but the shadow shape is still clearly readable as a pot silhouette",
        "color": "Cool grey-green (#A0A898) picking up a slight color cast from the succulent leaves above",
        "surface": "Cast onto the cork coaster first, then extending onto the light oak desk surface"
      },
      "reflections": "No reflections, all surfaces are matte",
      "surface_contact": "The ceramic pot sits centered on a round cork coaster, approximately 8cm diameter, which sits flat on the desk",
      "scale_reference": "Small decorative plant, the pot is approximately 7cm tall and 8cm in diameter, the succulent rosette extends about 4cm above the pot rim, the total height is roughly the same as the coffee mug nearby",
      "compositing_notes": "This is a clean extraction target. The compact shape and matte surfaces make masking straightforward. Extract the pot and coaster together as a unit. The succulent's sage-green color is relatively neutral and will sit naturally in most environments. When placing in a new scene, recreate the soft directional shadow and ensure the pot base appears to make solid contact with the target surface. The slight color spill in the shadow is a nice realistic detail worth replicating."
    }
  ]
}
```
