# Securing AI-Built Apps - Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Write and publish a blog post about securing applications built with AI, covering API key exposure, RLS pitfalls, auth solutions, context slop, and the security audit skill.

**Architecture:** Astro markdown blog post with nanobanana-generated images (WebP), following existing post conventions. Images stored in `public/blog/`, post in `src/content/blog/`.

**Tech Stack:** Astro, Markdown, nanobanana skill for image generation, sharp/image-optimizer for WebP conversion.

---

### Task 1: Generate Hero Image

**Files:**
- Create: `public/blog/blog/securing-ai-apps-hero.webp`

**Step 1: Generate image with nanobanana skill**

Use the nanobanana skill to generate an image. Prompt concept: a robot building an app/house with a visible open back door or security vulnerability. Futuristic, slightly ominous tone. Should work well as a blog hero image.

**Step 2: Optimize to WebP**

Use the image-optimizer skill to convert to WebP if not already. Save to `public/blog/blog/securing-ai-apps-hero.webp`.

**Step 3: Commit**

```bash
git add public/blog/blog/securing-ai-apps-hero.webp
git commit -m "feat: add hero image for securing AI apps post"
```

---

### Task 2: Generate Section Images

**Files:**
- Create: `public/blog/blog/securing-ai-apps-keys.webp`
- Create: `public/blog/blog/securing-ai-apps-corners.webp`

**Step 1: Generate API keys image with nanobanana**

Prompt concept: an open vault or exposed keys, digital/cyber aesthetic. For the "Your API Keys Are Showing" section.

**Step 2: Generate round-cornering image with nanobanana**

Prompt concept: AI taking shortcuts around a security wall, cutting corners. For the "Context Slop and Round-Cornering" section.

**Step 3: Optimize both to WebP**

Use image-optimizer skill. Save to `public/blog/blog/securing-ai-apps-keys.webp` and `public/blog/blog/securing-ai-apps-corners.webp`.

**Step 4: Commit**

```bash
git add public/blog/blog/securing-ai-apps-keys.webp public/blog/blog/securing-ai-apps-corners.webp
git commit -m "feat: add section images for securing AI apps post"
```

---

### Task 3: Write the Blog Post

**Files:**
- Create: `src/content/blog/securing-ai-apps.md`

**Step 1: Create the blog post file**

Write the full markdown blog post following the design doc at `docs/plans/2026-03-16-securing-ai-apps-design.md`.

Frontmatter format (match existing posts exactly):
```yaml
---
title: "Your AI-Built App Is Probably Not Secure"
description: "AI builds things that work, but working and secure aren't the same thing. Here's where AI-generated code cuts corners on security and how to fix it."
pubDate: 2026-03-16
tags: ["security", "ai", "supabase", "firebase", "rls"]
---
```

Writing conventions:
- No em dashes (per user feedback memory)
- Conversational but practical tone
- External links use `<a href="..." target="_blank" rel="noopener noreferrer">` format
- Images use `![alt text](/blog/blog/filename.webp)` format
- Code blocks use triple backticks with language identifier (sql, javascript, etc.)
- Keep code examples short, not full copy-paste snippets

Sections to write (see design doc for full details):

1. **Hook** (~150w) - Scenario of role escalation + core message + hero image
2. **Your API Keys Are Showing** (~200w) - Service_role in client, short code example + keys image
3. **The Anon Key Trap** (~200w) - Anon key + poor RLS = wide open
4. **RLS Looks Right But Isn't** (~350w) - Role escalation example, bad vs better RLS policy
5. **Stop Rolling Your Own Auth** (~200w) - Recommend battle-tested solutions with links:
   - better-auth: `https://www.better-auth.com/`
   - Auth.js: `https://authjs.dev/`
   - Supabase Auth (mention, no external link needed)
   - Firebase Authentication (mention, no external link needed)
6. **Context Slop & Round-Cornering** (~250w) - Explain both concepts + prompt examples:
   - Bad: "user need to be able to see their data in the dashboard."
   - Good: "user need to be able to see their data in the dashboard, we need to setup the correct rls using user id."
   - Add corners image
7. **Security Audit Skill** (~120w) - Bullet points of what it does + link to the skill
8. **Closing** (~100w) - Core takeaway + link to skill again

**Step 2: Verify the post renders**

Run: `npx astro build`
Expected: Build succeeds with no errors.

**Step 3: Commit**

```bash
git add src/content/blog/securing-ai-apps.md
git commit -m "feat: add blog post on securing AI-built applications"
```

---

### Task 4: Local Preview and Polish

**Step 1: Start dev server**

Run: `npx astro dev`

**Step 2: Preview the post in browser**

Check at `http://localhost:4321/blog/securing-ai-apps/`. Verify:
- All 3 images load correctly
- Code blocks render with syntax highlighting
- External links open in new tabs
- Post reads well and flows logically
- No broken formatting

**Step 3: Fix any issues found**

**Step 4: Final commit if changes made**

```bash
git add -A
git commit -m "fix: polish securing AI apps blog post"
```
