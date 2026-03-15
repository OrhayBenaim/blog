# Forest Glass Blog Redesign — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Redesign the Astro blog from a dark GitHub theme to a nature-immersive glassmorphism aesthetic with frosted glass panels over an organic forest background.

**Architecture:** Pure CSS redesign using CSS custom properties. No new dependencies — only Google Fonts added via `<link>`. All glass effects use `backdrop-filter: blur()` with `rgba()` backgrounds. A forest background image (CSS gradient fallback) is set on `body` with `background-attachment: fixed`. Subtle JS for navbar scroll behavior and fade-in animations.

**Tech Stack:** Astro 6, scoped CSS, CSS custom properties, Google Fonts (Plus Jakarta Sans, Inter, JetBrains Mono)

**Design doc:** `docs/plans/2026-03-16-forest-glass-redesign-design.md`

---

## Task 1: Update Design Tokens & Global Styles in BaseLayout

**Files:**
- Modify: `src/layouts/BaseLayout.astro`

**Step 1: Update CSS custom properties**

Replace the `:root` block (lines 22-32) with the new Forest Glass color system:

```css
:root {
  /* Forest Glass palette */
  --pine-teal: #344e41;
  --hunter-green: #3a5a40;
  --fern: #588157;
  --dry-sage: #a3b18a;
  --dust-grey: #dad7cd;

  /* Semantic tokens */
  --bg: #1a2e1a;
  --bg-glass: rgba(58, 90, 64, 0.25);
  --bg-glass-hover: rgba(58, 90, 64, 0.35);
  --bg-glass-dark: rgba(52, 78, 65, 0.4);
  --text: #dad7cd;
  --text-muted: #a3b18a;
  --accent: #588157;
  --accent-hover: #a3b18a;
  --border: rgba(163, 177, 138, 0.2);
  --border-hover: rgba(88, 129, 87, 0.5);
  --code-bg: rgba(52, 78, 65, 0.4);
  --max-width: 900px;

  /* Glass properties */
  --glass-blur: 16px;
  --glass-radius: 16px;
  --glass-border: 1px solid var(--border);
  --glass-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);

  /* Transitions */
  --transition-fast: 0.2s ease;
  --transition-normal: 0.3s ease;
}
```

**Step 2: Update `html` and `body` styles**

Replace the `html` rule (lines 40-45) with:

```css
html {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  color: var(--text);
  line-height: 1.7;
  scroll-behavior: smooth;
}
```

Replace the `body` rule (lines 47-51) with:

```css
body {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: var(--pine-teal);
  background-image:
    linear-gradient(135deg, rgba(52, 78, 65, 0.9) 0%, rgba(58, 90, 64, 0.7) 50%, rgba(52, 78, 65, 0.85) 100%),
    url('/blog/forest-bg.webp');
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  background-repeat: no-repeat;
}
```

**Step 3: Add Google Fonts to `<head>`**

Add before the `<Analytics />` tag (line 20):

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Plus+Jakarta+Sans:wght@600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
```

**Step 4: Update global link styles**

Replace the `a` and `a:hover` rules (lines 53-60):

```css
a {
  color: var(--accent);
  text-decoration: none;
  transition: color var(--transition-fast);
}

a:hover {
  color: var(--accent-hover);
  text-decoration: none;
}
```

**Step 5: Update `main` element**

Replace the `main` rule (lines 63-69):

```css
main {
  flex: 1;
  width: 100%;
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 2rem 1.5rem;
  padding-top: 6rem; /* space for fixed navbar */
}
```

**Step 6: Update heading styles**

Replace the heading rules (lines 91-100):

```css
h1, h2, h3, h4 {
  font-family: 'Plus Jakarta Sans', sans-serif;
  color: var(--dust-grey);
  line-height: 1.3;
  margin-top: 2rem;
  margin-bottom: 0.75rem;
}

