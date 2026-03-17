export interface PopularPost {
  path: string;
  views: number;
}

export async function getPopularPosts(limit = 3): Promise<PopularPost[]> {
  const apiKey = import.meta.env.POSTHOG_API_KEY;
  const projectId = import.meta.env.POSTHOG_PROJECT_ID;
  const host = import.meta.env.POSTHOG_HOST || 'https://eu.posthog.com';

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
