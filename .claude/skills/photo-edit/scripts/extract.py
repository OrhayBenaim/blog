#!/usr/bin/env python3
"""
Extract features from an image as structured JSON using Gemini Flash.

Usage:
  python extract.py --input photo.jpg --prompt "extraction prompt text"

Environment:
  GEMINI_API_KEY  Required.
"""

import argparse
import base64
import os
import sys

from google import genai
from google.genai import types


def get_client():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        candidate_paths = [
            os.path.join(os.getcwd(), ".env"),
            os.path.join(script_dir, ".env"),
            os.path.join(os.getcwd(), ".claude", "skills", "photo-edit", ".env"),
        ]
        for env_path in candidate_paths:
            if os.path.exists(env_path):
                with open(env_path) as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith("GEMINI_API_KEY="):
                            api_key = line.split("=", 1)[1].strip().strip("'\"")
                            break
            if api_key:
                break
    if not api_key:
        print("Error: GEMINI_API_KEY not set and not found in .env", file=sys.stderr)
        sys.exit(1)
    return genai.Client(api_key=api_key)


def main():
    parser = argparse.ArgumentParser(description="Extract image features as JSON")
    parser.add_argument("--input", required=True, help="Input image path")
    parser.add_argument("--prompt", required=True, help="Extraction prompt")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: File not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    client = get_client()

    with open(args.input, "rb") as f:
        image_data = f.read()

    ext = os.path.splitext(args.input)[1].lower()
    mime_map = {
        ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
        ".png": "image/png", ".webp": "image/webp",
        ".gif": "image/gif", ".bmp": "image/bmp",
    }
    mime_type = mime_map.get(ext, "image/jpeg")

    prompt = args.prompt + "\n\nReturn ONLY valid JSON. No markdown formatting, no code blocks, just raw JSON."

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            types.Content(parts=[
                types.Part(inline_data=types.Blob(mime_type=mime_type, data=image_data)),
                types.Part(text=prompt),
            ])
        ],
    )

    text = response.text.strip()
    # Strip markdown code fences if present
    if text.startswith("```"):
        lines = text.split("\n")
        lines = lines[1:]  # remove opening fence
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]  # remove closing fence
        text = "\n".join(lines)

    print(text)


if __name__ == "__main__":
    main()