h1 { font-size: 2rem; font-weight: 800; }
h2 { font-size: 1.5rem; font-weight: 700; }
h3 { font-size: 1.25rem; font-weight: 700; }
```

**Step 7: Update code and pre styles**

Replace code/pre rules (lines 71-89):

```css
code {
  font-family: 'JetBrains Mono', 'Fira Code', 'Cascadia Code', monospace;
  font-size: 0.9em;
}

:not(pre) > code {
  background: var(--code-bg);
  padding: 0.15em 0.35em;
  border-radius: 6px;
  border: var(--glass-border);
  backdrop-filter: blur(8px);
}

pre {
  padding: 1.25rem;
  border-radius: var(--glass-radius);
  border: var(--glass-border);
  background: var(--bg-glass-dark) !important;
  backdrop-filter: blur(12px);
  overflow-x: auto;
  margin: 1.5rem 0;
}
```

**Step 8: Update remaining global rules**

Update `img` border-radius (line 117):

```css
img {
  max-width: 100%;
  border-radius: var(--glass-radius);
}
```

Update `hr` (lines 120-123):

```css
hr {
  border: none;
  border-top: var(--glass-border);
  margin: 2rem 0;
}
```

**Step 9: Add page fade-in animation**

Add to the end of the global styles:

```css
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(8px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

main {
  animation: fadeInUp 0.5s ease both;
}
```

Note: This second `main` rule adds the animation. Merge it with the existing `main` rule from Step 5.

**Step 10: Verify**

Run: `npx astro dev`
Expected: The page loads with the green-toned gradient background, new fonts, and updated colors. No glass components yet, but the foundation is in place.

**Step 11: Commit**

```bash
git add src/layouts/BaseLayout.astro
git commit -m "feat: update design tokens and global styles for Forest Glass theme"
```

---

## Task 2: Add Forest Background Image

**Files:**
- Create: `public/forest-bg.webp`

**Step 1: Source a background image**

We need a dark, moody forest background image. Options:
- Use a free stock photo from Unsplash (search "dark forest canopy aerial")
- Or generate a CSS-only fallback (already in place from Task 1's gradient)

For now, create a CSS-only organic background pattern as a fallback. Add this to `BaseLayout.astro`'s body style if no image is available:

Replace the `background-image` in the body rule with a richer CSS gradient:

```css
body {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: var(--pine-teal);
  background-image:
    radial-gradient(ellipse at 20% 50%, rgba(88, 129, 87, 0.3) 0%, transparent 50%),
    radial-gradient(ellipse at 80% 20%, rgba(58, 90, 64, 0.4) 0%, transparent 50%),
    radial-gradient(ellipse at 40% 80%, rgba(52, 78, 65, 0.3) 0%, transparent 50%),
    linear-gradient(135deg, #2d4a37 0%, #344e41 25%, #3a5a40 50%, #344e41 75%, #2d4a37 100%);
  background-attachment: fixed;
}
```

The immersive-web-creator agent will determine whether to use an actual image or pure CSS gradients based on visual quality.

**Step 2: Commit**

```bash
git commit -m "feat: add organic forest background"
```

---

## Task 3: Redesign Header as Floating Glass Navbar

**Files:**
- Modify: `src/components/Header.astro`

**Step 1: Update the HTML structure**

Replace the entire `Header.astro` content with:

```astro
---
const navItems = [
  { label: 'Home', href: '/blog/' },
  { label: 'About', href: '/blog/about/' },
  { label: 'Tags', href: '/blog/tags/' },
];
---
<header>
  <nav>
    <a href="/blog/" class="logo">Orhay's Blog</a>
    <div class="nav-links">
      {navItems.map(item => (
        <a href={item.href}>{item.label}</a>
      ))}
      <a href="/blog/rss.xml" target="_blank" title="RSS Feed" class="rss-link">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M4 11a9 9 0 0 1 9 9" /><path d="M4 4a16 16 0 0 1 16 16" /><circle cx="5" cy="19" r="1" />
        </svg>
      </a>
    </div>
  </nav>
</header>

<script>
  const header = document.querySelector('header');
  let lastScroll = 0;
  window.addEventListener('scroll', () => {
    const scrolled = window.scrollY > 20;
    header?.classList.toggle('scrolled', scrolled);
    lastScroll = window.scrollY;
  }, { passive: true });
</script>

<style>
  header {
    position: fixed;
    top: 1rem;
    left: 50%;
    transform: translateX(-50%);
    width: calc(100% - 2rem);
    max-width: var(--max-width);
    z-index: 100;
    background: var(--bg-glass);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: var(--glass-border);
    border-radius: var(--glass-radius);
    box-shadow: var(--glass-shadow);
    transition: backdrop-filter var(--transition-normal),
                box-shadow var(--transition-normal),
                background var(--transition-normal);
  }

  header.scrolled {
    background: rgba(58, 90, 64, 0.35);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    box-shadow: 0 8px 40px rgba(0, 0, 0, 0.3);
  }

  nav {
    padding: 0.75rem 1.5rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .logo {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-weight: 700;
    font-size: 1.15rem;
    color: var(--dust-grey);
  }

  .logo:hover {
    color: var(--fern);
    text-decoration: none;
  }

  .nav-links {
    display: flex;
    gap: 1.25rem;
    align-items: center;
    font-size: 0.95rem;
  }

  .nav-links a {
    color: var(--dry-sage);
    transition: color var(--transition-fast);
  }

  .nav-links a:hover {
    color: var(--dust-grey);
    text-decoration: none;
  }

  .rss-link {
    display: flex;
    align-items: center;
  }

  @media (max-width: 640px) {
    header {
      top: 0.5rem;
      width: calc(100% - 1rem);
      border-radius: 12px;
    }

    nav {
      padding: 0.6rem 1rem;
    }

    .nav-links {
      gap: 0.75rem;
      font-size: 0.85rem;
    }
  }
</style>
```

**Step 2: Verify**

Run: `npx astro dev`
Expected: Floating glass navbar centered at top of page, detached from edges, frosted blur effect visible. On scroll past 20px, blur intensifies.

**Step 3: Commit**

```bash
git add src/components/Header.astro
git commit -m "feat: redesign header as floating glass navbar"
```

---

## Task 4: Redesign PostCard as Glass Cards in 2-Column Grid

**Files:**
- Modify: `src/components/PostCard.astro`
- Modify: `src/pages/index.astro`

**Step 1: Update PostCard component**

Replace the entire `PostCard.astro` content with:

```astro
---
interface Props {
  title: string;
  description: string;
  pubDate: Date;
  tags: string[];
  slug: string;
}

const { title, description, pubDate, tags, slug } = Astro.props;

function formatDate(date: Date): string {
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
  });
}
---
<article class="post-card">
  <a href={`/blog/blog/${slug}/`} class="card-link">
    <h2>{title}</h2>
    <p>{description}</p>
  </a>
  <div class="meta">
    <time datetime={pubDate.toISOString()}>{formatDate(pubDate)}</time>
    {tags.length > 0 && (
      <div class="tags">
        {tags.map(tag => (
          <a href={`/blog/tags/${tag}/`} class="tag">#{tag}</a>
        ))}
      </div>
    )}
  </div>
</article>

<style>
  .post-card {
    background: var(--bg-glass);
    backdrop-filter: blur(var(--glass-blur));
    -webkit-backdrop-filter: blur(var(--glass-blur));
    border: var(--glass-border);
    border-radius: var(--glass-radius);
    padding: 1.5rem;
    transition: transform var(--transition-normal),
                border-color var(--transition-normal),
                box-shadow var(--transition-normal);
  }

  .post-card:hover {
    transform: translateY(-4px);
    border-color: var(--border-hover);
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.25), 0 0 0 1px var(--border-hover);
  }

  .card-link {
    color: inherit;
    display: block;
  }

  .card-link:hover {
    text-decoration: none;
  }

  .post-card h2 {
    margin: 0 0 0.5rem;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 1.25rem;
    font-weight: 700;
    color: var(--dust-grey);
    transition: color var(--transition-fast);
  }

  .post-card:hover h2 {
    color: var(--fern);
  }

  .card-link p {
    color: var(--dry-sage);
    margin: 0;
    font-size: 0.9rem;
    line-height: 1.5;
  }

  .meta {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 1rem;
    padding-top: 0.75rem;
    border-top: 1px solid rgba(163, 177, 138, 0.1);
  }

  time {
    color: var(--dry-sage);
    font-size: 0.8rem;
  }

  .tags {
    display: flex;
    gap: 0.4rem;
    flex-wrap: wrap;
  }

  .tag {
    font-size: 0.75rem;
    color: var(--fern);
    background: rgba(88, 129, 87, 0.15);
    padding: 0.15rem 0.5rem;
    border-radius: 20px;
    border: 1px solid rgba(88, 129, 87, 0.2);
    transition: background var(--transition-fast), color var(--transition-fast);
  }

  .tag:hover {
    background: rgba(88, 129, 87, 0.3);
    color: var(--dust-grey);
    text-decoration: none;
  }
