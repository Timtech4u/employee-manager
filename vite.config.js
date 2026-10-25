import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  plugins: [vue()],
  base: '/staticfiles/',
  publicDir: false,
  build: { outDir: 'static-vuedj', emptyOutDir: true },
  server: {
    proxy: {
      '/api': {
        target: process.env.DJANGO_DEV_ORIGIN || 'http://localhost:8000',
        changeOrigin: false,
      },
    },
  },
  test: {
    environment: 'jsdom',
    environmentOptions: { jsdom: { url: 'https://tenant.example/' } },
  },
});
