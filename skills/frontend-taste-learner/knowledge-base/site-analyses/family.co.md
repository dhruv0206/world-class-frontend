# family.co — https://family.co
Analyzed: 2026-09-14
Screenshots taken: 6

## Snapshot
- Category: Crypto wallet / Web3 consumer
- Feel: Playful, premium, fluid
- Stack: Custom fonts ("Family", Inter), likely React. No GSAP/Framer motion detected on window.

## Layout & Spacing
- Max-width container: ~1200px
- Section vertical padding: ~120px
- Grid columns and gutter: Bento box grid layout (2 or 3 columns), ~24px gutters.
- White space philosophy: Generous whitespace, letting the bento cards breathe. 

## Typography
- H1: "Family" or Inter, ~72px, bold, tight letter-spacing (-0.02em), tight line-height (1.1).
- H2: ~48px, semi-bold, tight line-height.
- Body: Inter, ~16px, regular, 1.5 line-height, #666666.

## Color System
- Background: #FFFFFF
- Text primary: #000000
- Text secondary: #666666
- Accent: #00D395 (green)
- Border: #EAEAEA
- Card bg: #F7F7F7
- Mode: light

## Motion & Animation
- Scroll animations: Elements fade and slide up slightly on scroll.
- Hover effects: Subtle scale (1.02) on bento cards, button hover transitions.
- Motion personality: Fluid, Apple-like, bouncy.

## Standout Patterns
- High-fidelity bento grids with embedded micro-interactions (e.g. the "Backing Up" pill).
- Very tight, custom typography that gives it a distinct brand voice over standard system fonts.
- Extremely clean light mode with very subtle off-white card backgrounds to create depth without heavy shadows.

## Hermes Implementation Notes
- Animation library: Framer Motion (for fluid, spring-based interactions).
- Key techniques: Bento box layouts, tight H1 tracking, spring physics.
- Font stack: Inter
- Color tokens: bg=#FFFFFF text=#000000 accent=#00D395 border=#EAEAEA
