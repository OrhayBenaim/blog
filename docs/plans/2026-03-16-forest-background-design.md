# Forest Background Design

**Date:** 2026-03-16
**Status:** Approved

## Goal

Make the blog more vibrant by adding an AI-generated misty forest background image that blends with the existing Forest Glass color scheme. Two versions for A/B comparison.

## Image Specification

- **Style:** Misty ethereal forest, dappled afternoon sunlight breaking through dense canopy
- **Colors:** Graded to match palette — #344e41, #3a5a40, #588157, #a3b18a
- **Resolution:** 4K (3840x2160), landscape
- **Format:** WebP primary, JPEG fallback
- **Tool:** Nano Banana 2 (Gemini 3.1 Flash Image)
- **Location:** `public/images/forest-bg.webp` and `public/images/forest-bg.jpg`

## Version A — Full Background

Forest image covers entire page behind all content.

- `background-image` layered: dark overlay gradient on top, forest image below
- Overlay: `linear-gradient(rgba(26,46,26,0.65), rgba(26,46,26,0.7))`
- `background-attachment: fixed` for depth (scroll fallback on mobile)
- Glass panels float over the forest — no changes to glass styles

## Version C — Subtle Texture Blend

Forest image used as a faint texture underneath existing gradients.

- Forest applied via `body::before` pseudo-element at `opacity: 0.12–0.20`
- Existing radial/linear gradient system remains on top
- Adds atmospheric depth without affecting readability

## Toggle Mechanism

`data-bg` attribute on `<html>`:
- `data-bg="full"` → Version A
- `data-bg="texture"` → Version C
- No attribute → current gradient-only (fallback)

## Files Modified

| File | Change |
|------|--------|
| `src/layouts/BaseLayout.astro` | Add forest background CSS, pseudo-element, data-bg toggle, mobile fallback |
| `public/images/forest-bg.webp` | New — AI-generated forest image |
| `public/images/forest-bg.jpg` | New — JPEG fallback |

## No Changes To

- Glass panel styles, colors, blur values
- Header, footer, post card components
- Color scheme CSS variables
- Typography or layout
