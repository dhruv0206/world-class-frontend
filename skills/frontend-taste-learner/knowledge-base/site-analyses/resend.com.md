# Resend — https://resend.com
Analyzed: 2026-09-14
Screenshots taken: 8

## Snapshot
- Category: Developer tool
- Feel: Cinematic, technical, premium
- Stack: React, Next.js (assumed based on ecosystem), Tailwind

## Layout & Spacing
- Max-width container: ~1200px
- Section vertical padding: ~160px
- Grid columns and gutter: 4-column pricing cards, 24px gap
- White space philosophy: Ultra-minimalist, heavy reliance on deep black negative space to emphasize glowing elements.

## Typography
- H1: Domaine (Serif), ~72px, Medium/Bold, tight letter-spacing, 1.1 line-height
- H2: Inter (Sans-serif), ~48px, Semi-bold, tight tracking
- Body: Inter, ~16px, Regular, 1.6 line-height, color: #a1a1aa

## Color System
- Background: #000000
- Text primary: #ffffff
- Text secondary: #a1a1aa
- Accent: #ffffff (stark contrast)
- Border: #27272a (very subtle dark gray)
- Card bg: #09090b
- Mode: dark

## Motion & Animation
- Hero load: Subtle fade up of typography, central 3D cube rotates slowly with volumetric lighting.
- Scroll animations: Elements fade up smoothly on scroll (Lenis/GSAP typically used for this feel).
- Hover effects: Glow trails on card borders, slight brightness bump.
- Special effects: 3D webGL integration, subtle radial background gradients simulating light.
- Motion personality: Cinematic and subtle.

## Standout Patterns
1. **Typography contrast:** Pairing an elegant, editorial serif (Domaine) with a sharp, technical sans-serif (Inter) gives it a unique "premium developer" aesthetic.
2. **Volumetric lighting:** The background isn't flat black; it features subtle, masked radial gradients that look like spotlights.
3. **Micro-borders:** Cards use 1px borders with very dark grays (#27272a) that almost blend into the background, creating depth without bulk.
4. **Interactive code presentation:** Code blocks are treated as primary visual assets with high-fidelity syntax highlighting and tab interfaces.

## Hermes Implementation Notes
- Animation library: Framer Motion for UI, Three.js/React Three Fiber for hero 3D.
- Key techniques: 
  - Radial gradient backgrounds masked behind elements
  - 1px semi-transparent borders `border border-white/10`
  - Serif headings `font-serif` mixed with `font-sans` body
- Font stack: Domaine (or Playfair Display as fallback), Inter
- Color tokens: bg=#000000 text=#ffffff accent=#ffffff border=#27272a
