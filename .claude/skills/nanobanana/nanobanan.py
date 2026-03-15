#!/usr/bin/env python3
"""
Nano Banana v2 — CLI for image & video generation via Google Gemini / Veo.

Usage:
  python nanobanan.py image  --prompt "..." --output out.png [options]
  python nanobanan.py video  --prompt "..." --output out.mp4 [options]

Options (image):
  --input FILE          Input image for editing (optional)
  --aspect-ratio RATIO  e.g. 1:1, 9:16, 16:9 (default: 1:1)
  --resolution RES      512, 1K, 2K, 4K (default: 1K)
  --text-only           Return only image, no text response
  --retries N           Max retries on rate-limit (default: 3)

Options (video):
  --input FILE          Keyframe image for image-to-video (optional)
  --extend FILE         Previous video file to extend (optional, NOT YET SUPPORTED by SDK file upload)
  --aspect-ratio RATIO  16:9 or 9:16 (default: 16:9)
  --resolution RES      720p, 1080p, 4k (default: 1080p)
  --count N             Number of videos to generate (default: 1)
  --retries N           Max retries on rate-limit (default: 3)
  --poll-interval SECS  Seconds between polls (default: 10)

Environment:
  GEMINI_API_KEY        Required. Get from https://aistudio.google.com/apikey
"""

import argparse
import base64
import os
import sys
import time

from google import genai
from google.genai import types


def get_client():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        # Try loading from .env in repo root
        env_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", ".env")
        if os.path.exists(env_path):
            with open(env_path) as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("GEMINI_API_KEY="):
                        api_key = line.split("=", 1)[1].strip().strip("'\"")
                        break
    if not api_key:
        print("Error: GEMINI_API_KEY not set and not found in .env", file=sys.stderr)
        sys.exit(1)
    return genai.Client(api_key=api_key)


def with_retry(fn, max_retries=3):
    for attempt in range(1, max_retries + 1):
        try:
            return fn()
        except Exception as e:
            msg = str(e)
            if ("429" in msg or "RESOURCE_EXHAUSTED" in msg) and attempt < max_retries:
                wait = 40 * attempt
                print(f"  Rate limited. Waiting {wait}s before retry {attempt}/{max_retries}...")
                time.sleep(wait)
            else:
                raise


def cmd_image(args):
    client = get_client()
    print(f"Generating image -> {args.output}")

    modalities = ["IMAGE"] if args.text_only else ["TEXT", "IMAGE"]

    contents = args.prompt
    if args.input:
        with open(args.input, "rb") as f:
            img_bytes = f.read()
        contents = [
            types.Part.from_text(text=args.prompt),
            types.Part.from_bytes(data=img_bytes, mime_type=_mime(args.input)),
        ]

    def generate():
        return client.models.generate_content(
            model="gemini-3.1-flash-image-preview",
            contents=contents,
            config=types.GenerateContentConfig(
                response_modalities=modalities,
                image_config=types.ImageConfig(
                    aspect_ratio=args.aspect_ratio,
                    image_size=args.resolution,
                ),
            ),
        )

    response = with_retry(generate, args.retries)

    for part in response.candidates[0].content.parts:
        if part.text:
            print(f"  Model text: {part.text}")
        elif part.inline_data:
            data = part.inline_data.data
            if isinstance(data, str):
                data = base64.b64decode(data)
            with open(args.output, "wb") as f:
                f.write(data)
            print(f"  Saved: {args.output} ({len(data)} bytes)")


def cmd_video(args):
    client = get_client()
    print(f"Generating video -> {args.output}")

    kwargs = {
        "model": "veo-3.1-generate-preview",
        "prompt": args.prompt,
        "config": types.GenerateVideosConfig(
            aspect_ratio=args.aspect_ratio,
            number_of_videos=args.count,
            resolution=args.resolution,
        ),
    }

    if args.input:
        with open(args.input, "rb") as f:
            img_bytes = f.read()
        kwargs["image"] = types.Image(
            image_bytes=base64.b64encode(img_bytes).decode(),
            mime_type=_mime(args.input),
        )

    def generate():
        return client.models.generate_videos(**kwargs)

    operation = with_retry(generate, args.retries)

    attempts = 0
    while not operation.done:
        attempts += 1
        print(f"  Polling... (attempt {attempts})")
        time.sleep(args.poll_interval)
        operation = client.operations.get_videos_operation(operation=operation)

    for i, vid in enumerate(operation.response.generated_videos):
        out = args.output if args.count == 1 else args.output.replace(".mp4", f"-{i}.mp4")
        client.files.download(file=vid.video, download_path=out)
        print(f"  Saved: {out}")


def _mime(path):
    ext = os.path.splitext(path)[1].lower()
    return {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
        ".gif": "image/gif",
    }.get(ext, "image/png")


def main():
    parser = argparse.ArgumentParser(description="Nano Banana v2 — Image & Video Generation CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    # ── image ──
    img = sub.add_parser("image", help="Generate or edit an image")
    img.add_argument("--prompt", required=True, help="Text prompt")
    img.add_argument("--output", required=True, help="Output file path (.png)")
    img.add_argument("--input", help="Input image for editing")
    img.add_argument("--aspect-ratio", default="1:1", help="Aspect ratio (default: 1:1)")
    img.add_argument("--resolution", default="1K", help="Resolution: 512, 1K, 2K, 4K (default: 1K)")
    img.add_argument("--text-only", action="store_true", help="Image-only response, no text")
    img.add_argument("--retries", type=int, default=3, help="Max retries on rate-limit")

    # ── video ──
    vid = sub.add_parser("video", help="Generate a video")
    vid.add_argument("--prompt", required=True, help="Text prompt")
    vid.add_argument("--output", required=True, help="Output file path (.mp4)")
    vid.add_argument("--input", help="Keyframe image for image-to-video")
    vid.add_argument("--aspect-ratio", default="16:9", help="Aspect ratio: 16:9 or 9:16")
    vid.add_argument("--resolution", default="1080p", help="Resolution: 720p, 1080p, 4k")
    vid.add_argument("--count", type=int, default=1, help="Number of videos (default: 1)")
    vid.add_argument("--retries", type=int, default=3, help="Max retries on rate-limit")
    vid.add_argument("--poll-interval", type=int, default=10, help="Poll interval in seconds")

    args = parser.parse_args()

    if args.command == "image":
        cmd_image(args)
    elif args.command == "video":
        cmd_video(args)

    print("\nDone!")


if __name__ == "__main__":
    main()
