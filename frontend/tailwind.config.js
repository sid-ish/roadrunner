export default {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  theme: {
    extend: {
      colors: {
        primary: "var(--color-primary)",
        secondary: "var(--color-secondary)",
        bg: "var(--color-bg)",
        card: "var(--color-card)",
        text: "var(--color-text)"
      }
    }
  },
  plugins: []
}
