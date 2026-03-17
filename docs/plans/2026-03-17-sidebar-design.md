# Main Page Sidebar Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add a left sidebar to the blog's main page with profile, popular posts (from PostHog), and contact links.

**Architecture:** Create a `Sidebar.astro` component used only in `index.astro`. Override `--max-width` on the index page to accommodate the sidebar + content grid. Use `<details>/<summary>` for zero-JS mobile collapsible. Fetch PostHog data at Astro build time in the frontmatter.

**Tech Stack:** Astro 6, Custom CSS (no Tailwind), PostHog API, HTML `<details>` element

---

### Task 1: Optimize profile image

**Files:**
- Input: `public/profile.jpg`
- Output: `public/profile.webp`

**Step 1: Use image-optimizer skill to convert profile.jpg to WebP**

Use the `image-optimizer` skill to convert `public/profile.jpg` to `public/profile.webp`.

**Step 2: Verify the file exists**

Run: `ls -la public/profile.webp`
Expected: File exists, smaller than original jpg

---

### Task 2: Create Sidebar component

**Files:**
- Create: `src/components/Sidebar.astro`

**Step 1: Create the Sidebar component**

```astro
---
interface Props {
  popularPosts?: { title: string; slug: string }[];
}

const { popularPosts = [] } = Astro.props;
---

<aside class="sidebar">
  <div class="sidebar-content">
    <div class="sidebar-section profile-section">
      <img
        src="/blog/profile.webp"
        alt="Orhay Benaim"
        class="profile-pic"
        width="120"
        height="120"
        loading="eager"
      />
      <p class="about-text">
        Hi, I'm Orhay. I'm a software engineer and this is where I share what
        I've learned, technical tutorials, guides, and things I find interesting
        along the way.
      </p>
    </div>

    {popularPosts.length > 0 && (
      <div class="sidebar-section">
        <h3 class="section-heading">Popular Posts</h3>
        <ul class="popular-posts">
          {popularPosts.map((post) => (
            <li>
              <a href={`/blog/blog/${post.slug}/`}>{post.title}</a>
            </li>
          ))}
        </ul>
      </div>
    )}

    <div class="sidebar-section">
      <h3 class="section-heading">Reach Out</h3>
      <ul class="reach-out">
        <li>
          <a href="https://github.com/OrhayBenaim" target="_blank" rel="noopener">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
            </svg>
            GitHub
          </a>
        </li>
        <li>
          <a href="mailto:orhaybenaim@gmail.com">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect width="20" height="16" x="2" y="4" rx="2"/>
              <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>
            </svg>
            Email
          </a>
        </li>
      </ul>
    </div>
  </div>
</aside>

<!-- Mobile collapsible version -->
<details class="sidebar-mobile">
  <summary class="sidebar-toggle">About Me</summary>
  <div class="sidebar-content">
    <div class="sidebar-section profile-section">
      <img
        src="/blog/profile.webp"
        alt="Orhay Benaim"
        class="profile-pic"
        width="120"
        height="120"
        loading="eager"
      />
      <p class="about-text">
        Hi, I'm Orhay. I'm a software engineer and this is where I share what
        I've learned, technical tutorials, guides, and things I find interesting
        along the way.
      </p>
    </div>

    {popularPosts.length > 0 && (
      <div class="sidebar-section">
        <h3 class="section-heading">Popular Posts</h3>
        <ul class="popular-posts">
          {popularPosts.map((post) => (
            <li>
              <a href={`/blog/blog/${post.slug}/`}>{post.title}</a>
            </li>
          ))}
        </ul>
      </div>
    )}

    <div class="sidebar-section">
      <h3 class="section-heading">Reach Out</h3>
      <ul class="reach-out">
        <li>
          <a href="https://github.com/OrhayBenaim" target="_blank" rel="noopener">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
            </svg>
            GitHub
          </a>
        </li>
        <li>
          <a href="mailto:orhaybenaim@gmail.com">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect width="20" height="16" x="2" y="4" rx="2"/>
              <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>
            </svg>
            Email
          </a>
        </li>
      </ul>
    </div>
  </div>
</details>

<style>
  /* Desktop sidebar */
  .sidebar {
    display: block;
    background: var(--bg-glass);
    backdrop-filter: blur(var(--glass-blur));
    -webkit-backdrop-filter: blur(var(--glass-blur));
    border: var(--glass-border);
    border-radius: var(--glass-radius);
    box-shadow: var(--glass-shadow);
    padding: 1.5rem;
    height: fit-content;
  }

  .sidebar-mobile {
    display: none;
  }

  /* Profile */
  .profile-section {
    text-align: center;
  }

  .profile-pic {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    object-fit: cover;
    border: 2px solid var(--border-hover);
    margin-bottom: 1rem;
  }

  .about-text {
    color: var(--text-muted);
    font-size: 0.85rem;
    line-height: 1.6;
    margin: 0;
  }

  /* Sections */
  .sidebar-section + .sidebar-section {
    margin-top: 1.25rem;
    padding-top: 1.25rem;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
  }

  .section-heading {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 0.9rem;
    font-weight: 700;
    color: var(--text);
    margin: 0 0 0.75rem;
  }

  /* Popular posts */
  .popular-posts {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .popular-posts li {
    margin-bottom: 0.5rem;
  }

  .popular-posts a {
    color: var(--text-muted);
    font-size: 0.85rem;
    line-height: 1.4;
    transition: color var(--transition-fast);
  }

  .popular-posts a:hover {
    color: var(--accent-hover);
  }

  /* Reach out */
  .reach-out {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .reach-out li {
    margin-bottom: 0.5rem;
  }

  .reach-out a {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    color: var(--text-muted);
    font-size: 0.85rem;
    transition: color var(--transition-fast);
  }

  .reach-out a:hover {
    color: var(--accent-hover);
  }

  /* Mobile */
  @media (max-width: 640px) {
    .sidebar {
      display: none;
    }

    .sidebar-mobile {
      display: block;
      margin-bottom: 1.5rem;
    }

    .sidebar-toggle {
      display: block;
      width: 100%;
      background: var(--bg-glass);
      backdrop-filter: blur(var(--glass-blur));
      -webkit-backdrop-filter: blur(var(--glass-blur));
      border: var(--glass-border);
      border-radius: var(--glass-radius);
      padding: 0.75rem 1.25rem;
      color: var(--text);
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-weight: 700;
      font-size: 0.95rem;
      cursor: pointer;
      list-style: none;
    }

    .sidebar-toggle::-webkit-details-marker {
      display: none;
    }

    .sidebar-toggle::after {
      content: '+';
      float: right;
      font-size: 1.2rem;
      color: var(--text-muted);
      transition: transform var(--transition-fast);
    }

    details[open] .sidebar-toggle::after {
      content: '−';
    }

    .sidebar-mobile .sidebar-content {
      background: var(--bg-glass);
      backdrop-filter: blur(var(--glass-blur));
      -webkit-backdrop-filter: blur(var(--glass-blur));
      border: var(--glass-border);
      border-top: none;
      border-radius: 0 0 var(--glass-radius) var(--glass-radius);
      padding: 1.5rem;
    }

    .sidebar-mobile[open] .sidebar-toggle {
      border-radius: var(--glass-radius) var(--glass-radius) 0 0;
    }
  }
</style>
```

