# amie.so — https://amie.so
Analyzed: 2026-09-14
Screenshots taken: 6

## Snapshot
- Category: SaaS / productivity tool
- Feel: Joyful, clean, modern, crisp
- Stack: Inter var, CSS-based or lightweight custom animations (no GSAP/Framer detected)

## Layout & Spacing
- Max-width container (px): ~1200px
- Section vertical padding (px): ~160px
- Grid columns and gutter: 2-column pricing, ~32px gutter
- White space philosophy: Expansive and breathable. Lots of vertical space separating conceptual blocks.

## Typography
- H1: Inter var, ~72px, bold, tight letter-spacing (-2%), tight line-height (1.1)
- H2: Inter var, ~56px, bold, tight letter-spacing (-1.5%), line-height (1.1)
- Body: Inter var, ~18px, normal, line-height 1.5, color: #666666

## Color System
- Background: #FAFAFA
- Text primary: #000000
- Text secondary: #666666
- Accent: #1ea1f1 (bright blue button) / #00c853 (green checks)
- Border: #EAEAEA
- Card bg: #FFFFFF
- Mode: light

## Motion & Animation
- Hero load animation: Unclear from static, assumed fade/slide up
- Scroll animations: Unclear, no global scroll libs detected
- Hover effects: Button background darkens, scale transforms
- Special effects: Hand-drawn SVG arrows pointing at UI elements
- Motion personality: Subtle and native-feeling

## Standout Patterns
1. Handwritten/drawn SVG arrows and annotations layered over clean SaaS components, adding a human touch.
2. Two-tone H2 typography in feature sections to create contrast within a single sentence.
3. Huge central product showcase image immediately below the hero, grounded with subtle shadow.
4. "App Store Featured" / "Product of the day" micro-badges styled as pills above the hero headline.

## Hermes Implementation Notes
- Animation library: Native CSS transitions or light Framer Motion (use sparingly)
- Key techniques: 
  - Mix crisp typography with organic SVG doodles/arrows.
  - Large product image right below hero text.
  - Generous whitespace, light gray background (#FAFAFA) instead of pure white to make white cards pop.
- Font stack: Inter, sans-serif
- Color tokens: bg=#FAFAFA text=#000000 accent=#1ea1f1 border=#EAEAEA
