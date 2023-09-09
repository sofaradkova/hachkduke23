module.exports = {
    content: ['./src/routes/**/*.{svelte,js,ts}'],
    plugins: [require('daisyui')],
    daisyui: {
        themes: [
            {
            mytheme: {
            "primary": "#18314F", 
            "primary-focus": "#0D0630",
            "secondary": "#8BBEB2",
            "secondary-focus": "#384E77",
            "accent": "#E6F9AF",
            "neutral": "#FFFFFF",
            "base-100": "#3D3D3D",
            },
        },
        ],
    },
};
