

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
			{
				mytheme: {
					primary: "#18314F",
					"primary-focus": "#0D0630",
					secondary: "#8BBEB2",
					"secondary-focus": "#384E77",
					accent: "#5F7421",
					neutral: "#FFFFFF",
					"base-100": "#3D3D3D",
				},
			},
		],
  },
}