</style>
```

**Step 2: Update homepage for 2-column grid**

Replace the entire `src/pages/index.astro` content with:

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
import Header from '../components/Header.astro';
import Footer from '../components/Footer.astro';
import PostCard from '../components/PostCard.astro';
import { getCollection } from 'astro:content';

const posts = (await getCollection('blog'))
  .sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf());
---
<BaseLayout title="Orhay's Blog" description="Technical tutorials and knowledge sharing">
  <Header slot="header" />
  <h1>Posts</h1>
  <section class="posts-grid">
    {posts.map(post => (
      <PostCard
        title={post.data.title}
        description={post.data.description}
        pubDate={post.data.pubDate}
        tags={post.data.tags}
        slug={post.id}
      />
    ))}
  </section>
  <Footer slot="footer" />
</BaseLayout>

<style>
  h1 {
    margin-top: 0;
    margin-bottom: 1.5rem;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-weight: 800;
    color: var(--dust-grey);
  }

  .posts-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1.25rem;
  }

  @media (max-width: 640px) {
    .posts-grid {
      grid-template-columns: 1fr;
    }
  }
</style>
```

**Step 3: Verify**

Run: `npx astro dev`
Expected: Homepage shows post cards in a 2-column grid. Cards have frosted glass effect, hover lifts them, tags are pill-shaped.

