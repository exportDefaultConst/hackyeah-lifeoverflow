import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    proxy: {
      '/api': {
        target: 'http://lifeoverflow.packt.pl',
        changeOrigin: true
      }
    }
  },
  preview: {
    port: 4443,
    host: '0.0.0.0',
    allowedHosts: ['lifeoverflow.packt.pl']
  }
})
