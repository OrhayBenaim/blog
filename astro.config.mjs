import { defineConfig } from 'astro/config';
import { remarkReadingTime } from './src/plugins/remark-reading-time.mjs';

export default defineConfig({
  site: 'https://orhaybenaim.github.io',
  base: '/blog',
  markdown: {
    syntaxHighlight: {
      type: 'shiki',
      excludeLangs: [],
    },
    remarkPlugins: [remarkReadingTime],
  },
});