**Step 4: Commit**

```bash
git add src/components/PostCard.astro src/pages/index.astro
git commit -m "feat: redesign post cards as glass cards in 2-column grid"
```

---

## Task 5: Redesign Blog Post Page with Glass Container

**Files:**
- Modify: `src/layouts/BlogPost.astro`

**Step 1: Update BlogPost layout**

Replace the entire `BlogPost.astro` content with:

```astro
---
import BaseLayout from './BaseLayout.astro';
import Header from '../components/Header.astro';
import Footer from '../components/Footer.astro';

interface Props {
  title: string;
  description: string;
  pubDate: Date;
  updatedDate?: Date;
  tags: string[];
  minutesRead?: string;
}

const { title, description, pubDate, updatedDate, tags, minutesRead } = Astro.props;

function formatDate(date: Date): string {
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  });
}
---
<BaseLayout title={title} description={description}>
  <Header slot="header" />
  <article class="glass-article">
    <header class="post-header">
      <h1>{title}</h1>
      <div class="post-meta">
        <time datetime={pubDate.toISOString()}>{formatDate(pubDate)}</time>
        {updatedDate && (
          <span> · Updated <time datetime={updatedDate.toISOString()}>{formatDate(updatedDate)}</time></span>
        )}
        {minutesRead && <span> · {minutesRead}</span>}
      </div>
      {tags.length > 0 && (
        <div class="post-tags">
          {tags.map(tag => (
            <a href={`/blog/tags/${tag}/`} class="tag">#{tag}</a>
          ))}
        </div>
      )}
    </header>
    <div class="post-content">
      <slot />
    </div>
  </article>
  <Footer slot="footer" />
</BaseLayout>

<style>
  .glass-article {
    background: var(--bg-glass);
    backdrop-filter: blur(var(--glass-blur));
    -webkit-backdrop-filter: blur(var(--glass-blur));
    border: var(--glass-border);
    border-radius: var(--glass-radius);
    box-shadow: var(--glass-shadow);
    padding: 2.5rem;
    max-width: 720px;
    margin: 0 auto;
  }

  .post-header {
    margin-bottom: 2.5rem;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid rgba(163, 177, 138, 0.15);
  }

  .post-header h1 {
    margin-top: 0;
    font-size: 2.25rem;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-weight: 800;
    color: var(--dust-grey);
  }

  .post-meta {
    color: var(--dry-sage);
    font-size: 0.9rem;
    margin-top: 0.5rem;
  }

  .post-tags {
    display: flex;
    gap: 0.5rem;
    margin-top: 0.75rem;
    flex-wrap: wrap;
  }

  .tag {
    font-size: 0.8rem;
    color: var(--fern);
    background: rgba(88, 129, 87, 0.15);
    padding: 0.2rem 0.65rem;
    border-radius: 20px;
    border: 1px solid rgba(88, 129, 87, 0.2);
    transition: background var(--transition-fast), color var(--transition-fast);
  }

  .tag:hover {
    text-decoration: none;
    background: rgba(88, 129, 87, 0.3);
    color: var(--dust-grey);
  }

  .post-content {
    font-size: 1.05rem;
  }

  .post-content :global(h2) {
    margin-top: 2.5rem;
  }

  .post-content :global(blockquote) {
    border-left: 3px solid var(--fern);
    padding-left: 1rem;
    color: var(--dry-sage);
    margin: 1.5rem 0;
  }

  .post-content :global(pre) {
    background: var(--bg-glass-dark) !important;
    border: var(--glass-border);
    border-radius: 12px;
  }

  @media (max-width: 640px) {
    .glass-article {
      padding: 1.5rem;
      border-radius: 12px;
    }
  }
</style>
```

