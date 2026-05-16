# Attio — https://attio.com
Analyzed: 2026-05-16

## Snapshot
- Category: SaaS / CRM
- Feel: Precise, Premium, Structured
- Stack: Custom / React

## Layout & Spacing
- Overall grid system: Explicit, visible grid utilizing a strict, multi-column layout with 1px light gray borders (#EAEAEA). Max-width around 1200px - 1440px.
- Section rhythm: Highly structured and generous vertical rhythm. Sections are separated by significant vertical space (160px - 240px padding), demarcated by horizontal grid lines and monospaced identifiers (e.g. `[01] POWERFUL PLATFORM`).
- White space philosophy: Extremely generous and intentional. Uses white space as a framing device.
- Alignment patterns: Center alignment for major narrative moments. Strict left-alignment for reading blocks anchored to the grid.

## Typography  
- Heading style: Massive H1 (72px - 84px), tight tracking (-0.02em), heavy weight (700 Bold or 800 ExtraBold). Clean geometric sans-serif.
- Body text approach: Clean, highly legible sans-serif. Likely 16px to 18px base size with generous line-height (1.6).
- Font personality: Geometric, precise, modern.
- Any notable type treatments: Use of monospaced fonts for labels, section indicators, and meta-data, creating a technical, structural feel.

## Color System
- Primary background color: Pristine white (#FFFFFF) dominating the page.
- Primary text color: High contrast deep charcoal or near black (#111111).
- Accent colors: Very subtle usage; reliance on UI element styling (drop shadows, borders) rather than loud brand colors.
- Dark/light mode approach: Light mode default, focusing on stark contrast and clean lines.

## Motion & Animation
- Overall motion philosophy: Functional, snappy, cinematic but not overwhelming.
- Detailed interactions: Interactive product mockups showing the UI in action, smooth fade-ups on scroll.

## Standout Patterns
- The visible 1px grid line aesthetic is a huge driver of the "premium technical" feel.
- "Product as the demo" - showing intricate, high-fidelity UI components interacting rather than static screenshots.

## Hermes Implementation Notes
- Animation library to use: Framer Motion / GSAP ScrollTrigger for complex sequencing.
- Key techniques: Reveal animations anchored to a strict CSS grid layout. Use pseudo-elements or explicit div borders for the 1px grid overlay.
- Font stack: Inter, Geist, or equivalent geometric sans-serif for headings/body; JetBrains Mono or similar for labels.
- Color tokens: Background: #ffffff, Text: #0f172a (slate-900), Borders: #e2e8f0 (slate-200).
