---
name: nanobanana
description: Generate images and videos using Nano Banana 2 (Google Gemini 3.1 Flash Image) and Veo 3.1. This skill should be used when the agent needs to generate images from text prompts, create AI-generated visuals or videos, or integrate Nano Banana 2 / Veo 3.1 into a project.
---

# Nano Banana v2 Image & Video Generation

Nano Banana 2 is Google's fast AI image generation model powered by Gemini 3.1 Flash Image. Combined with **Veo 3.1**, it also supports text-to-video and image-to-video generation with native audio.

**Image Model ID:** `gemini-3.1-flash-image-preview`
**Video Model ID:** `veo-3.1-generate-preview`

## CLI Script — ALWAYS USE THIS

**CRITICAL:** Do NOT create new scripts for generation. Use the bundled Python CLI at:
```
.claude/skills/nanobanana/nanobanan.py
```

The script reads `GEMINI_API_KEY` from environment or from `<repo-root>/.env`.

### Image Generation

```bash
# Text-to-image
python .claude/skills/nanobanana/nanobanan.py image \
  --prompt "A photorealistic sunset over mountains" \
  --output output.png \
  --aspect-ratio 16:9 \
  --resolution 2K

# Image editing (pass input image + edit prompt)
python .claude/skills/nanobanana/nanobanan.py image \
  --prompt "Add a rainbow in the sky" \
  --input photo.png \
  --output edited.png

# Image-only response (no text commentary)
python .claude/skills/nanobanana/nanobanan.py image \
  --prompt "A minimalist logo" \
  --output logo.png \
  --text-only
```

**Image options:**
| Flag | Default | Values |
|------|---------|--------|
| `--aspect-ratio` | `1:1` | `1:1`, `1:4`, `1:8`, `2:3`, `3:2`, `3:4`, `4:1`, `4:3`, `4:5`, `5:4`, `8:1`, `9:16`, `16:9`, `21:9` |
| `--resolution` | `1K` | `512`, `1K`, `2K`, `4K` |
| `--text-only` | off | Flag — image-only response |
| `--retries` | `3` | Max retries on rate-limit |
| `--input` | — | Input image path for editing |

### Video Generation

```bash
# Text-to-video
python .claude/skills/nanobanana/nanobanan.py video \
  --prompt "A cinematic slow-motion shot of a dog running through a meadow" \
  --output dog.mp4 \
  --resolution 1080p

# Image-to-video (animate a keyframe)
python .claude/skills/nanobanana/nanobanan.py video \
  --prompt "Camera slowly pans across the scene, petals falling" \
  --input keyframe.png \
  --output animated.mp4

# Portrait video (TikTok/Reels)
python .claude/skills/nanobanana/nanobanan.py video \
  --prompt "A person dancing in a neon-lit alley" \
  --output dance.mp4 \
  --aspect-ratio 9:16
```

**Video options:**
| Flag | Default | Values |
|------|---------|--------|
| `--aspect-ratio` | `16:9` | `16:9`, `9:16` |
| `--resolution` | `1080p` | `720p`, `1080p`, `4k` |
| `--count` | `1` | Number of videos to generate |
| `--retries` | `3` | Max retries on rate-limit |
| `--poll-interval` | `10` | Seconds between polling |
| `--input` | — | Keyframe image for image-to-video |

### Multi-step Pipelines

For multi-step workflows (e.g. generate image then animate it), run multiple CLI calls sequentially:

```bash
# Step 1: Generate keyframe
python .claude/skills/nanobanana/nanobanan.py image \
  --prompt "A serene Japanese garden with cherry blossoms" \
  --output keyframe.png --text-only --resolution 2K

# Step 2: Animate it
python .claude/skills/nanobanana/nanobanan.py video \
  --prompt "Camera pans across the garden, petals gently falling" \
  --input keyframe.png --output garden.mp4
```

For concatenating multiple videos, use ffmpeg after generation:
```bash
# Create a file list
printf "file 'video1.mp4'\nfile 'video2.mp4'\nfile 'video3.mp4'" > list.txt
ffmpeg -y -f concat -safe 0 -i list.txt -c copy final.mp4
```

## Prompting Best Practices

Refer to `references/prompting-guide.md` for detailed strategies. Key principles:

- **Be specific** — include style, lighting, composition, subject details
- **Text in images** — put desired text in quotes, specify positioning
- **Limit text elements** to 3-5 per image
- **Aspect ratio selection:**
  - Social media: `1:1` (feed), `9:16` (stories/reels), `16:9` (YouTube)
  - Marketing: `16:9` or `21:9` (heroes)
  - Mobile screens: `9:16`

## Video Notes

- Generation takes ~1-2 minutes (script polls automatically)
- Veo 3.1 generates **native audio** (dialogue, SFX, ambient)
- Videos are 8 seconds long
- Rate limits apply — the script auto-retries on 429s

## For SDK Integration (rare)

If the user explicitly asks to integrate Nano Banana into their codebase (not just generate images), use the Python SDK `google-genai`. See the CLI script source for patterns:
```
.claude/skills/nanobanana/nanobanan.py
```
