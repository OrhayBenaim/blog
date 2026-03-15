# Forest Background Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add a vibrant AI-generated misty forest background image with two CSS modes (full background vs subtle texture) for A/B comparison.

**Architecture:** Generate a 4K forest image via Nano Banana, save as WebP+JPEG in `public/images/`, then add CSS to `BaseLayout.astro` with a `data-bg` attribute toggle on `<html>` to switch between "full" and "texture" modes. No changes to glass panel styles, components, or color variables.

**Tech Stack:** Astro, CSS (pseudo-elements, layered backgrounds), Nano Banana 2 (image generation)

---

### Task 1: Generate Forest Background Image

**Files:**
- Create: `public/images/forest-bg.png` (raw output from Nano Banana)

**Step 1: Generate the image using nanobanana skill**

Use the `nanobanana` skill with this prompt:

```
A 4K ultra-wide misty ethereal forest photograph, dappled afternoon sunlight breaking through a dense canopy of tall ancient trees, patches of golden-green light filtering through leaves creating light rays in the mist, soft fog weaving between moss-covered tree trunks, deep forest green color palette dominated by #344e41 #3a5a40 #588157 tones with muted sage #a3b18a highlights, photorealistic, atmospheric perspective with depth, cinematic composition, no people, no text, no UI elements. Landscape orientation.
```

Options: 4K resolution, landscape aspect ratio.

Save output to `public/images/forest-bg.png`.

**Step 2: Verify the image**

Run: `ls -la public/images/forest-bg.png`
Expected: File exists with reasonable size (1-5MB)

**Step 3: Commit**

```bash
git add public/images/forest-bg.png
git commit -m "feat: add AI-generated misty forest background image"
```

---

### Task 2: Convert Image to WebP and JPEG

**Files:**
- Create: `public/images/forest-bg.webp`
- Create: `public/images/forest-bg.jpg`
- Delete: `public/images/forest-bg.png` (raw file no longer needed)

**Step 1: Install sharp-cli if needed and convert**

```bash
npx sharp-cli -i public/images/forest-bg.png -o public/images/forest-bg.webp --format webp --quality 80
npx sharp-cli -i public/images/forest-bg.png -o public/images/forest-bg.jpg --format jpeg --quality 85
```

If sharp-cli is not available, use ImageMagick or any available converter:
```bash
magick public/images/forest-bg.png -quality 80 public/images/forest-bg.webp
magick public/images/forest-bg.png -quality 85 public/images/forest-bg.jpg
```

**Step 2: Verify both files exist**

Run: `ls -la public/images/forest-bg.*`
Expected: `.webp` and `.jpg` files, both under 1MB ideally.

**Step 3: Remove raw PNG**

```bash
rm public/images/forest-bg.png
```

**Step 4: Commit**

```bash
git add public/images/forest-bg.webp public/images/forest-bg.jpg
git add -u public/images/forest-bg.png
git commit -m "feat: add optimized WebP and JPEG forest background"
```

---

### Task 3: Add Version A CSS (Full Background)

**Files:**
- Modify: `src/layouts/BaseLayout.astro:11` (add `data-bg` attribute to `<html>`)
- Modify: `src/layouts/BaseLayout.astro:71-82` (add Version A styles after body styles)

**Step 1: Add `data-bg="full"` attribute to the `<html>` tag**

In `src/layouts/BaseLayout.astro`, change line 12:

```html
<!-- FROM -->
<html lang="en">

<!-- TO -->
<html lang="en" data-bg="full">
```

This sets Version A as the initial default for testing.

**Step 2: Add Version A CSS rules after the existing `body` block (after line 82)**

Insert after the `body { ... }` closing brace (line 82), before the `a {` rule:

```css
/* Forest background — Version A: Full background */
html[data-bg="full"] body {
  background-image:
    linear-gradient(to bottom, rgba(26, 46, 26, 0.6) 0%, rgba(26, 46, 26, 0.7) 100%),
    url('/blog/images/forest-bg.webp');
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
}

/* Mobile fallback — fixed attachment not supported on iOS/Android */
@supports (-webkit-touch-callout: none) {
  html[data-bg="full"] body {
    background-attachment: scroll;
  }
}
```

**Step 3: Verify it builds**

Run: `cd /c/Users/Orhay/git/blog && npm run build`
Expected: Build succeeds with no errors.

**Step 4: Commit**

```bash
git add src/layouts/BaseLayout.astro
git commit -m "feat: add Version A full forest background with dark overlay"
```

---

### Task 4: Add Version C CSS (Subtle Texture Blend)

**Files:**
- Modify: `src/layouts/BaseLayout.astro` (add Version C styles after Version A block)

**Step 1: Add Version C CSS rules after the Version A block**

Insert after the Version A `@supports` block:

```css
/* Forest background — Version C: Subtle texture blend */
html[data-bg="texture"] body {
  position: relative;
}

html[data-bg="texture"] body::before {
  content: '';
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url('/blog/images/forest-bg.webp');
  background-size: cover;
  background-position: center;
  opacity: 0.15;
  z-index: -1;
  pointer-events: none;
}
```

Note: In Version C, the existing `body` background (gradients) stays untouched. The forest image sits behind everything at low opacity via the `::before` pseudo-element.

**Step 2: Verify it builds**

Run: `cd /c/Users/Orhay/git/blog && npm run build`
Expected: Build succeeds with no errors.

**Step 3: Commit**

```bash
git add src/layouts/BaseLayout.astro
git commit -m "feat: add Version C subtle texture forest background"
```

---

### Task 5: Test Both Versions with Screenshots

**Step 1: Start dev server**

Run: `cd /c/Users/Orhay/git/blog && npm run dev`
(Keep running in background)

**Step 2: Screenshot Version A (full background)**

Ensure `<html>` has `data-bg="full"`, then:

```bash
agent-browser open http://localhost:4321/blog/ && agent-browser wait --load networkidle && agent-browser screenshot --full /tmp/version-a-home.png
agent-browser open http://localhost:4321/blog/posts/hello-world/ && agent-browser wait --load networkidle && agent-browser screenshot --full /tmp/version-a-post.png
```

View both screenshots to verify:
- Forest image visible behind dark overlay
- Glass panels readable and intact
- No layout breakage

**Step 3: Switch to Version C and screenshot**

Change `data-bg="full"` to `data-bg="texture"` in `BaseLayout.astro` line 12, then:

```bash
agent-browser open http://localhost:4321/blog/ && agent-browser wait --load networkidle && agent-browser screenshot --full /tmp/version-c-home.png
agent-browser open http://localhost:4321/blog/posts/hello-world/ && agent-browser wait --load networkidle && agent-browser screenshot --full /tmp/version-c-post.png
```

View both screenshots to verify:
- Subtle forest texture visible beneath gradients
- Existing gradient colors still dominant
- Readability unchanged

**Step 4: Present both versions to user for comparison**

Show all four screenshots side by side (Version A home + post, Version C home + post) and ask which they prefer or if adjustments are needed.

**Step 5: Close browser and stop dev server**

```bash
agent-browser close
```

**Step 6: Commit final state**

```bash
git add src/layouts/BaseLayout.astro
git commit -m "feat: set default background version after A/B comparison"
```
