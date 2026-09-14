# KIKK Festival — https://kikk.be
Analyzed: 2026-09-14
Screenshots taken: 4

## Snapshot
- Category: Agency / Event
- Feel: Brutalist, geometric, experimental
- Stack: HTML/CSS, Custom JS

## Layout & Spacing
- Max-width container (px): Full width with rigid 1px border grid system
- Section vertical padding (px): ~120px
- Grid columns and gutter: Custom asymmetric grid with persistent vertical border lines
- White space philosophy: Expansive, uses giant background typography to fill space without adding weight

## Typography
- H1: Suisse Intl / Inter Tight, 120px+, 700 weight, normal letter-spacing, tight line-height
- H2: Suisse Intl, 48px, 500 weight
- Body: Suisse Intl, 16px, 400 weight, 1.5 line-height, #333333

## Color System
- Background: #F1F1F1
- Text primary: #111111
- Text secondary: #666666
- Accent: #4A6FFF (Blue geometric overlay)
- Border: #D1D1D1
- Card bg: #FFFFFF
- Mode: light

## Motion & Animation
- Hero load animation: Geometric shapes slide in diagonally over text
- Scroll animations: Background giant text translates slowly (parallax)
- Hover effects: Grid cell backgrounds invert
- Special effects: SVG diagonal interactive elements
- Motion personality: Expressive, mechanical

## Standout Patterns
1. Persistent 1px grid lines defining the layout instead of invisible margins
2. Giant, low-opacity background typography acting as texture
3. Diagonal geometric vector shapes breaking the rigid orthogonal grid
4. Vertical rotated text for section labels (e.g., "002 — ABOUT")

## Hermes Implementation Notes
- Animation library: Framer Motion / GSAP (though native uses custom)
- Key techniques: CSS Grid with borders, vertical text (`writing-mode: vertical-rl`), SVG overlays
- Font stack: Inter, Suisse Intl
- Color tokens: bg=#F1F1F1 text=#111111 accent=#4A6FFF border=#D1D1D1
