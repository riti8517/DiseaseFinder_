import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0',
    port: 5173,
    allowedHosts: ['mysymptoms.info', 'www.mysymptoms.info'],
    proxy: {
      '/chat': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
      '/symptoms': {
        target: 'http://localhost:8080',
        changeOrigin: true,
      },
      '/predictDisease': {
        target: 'http://localhost:8080',
        changeOrigin: true,
      },
    },
  },
})
