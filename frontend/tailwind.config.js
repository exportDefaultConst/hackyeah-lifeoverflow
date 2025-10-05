/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'zus-yellow': '#FFB34F',
        'zus-green': '#00993F',
        'zus-grey': '#BEC3CE',
        'zus-blue': '#3F84D2',
        'zus-dark-blue': '#00416E',
        'zus-red': '#F05E5E',
      },
    },
  },
  plugins: [],
}
