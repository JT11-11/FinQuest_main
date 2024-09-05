/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./static/**.css",
    "./templates/**/*.html",
  ],

  theme: {
    extend: {
      colors:{
        greenish:"#52796f",
        whitegreen:"#cad2c5"
      }

    },
  },
  plugins: [],
}


