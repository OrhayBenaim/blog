# Photo Analysis Extraction Prompts

## Prompt 1: General Scene & Objects

Analyze the interior design image and convert all visual information into highly detailed structured JSON format. Focus specifically on isolating individual objects and lighting placements. For each key object, extract its precise colour (using descriptive names or hex codes) and its exact material (eg. matte leather, brushed steel, oak wood). Include JSON keys for 'room_style', 'overall_colour_palette', and an 'object' array containing 'name','colour','material', 'position_in_room' and 'lighting_position'. Output ONLY valid JSON and format the output as a copyable JSON code block using Markdown.

## Prompt 2: Lighting & Time of Day

You are a lighting analysis specialist for photography. Analyze the provided photo and extract all lighting information as structured JSON.

Examine every visible and inferred light source in the image. For each light source, describe its type (natural sunlight, overcast sky, tungsten lamp, fluorescent panel, neon sign, candle, etc.), the direction it comes from relative to the camera, its approximate color temperature as a descriptive label and Kelvin estimate, and its intensity relative to other sources in the scene.

Describe the shadows in the image: their direction, how soft or hard their edges are, their approximate length relative to the objects casting them, and their color tint.

Estimate the time of day based on light angle, color, and shadow behavior. Describe weather or atmospheric conditions that affect the light (overcast, haze, fog, clear sky, rain, dust particles catching light, etc.).

Assess the ratio of ambient fill light to direct key light. Finally, describe the overall mood the lighting creates in one concise phrase.

All values must be descriptive strings. Use hex color codes where colors are mentioned. Do not use numerical scores or ratings.

## Prompt 3: Logos & Text

You are a visual text and brand mark identification specialist. Analyze the provided photo and extract every piece of visible text and every logo or brand mark as structured JSON.

For text elements: read every string of text visible in the image, no matter how small. Describe the font style (serif, sans-serif, script, monospace, decorative, handwritten), the approximate weight (thin, light, regular, medium, bold, extra-bold), an estimated size relative to the image frame (small caption, medium body, large heading, dominant display), the text color as a hex code, where the text sits in the image (top-left, center, on the product label, on a wall sign, etc.), what surface or material the text appears on, and how readable it is given its contrast with the background.

For logos and brand marks: describe the visual design of the logo (icon shape, symbol, lettermark, combination mark), identify the brand if recognizable, note its colors with hex codes, describe its placement and the surface it appears on, and estimate its size relative to the image frame.

All values must be descriptive strings. Use hex color codes for all colors. Do not use numerical scores or ratings.

## Prompt 4: Camera Perspective

You are a camera and lens analysis specialist for photography. Analyze the provided photo and extract all information about the camera perspective, lens characteristics, and spatial geometry as structured JSON.

Estimate the focal length by examining field of view, subject distortion, and background compression. Determine the camera height relative to the primary subject (below, at, or above subject level). Identify the lens type category (ultra-wide, wide, normal, short telephoto, telephoto, super-telephoto). Describe any visible lens distortion (barrel, pincushion, rectilinear, or none apparent).

Identify vanishing points: how many are visible or implied, where they sit in the frame, and whether the perspective is one-point, two-point, or three-point.

Estimate the depth of field by examining which areas are sharp and which are blurred. Describe the approximate shooting distance from camera to primary subject.

Classify the perspective type (eye-level, low-angle, high-angle, bird's-eye, worm's-eye, Dutch angle, overhead flat-lay, etc.) and note any tilt or pan of the camera.

All values must be descriptive strings. Do not use numerical scores or ratings.

## Prompt 5: Objects for Compositing

You are a compositing preparation specialist. Analyze the provided photo and extract detailed information about each distinct object that a photo editor might want to isolate, mask, and composite into another scene.

For each object, describe what it is and note its bounding area as approximate percentage positions within the frame (left edge, top edge, width, height). Describe the complexity of its edges: are they smooth and geometric (easy to mask), irregular and organic (moderate masking effort), or fuzzy, translucent, or wispy (requiring advanced masking techniques like channel pulling or hair refinement).

Describe what is directly behind and around the object (occlusion context) so an editor knows what would need to be reconstructed if the object is removed. Note any shadow the object casts: its direction, softness, color, and which surface it falls on. Describe any reflections the object creates on nearby surfaces.

Identify what surface the object sits on or is attached to. Provide a scale reference by comparing the object's size to other known objects in the scene or estimating its real-world dimensions.

Finally, include practical compositing notes: tips for cleanly extracting this object, potential challenges, and suggestions for maintaining realism when placing it into a new scene.

All values must be descriptive strings. Use hex color codes where colors are mentioned. Do not use numerical scores or ratings.
