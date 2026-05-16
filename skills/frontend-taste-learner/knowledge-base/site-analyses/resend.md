# Resend — https://resend.com
Analyzed: 2026-05-16

## Snapshot
- Category: Developer Tool / API
- Feel: Elegant, minimal, trustworthy, focused
- Stack: Next.js + Tailwind

## Layout & Spacing
- Centered, constrained maximum width.
- Generous padding, clean grid, airy feel.
- Code blocks are given significant visual weight and placed alongside UI previews.
- Perfect alignment, rigorous geometric structure.

## Typography  
- Inter / Geist font stack.
- Incredibly crisp headings with high contrast.
- Mono font for code blocks (often Geist Mono or similar).
- Muted grays for secondary text to establish strong hierarchy.

## Color System
- Strict monochrome palette: pure black (#000000) and pure white (#FFFFFF).
- Very subtle grays for borders and secondary surfaces (e.g., #111, #333).
- High contrast borders defining interactive areas.
- Occasional, highly intentional glowing accents (e.g., a single colored border beam).

## Motion & Animation
- Subtle, buttery smooth fade-ins on scroll.
- Border beam animations (a glowing line tracing the edge of a card).
- Rotating globes, interactive terminal/IDE representations.
- Tab transitions are snappy and crossfade cleanly.

## Standout Patterns
- Interactive code blocks / IDE inside the browser.
- Rotating 3D objects or code block visualizations as art.
- Dark mode default with minimal chrome.
- "Show, don't tell" interactive hero sections.

## Hermes Implementation Notes
- Animation library to use: Framer Motion
- Font stack: Inter, Geist, JetBrains Mono for code.
- Color: Strict #000 background, #FFF text. Rely heavily on 1px borders (#333) to separate layout.
