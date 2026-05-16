# linear.app — https://linear.app
Analyzed: 2026-05-16
Screenshots taken: 5

## Snapshot
- Category: Premium SaaS / Developer Tool
- Feel: Precise, elegant, fluid
- Stack: Next.js/React, Custom animations (CSS/JS, no Framer or GSAP detected), Tailwind/Custom CSS

## Layout & Spacing
- Max-width container: ~1200px
- Section vertical padding: Very large (160px - 200px between major blocks)
- Grid columns and gutter: 2-column and 3-column masonry/bento grids with ~24px gutters.
- White space philosophy: Ultra-minimal. Uses space to frame high-fidelity UI mockups and glowing assets. Content is tightly constrained to the center or clear halves.

## Typography
- H1: Inter Variable, ~80px, medium (500), tight letter-spacing (-0.03em), line-height (1.05)
- H2: Inter Variable, ~48px, medium (500), tight letter-spacing (-0.02em), line-height (1.1)
- Body: Inter Variable, 18px, regular (400), line-height (1.6), #8A8F98

## Color System
- Background: #08090A
- Text primary: #FFFFFF
- Text secondary: #8A8F98
- Accent: #5E6AD2 (Linear purple/indigo blur accents)
- Border: #2A2B2D
- Card bg: #111214
- Mode: dark

## Motion & Animation
- Hero load animation: Subtle radial gradient lights up the background. UI screenshot slides up slightly and fades in. Typography scales down slightly from an enlarged state while fading in.
- Scroll animations: Cinematic fade-up + scale-up (0.95 to 1.0) on large sections. Very smooth, estimating 600-800ms duration.
- Hover effects: Buttons glow slightly, borders on bento cards illuminate, subtle translate-y (-2px) on interactive elements.
- Special effects: Lottie/WebGL animated UI elements within screenshots, subtle mouse-tracking radial gradients (spotlight effect) on cards.
- Motion personality: Cinematic, fluid, weightless but grounded.

## Standout Patterns
- The "Spotlight" effect on borders and backgrounds (mouse tracking reveals borders or glows).
- Typography relies on 'Medium' weight rather than 'Bold' for headers, giving it an elegant, editorial feel instead of a shouty tech feel.
- High-fidelity product visuals. The "screenshots" aren't just JPEGs; they are rebuilt UI components or extremely high-quality renders that often animate.
- Usage of "glassmorphism" (backdrop-blur) on the sticky navigation and floating elements, combined with hairline borders.

## Hermes Implementation Notes
- Animation library: Framer Motion (recommended to replicate these physics) or native CSS with intersection observers.
- Key techniques: Mouse-tracking radial gradients for the "spotlight" card effect.
- Font stack: Inter (with font-feature-settings for tabular numbers/alternate glyphs).
- Color tokens: bg=#08090A text=#FFFFFF accent=#5E6AD2 border=#2A2B2D