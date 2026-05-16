# Linear — linear.app
Analyzed: 2026-05-16

## Snapshot
- Category: SaaS (Productivity)
- Feel: Cinematic, Precise, Tool-like
- Stack: React + Custom WebGL + Framer Motion

## Layout & Spacing
12-column grid housed within a central max-width container (estimated 1200px to 1440px). Section rhythm is exceptionally generous (160px to 240px vertical padding). Uses white space intentionally to let UI mockups float. Asymmetrical split patterns are common.

## Typography  
Clean, geometric/neo-grotesque sans-serif (Inter). Extreme contrast in scale with 72-80px hero text, 600-700 weight, and tight negative tracking (-0.02em). Body text is 18px-20px with 1.6 line height in muted grey.

## Color System
Deep dark mode (almost black #000000 to very dark grey). Primary text is off-white (#F4F4F5). Gradients and soft glows are used as accent colors. Cool temperature overall.

## Motion & Animation
Smooth, cinematic fade-ins, gentle upward translates. Scrolling triggers elements sequentially. Scroll-bound hardware-accelerated video/WebGL sections for product demonstrations. Snappy interactions on UI elements.

## Standout Patterns
Floating product UI screenshots that build dynamically as you scroll. Keyboard shortcut hints built into the marketing site.

## Hermes Implementation Notes
- Animation library to use: Framer Motion + Lenis for smooth scroll
- Key techniques: Fade-up with 10px Y offset, delay staggering
- Font stack: Inter, system-ui
- Color tokens: #000000 bg, #FAFAFA text, #A1A1AA muted