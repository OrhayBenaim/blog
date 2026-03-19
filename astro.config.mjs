import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import { remarkReadingTime } from './src/plugins/remark-reading-time.mjs';

export default defineConfig({
  site: 'https://orhaybenaim.github.io',
  base: '/blog',
  integrations: [sitemap()],
  markdown: {
    syntaxHighlight: {
      type: 'shiki',
      excludeLangs: [],
    },
    remarkPlugins: [remarkReadingTime],
  },
});