**Step 2: Verify file was created**

Run: `ls src/components/Sidebar.astro`
Expected: File exists

---

### Task 3: Create PostHog data fetching utility

**Files:**
- Create: `src/lib/posthog.ts`

**Step 1: Create the PostHog utility**

This module fetches top pageviews at build time. It gracefully returns an empty array if the API key is missing or the request fails.

```typescript
export interface PopularPost {
  path: string;
  views: number;
}

export async function getPopularPosts(limit = 3): Promise<PopularPost[]> {
  const apiKey = import.meta.env.POSTHOG_API_KEY;
  const projectId = import.meta.env.POSTHOG_PROJECT_ID;
  const host = import.meta.env.POSTHOG_HOST || 'https://us.posthog.com';

  if (!apiKey || !projectId) {
    console.warn('[PostHog] Missing POSTHOG_API_KEY or POSTHOG_PROJECT_ID, skipping popular posts');
    return [];
  }

  try {
    const response = await fetch(`${host}/api/projects/${projectId}/query/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${apiKey}`,
      },
      body: JSON.stringify({
        query: {
          kind: 'HogQLQuery',
          query: `
            SELECT
              properties.$pathname AS path,
              count() AS views
            FROM events
            WHERE event = '$pageview'
              AND properties.$pathname LIKE '/blog/blog/%'
            GROUP BY path
            ORDER BY views DESC
            LIMIT ${limit}
          `,
        },
      }),
    });

    if (!response.ok) {
      console.warn(`[PostHog] API returned ${response.status}`);
      return [];
    }

    const data = await response.json();
    const results: PopularPost[] = (data.results || []).map(
      (row: [string, number]) => ({
        path: row[0],
        views: row[1],
      })
    );

    return results;
  } catch (err) {
    console.warn('[PostHog] Failed to fetch popular posts:', err);
    return [];
  }
}
```