**Step 2: Verify**

Run: `npx astro dev`, navigate to a blog post.
Expected: Article is wrapped in a frosted glass panel, centered, with updated tags as pills.

**Step 3: Commit**

```bash
git add src/layouts/BlogPost.astro
git commit -m "feat: redesign blog post page with glass container"
```

---

## Task 6: Redesign Tags Pages

**Files:**
- Modify: `src/pages/tags/index.astro`
- Modify: `src/pages/tags/[tag].astro`

**Step 1: Update tags index page**

Replace the entire `src/pages/tags/index.astro` content with:

```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';
import Header from '../../components/Header.astro';
import Footer from '../../components/Footer.astro';
import { getCollection } from 'astro:content';

const posts = await getCollection('blog');
const tagCounts = new Map<string, number>();
posts.forEach(post => {
  post.data.tags.forEach(tag => {
    tagCounts.set(tag, (tagCounts.get(tag) || 0) + 1);
  });
});
const tags = [...tagCounts.entries()].sort((a, b) => b[1] - a[1]);
---
<BaseLayout title="Tags - Orhay's Blog" description="Browse posts by tag">
  <Header slot="header" />
  <h1>Tags</h1>
  <div class="tags">
    {tags.map(([tag, count]) => (
      <a href={`/blog/tags/${tag}/`} class="tag-card">
        <span class="tag-name">#{tag}</span>
        <span class="count">{count} post{count !== 1 ? 's' : ''}</span>
      </a>
    ))}
  </div>
  <Footer slot="footer" />
</BaseLayout>

<style>
  h1 {
    margin-top: 0;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-weight: 800;
    color: var(--dust-grey);
  }

  .tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
    margin-top: 1.5rem;
  }

  .tag-card {
    background: var(--bg-glass);
    backdrop-filter: blur(var(--glass-blur));
    -webkit-backdrop-filter: blur(var(--glass-blur));
    border: var(--glass-border);
    border-radius: var(--glass-radius);
    padding: 0.75rem 1.25rem;
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
    transition: transform var(--transition-normal),
                border-color var(--transition-normal),
                box-shadow var(--transition-normal);
  }

  .tag-card:hover {
    transform: translateY(-2px);
    border-color: var(--border-hover);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
    text-decoration: none;
  }

  .tag-name {
    color: var(--fern);
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-weight: 600;
    font-size: 1rem;
  }

  .tag-card:hover .tag-name {
    color: var(--dust-grey);
  }

  .count {
    color: var(--dry-sage);
    font-size: 0.8rem;
  }
</style>
```

