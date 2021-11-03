module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      spacing: {
        "25vh": "25vh",
        "50vh": "50vh",
        "75vh": "75vh",
      },
      borderRadius: {
        xl: "1.5rem",
      },
      colors: {
        teal: {
          "100": "#CCFBF1",
          "200": "#99F6E4",
          "300": "#5EEAD4",
          "400": "#2DD4BF",
          "500": "#14B8A6",
          "600": "#0D9488",
          "700": "#0F766E",
          "800": "#115E59",
          "900": "#134E4A",
        }
      },
      minHeight: {
        "50vh": "50vh",
        "75vh": "75vh"
      }
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
