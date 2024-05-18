// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ['@nuxt/content', 'nuxt-icon'],
  app: {
    head: {
      link: [
        {
          rel: 'icon',
          type: 'image/svg+xml',
          href: '/ww-favicon.svg',
        },
      ],
    },
  },
});
