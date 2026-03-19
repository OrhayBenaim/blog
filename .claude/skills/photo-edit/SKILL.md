---
name: photo-edit
description: Interactive photo editing workflow using structured JSON extraction prompts. Extract features from a photo as JSON (via Gemini), modify specific fields, and regenerate with Nano Banana. This skill should be used when the user wants to edit a photo by extracting and modifying its properties (lighting, objects, text, camera angle), or mentions "photo-edit", "extract features from image", "change lighting in photo", "swap object in photo", or "structured photo editing".
---

# Photo Edit - Structured JSON Photo Editing

Edit photos with surgical precision by extracting features as structured JSON, modifying specific fields, and regenerating with the changes applied.

## How It Works

1. User provides an image (or skill asks for one)
2. User picks an extraction prompt
3. Gemini extracts features as JSON
4. User says what to change
5. Skill modifies the JSON and regenerates via Nano Banana

## Step 1: Get the Image

Check if the user provided an image path as an argument when invoking the skill. If yes, verify the file exists. If no argument was provided, ask the user for the image path.

## Step 2: Choose Extraction Prompt

Present the five options and ask the user to pick one:

1. **General Scene & Objects** - Room style, color palette, every object with color, material, position
2. **Lighting & Time of Day** - Light sources, shadows, color temperatures, time of day, mood
3. **Logos & Text** - All visible text strings, fonts, logos, brand marks
4. **Camera Perspective** - Focal length, lens type, depth of field, vanishing points, distortion
5. **Objects for Compositing** - Per-object bounding areas, edge complexity, shadows, compositing tips

Load the selected prompt text from `references/prompts.md` (search for the prompt number heading, e.g. "## Prompt 2").

## Step 3: Extract Features

Use the bundled extraction script (Gemini 2.0 Flash, cheap and fast for vision analysis):

```bash
python .claude/skills/photo-edit/scripts/extract.py \
  --input "<image_path>" \
  --prompt "<extraction_prompt_text>"
```

This sends the image to Gemini Flash and returns structured JSON to stdout. Parse the output and display it to the user.

If the script fails or returns invalid JSON, ask the user to paste the JSON manually (they may have extracted it from Gemini directly).

## Step 4: Ask What to Change

Ask the user what they want to modify. The user describes changes in natural language, for example:
- "Make it nighttime"
- "Change the sofa to olive green velvet"
- "Swap the text to say PREMIUM ROAST"
- "Shift to a bird's eye camera angle"

Apply the requested changes to the JSON. Show the user exactly which fields changed and the new values. Do NOT ask for confirmation, just proceed to regeneration.

## Step 5: Regenerate

Send the original image plus the modified JSON to Nano Banana:

```bash
python .claude/skills/nanobanana/nanobanan.py image \
  --input "<original_image_path>" \
  --prompt "Modify the image following this JSON: <modified_json>" \
  --output "<output_path>" \
  --resolution 2K
```

Output path: same directory as the input, with `-edited` appended to the filename (e.g. `photo-edited.png`). If the file already exists, append a number (e.g. `photo-edited-2.png`).

After generation, display the output path to the user and read/show the generated image.

## Step 6: Iterate

Ask if the user wants to:
- Make more changes (go back to Step 4 with the same JSON)
- Try a different extraction type (go back to Step 2)
- Done

## Rules

- Never modify the original image file
- Always show changed JSON fields before regenerating
- The regeneration prompt is always: "Modify the image following this JSON:" followed by the full modified JSON
- Keep the original image path for all regeneration passes (always edit from the original, not from previous edits)
