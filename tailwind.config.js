

export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      colors: {
        'neon-y': '#E6F9AF',
        'dark-y': '5F7421'
      },
    },
  },
  plugins: [require('daisyui')],
  daisyui: {
    themes: [
        "lemonade"
    ],
  },
}