**Step 2: Update tag filter page**

Replace the entire `src/pages/tags/[tag].astro` content with:

```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';
import Header from '../../components/Header.astro';
import Footer from '../../components/Footer.astro';
import PostCard from '../../components/PostCard.astro';
import { getCollection } from 'astro:content';

export async function getStaticPaths() {
  const posts = await getCollection('blog');
  const tags = new Set<string>();
  posts.forEach(post => post.data.tags.forEach(tag => tags.add(tag)));

  return [...tags].map(tag => ({
    params: { tag },
    props: {
      tag,
      posts: posts
        .filter(post => post.data.tags.includes(tag))
        .sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf()),
    },
  }));
}

const { tag, posts } = Astro.props;
---
<BaseLayout title={`#${tag} - Orhay's Blog`} description={`Posts tagged with ${tag}`}>
  <Header slot="header" />
  <h1>#{tag}</h1>
  <p class="count">{posts.length} post{posts.length !== 1 ? 's' : ''}</p>
  <section class="posts-grid">
    {posts.map(post => (
      <PostCard
        title={post.data.title}
        description={post.data.description}
        pubDate={post.data.pubDate}
        tags={post.data.tags}
        slug={post.id}
      />
    ))}
  </section>
  <Footer slot="footer" />
</BaseLayout>

<style>
  h1 {
    margin-top: 0;
    margin-bottom: 0.25rem;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-weight: 800;
    color: var(--dust-grey);
  }

  .count {
    color: var(--dry-sage);
    margin-bottom: 1.5rem;
  }

  .posts-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1.25rem;
  }

  @media (max-width: 640px) {
    .posts-grid {
      grid-template-columns: 1fr;
    }
  }
</style>
```

**Step 3: Verify**

Run: `npx astro dev`, navigate to `/blog/tags/`.
Expected: Tags page shows glass card pills for each tag with hover lift effect. Tag filter page shows posts in 2-column grid.

**Step 4: Commit**

```bash
git add src/pages/tags/index.astro src/pages/tags/\[tag\].astro
git commit -m "feat: redesign tags pages with glass cards"
```

---

## Task 7: Redesign About Page

**Files:**
- Modify: `src/pages/about.astro`

**Step 1: Update about page**

Replace the entire `src/pages/about.astro` content with:

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
import Header from '../components/Header.astro';
import Footer from '../components/Footer.astro';
---
<BaseLayout title="About - Orhay's Blog" description="About Orhay Benaim">
  <Header slot="header" />
  <div class="glass-panel">
    <h1>About</h1>
    <p>
      Hi, I'm Orhay. I'm a software engineer and this is where I share what I've learned —
      technical tutorials, guides, and things I find interesting along the way.
    </p>
    <p>
      If you have questions or want to reach out, find me on
      <a href="https://github.com/OrhayBenaim" target="_blank">GitHub</a>.
    </p>
  </div>
  <Footer slot="footer" />
</BaseLayout>

<style>
  .glass-panel {
    background: var(--bg-glass);
    backdrop-filter: blur(var(--glass-blur));
    -webkit-backdrop-filter: blur(var(--glass-blur));
    border: var(--glass-border);
    border-radius: var(--glass-radius);
    box-shadow: var(--glass-shadow);
    padding: 2.5rem;
    max-width: 720px;
    margin: 0 auto;
  }

  h1 {
    margin-top: 0;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-weight: 800;
    color: var(--dust-grey);
  }

  p {
    color: var(--dry-sage);
    line-height: 1.8;
  }

  @media (max-width: 640px) {
    .glass-panel {
      padding: 1.5rem;
      border-radius: 12px;
    }
  }
</style>
```