**Step 2: Verify file was created**

Run: `ls src/lib/posthog.ts`
Expected: File exists

---

### Task 4: Update index.astro to include sidebar

**Files:**
- Modify: `src/pages/index.astro`

**Step 1: Update index.astro with sidebar layout**

Replace the full content of `src/pages/index.astro` with:

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
import Header from '../components/Header.astro';
import Footer from '../components/Footer.astro';
import PostCard from '../components/PostCard.astro';
import Sidebar from '../components/Sidebar.astro';
import { getCollection } from 'astro:content';
import { getPopularPosts } from '../lib/posthog';

const posts = (await getCollection('blog'))
  .sort((a, b) => {
    const dateDiff = b.data.pubDate.valueOf() - a.data.pubDate.valueOf();
    if (dateDiff !== 0) return dateDiff;
    return b.data.pubTime.localeCompare(a.data.pubTime);
  });

// Fetch popular posts from PostHog and match to blog titles
const popularPostPaths = await getPopularPosts(3);
const popularPosts = popularPostPaths
  .map((pp) => {
    // Extract slug from path like "/blog/blog/my-post/" -> "my-post"
    const match = pp.path.match(/\/blog\/blog\/([^/]+)/);
    if (!match) return null;
    const slug = match[1];
    const post = posts.find((p) => p.id === slug);
    if (!post) return null;
    return { title: post.data.title, slug: post.id };
  })
  .filter((p): p is { title: string; slug: string } => p !== null);
---
<BaseLayout title="Orhay's Blog" description="Technical tutorials and knowledge sharing">
  <Header slot="header" />
  <div class="home-layout">
    <Sidebar popularPosts={popularPosts} />
    <div class="main-content">
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
    </div>
  </div>
  <Footer slot="footer" />
</BaseLayout>

<style>
  :global(main) {
    --max-width: 1100px;
  }

  .home-layout {
    display: grid;
    grid-template-columns: 280px 1fr;
    gap: 2rem;
    align-items: start;
  }

  h1 {
    margin-top: 0;
    margin-bottom: 1.5rem;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-weight: 800;
    color: var(--text);
  }

  .posts-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1.25rem;
  }

  @media (max-width: 900px) {
    .posts-grid {
      grid-template-columns: 1fr;
    }
  }

  @media (max-width: 640px) {
    :global(main) {
      --max-width: 900px;
    }

    .home-layout {
      display: block;
    }
  }
</style>
```

**Step 2: Verify the build succeeds**

Run: `npm run build`
Expected: Build completes without errors

---

### Task 5: Add PostHog environment variables

**Files:**
- Create: `.env.example`

**Step 1: Create .env.example with required variables**

```
POSTHOG_API_KEY=phx_your_personal_api_key_here
POSTHOG_PROJECT_ID=your_project_id_here
POSTHOG_HOST=https://us.posthog.com
```

**Step 2: Verify `.env` is in `.gitignore`**

Run: `grep -q ".env" .gitignore && echo "OK" || echo "MISSING"`

If missing, add `.env` to `.gitignore`.

**Step 3: Create actual `.env` file with real credentials**

Ask the user for their PostHog personal API key and project ID, or look them up via the PostHog MCP tools (`mcp__posthog__projects-get` to get the project ID).

---

### Task 6: Visual verification

**Step 1: Run dev server and verify**

Run: `npm run dev`

Verify in browser:
- Desktop: Sidebar appears on the left with profile pic, popular posts, and contact links
- Mobile (< 640px): Sidebar collapses into an "About Me" toggle
- Blog post pages: No sidebar visible
- About page: No sidebar visible

**Step 2: Verify build**

Run: `npm run build`
Expected: Clean build with no errors

**Step 3: Commit**

```bash
git add src/components/Sidebar.astro src/lib/posthog.ts src/pages/index.astro public/profile.webp .env.example
git commit -m "feat: add sidebar with profile, popular posts, and contact links to main page"
```

---

Plan complete and saved to `docs/plans/2026-03-17-sidebar-design.md`. Two execution options:

**1. Subagent-Driven (this session)** - I dispatch fresh subagent per task, review between tasks, fast iteration

**2. Parallel Session (separate)** - Open new session with executing-plans, batch execution with checkpoints

Which approach?
