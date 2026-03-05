/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,jsx,ts,tsx}'],
  theme: {
    extend: {
      colors: {
        primary: '#308ce8',
        'background-light': '#f6f7f8',
        'background-dark': '#111921',
      },
    },
  },
  plugins: [],
}