**Step 2: Verify**

Run: `npx astro dev`, navigate to `/blog/about/`.
Expected: About page content is wrapped in a glass panel.

**Step 3: Commit**

```bash
git add src/pages/about.astro
git commit -m "feat: redesign about page with glass panel"
```

---

## Task 8: Redesign Footer

**Files:**
- Modify: `src/components/Footer.astro`

**Step 1: Update footer**

Replace the entire `Footer.astro` content with:

```astro
---
const year = new Date().getFullYear();
---
<footer>
  <p>&copy; {year} Orhay Benaim. Built with <a href="https://astro.build" target="_blank">Astro</a>.</p>
</footer>

<style>
  footer {
    padding: 2rem 1.5rem;
    text-align: center;
    color: var(--dry-sage);
    font-size: 0.85rem;
  }

  footer a {
    color: var(--fern);
  }

  footer a:hover {
    color: var(--dust-grey);
  }
</style>
```

**Step 2: Verify**

Run: `npx astro dev`
Expected: Footer is clean text on the background, no glass container, Dry Sage colored.

**Step 3: Commit**

```bash
git add src/components/Footer.astro
git commit -m "feat: update footer for Forest Glass theme"
```

---

## Task 9: Final Visual Polish & Responsive Testing

**Files:**
- Possibly modify: `src/layouts/BaseLayout.astro` (tweaks)

**Step 1: Run full build**

Run: `npx astro build`
Expected: Build succeeds with no errors.

**Step 2: Preview production build**

Run: `npx astro preview`
Test the following at various widths (desktop, tablet ~768px, mobile ~375px):
- [ ] Homepage: 2-column grid collapses to 1 on mobile
- [ ] Navbar: glass effect visible, floats detached from edges, scrolled state works
- [ ] Blog post: glass container is readable, code blocks have glass styling
- [ ] Tags page: tag cards display correctly
- [ ] About page: glass panel centered
- [ ] Footer: minimal text, no glass

**Step 3: Fix any issues found**

Adjust spacing, font sizes, or glass opacity as needed.

**Step 4: Commit**

```bash
git commit -am "fix: responsive polish and final tweaks"
```

---

## Summary of Files Modified

| File | Change |
|------|--------|
| `src/layouts/BaseLayout.astro` | Design tokens, fonts, background, global styles, animations |
| `src/layouts/BlogPost.astro` | Glass article container, updated tag pills |
| `src/components/Header.astro` | Floating glass navbar with scroll behavior |
| `src/components/PostCard.astro` | Glass cards with hover effects |
| `src/components/Footer.astro` | Minimal footer, Dry Sage text |
| `src/pages/index.astro` | 2-column grid layout |
| `src/pages/about.astro` | Glass panel wrapper |
| `src/pages/tags/index.astro` | Glass tag cards |
| `src/pages/tags/[tag].astro` | 2-column grid layout |
| `public/forest-bg.webp` | Optional background image |
