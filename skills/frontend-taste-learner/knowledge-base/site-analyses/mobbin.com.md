# mobbin.com — https://mobbin.com
Analyzed: 2026-09-14
Screenshots taken: 6

## Snapshot
- Category: Design inspiration / SaaS
- Feel: Premium, minimal, Apple-like
- Stack: React, Framer Motion

## Layout & Spacing
- Max-width container (px): ~1200px
- Section vertical padding (px): ~120px-160px
- Grid columns and gutter: 3-column grid for pricing (gap ~32px)
- White space philosophy: Expansive, uses space to isolate elements and drive focus.

## Typography
- H1: M Saans 652, large (~80px), bold, tight letter-spacing
- H2: M Saans 600, ~48px
- Body: M Saans Variable Light, ~16px

## Color System
- Background: #FFFFFF (Home), #111111 (Pricing)
- Text primary: #000000 (Light), #FFFFFF (Dark)
- Text secondary: #666666 (Light), #999999 (Dark)
- Accent: #000000
- Border: #EAEAEE (Light), #333333 (Dark)
- Card bg: #F9F9F9 (Light), #1A1A1A (Dark)
- Mode: Light (Homepage), Dark (Pricing page)

## Motion & Animation
- Scroll animations: Floating app icons scatter around central text (parallax effect).
- Motion personality: Fluid, Apple-like, structural.

## Standout Patterns
1. Floating pill-shaped navigation bar (centered) instead of a standard full-width header.
2. Dramatic color mode switch between homepage (pure white) and pricing (deep dark).
3. Scattered, floating app icons acting as a dynamic background layer.
4. Custom typeface with extremely tight tracking on oversized headlines.

## Hermes Implementation Notes
- Animation library: Framer Motion
- Key techniques: 
  - Floating pill nav with backdrop-blur
  - Parallax floating icons
  - Sharp contrast between pages
- Font stack: "M Saans", sans-serif (use Inter with tight tracking as fallback)
- Color tokens: bg=#FFFFFF text=#000000 accent=#000000 border=#EAEAEE
