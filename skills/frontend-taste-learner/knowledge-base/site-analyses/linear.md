# Linear — https://linear.app
Analyzed: 2026-05-16

## Snapshot
- Category: SaaS / Product Management
- Feel: Precision, Dark, Opinionated
- Stack: Custom / React

## Layout & Spacing
- Overall grid system: 12-column grid constrained by a central max-width container (~1200px - 1280px). Uses 50/50 or 40/60 splits for feature sections.
- Section rhythm: Massive vertical gaps between major sections (160px to 240px padding), forcing focus on one concept at a time.
- White space philosophy: Generous and highly intentional negative space. Because the background is dark, the empty space acts as a void framing illuminated UI mockups.
- Alignment patterns: Strong left-alignment for typography. Center alignment reserved for hero and final CTA to create symmetry.

## Typography  
- Heading style: Clean neo-grotesque sans-serif. H1 is large (~72px) with tight tracking and a medium-to-bold weight.
- Body text approach: ~18px to 20px base size, highly legible with a slightly relaxed line height (1.5 - 1.6). Text color is often a muted gray/silver against the dark background, with white used for emphasis.
- Font personality: Geometric, engineered, objective.
- Any notable type treatments: The typography feels "invisible" — it doesn't draw attention to itself, serving purely as a vehicle for clarity.

## Color System
- Primary background color: Deep, rich black/very dark gray (e.g., #000000 or #0a0a0a).
- Primary text color: Stark white (#FFFFFF) for headers, muted silver/gray (#8A8F98) for body text.
- Accent colors: Very restrained use of color (subtle purples or blues), usually confined to the UI mockups or specific active states.
- Dark/light mode approach: Dark mode native. The brand identity is heavily tied to the dark, glowing aesthetic.

## Motion & Animation
- Overall motion philosophy: Smooth, highly performant, and purposeful. Not overly bouncy.
- Detailed interactions: Likely uses scroll-triggered fade-ups and subtle scaling for mockups entering the viewport.

## Standout Patterns
- The "Dark SaaS" benchmark: Linear practically defined this aesthetic. Deep blacks, glowing UI elements, stark white headers.
- Hero UI Mockup: A highly detailed, realistic (often interactive or video-based) UI mockup directly beneath the hero text.

## Hermes Implementation Notes
- Animation library to use: Framer Motion.
- Key techniques: `opacity: 0` to `opacity: 1` with `y: 20` to `y: 0` on scroll using `whileInView`.
- Font stack: Inter, Roboto, or a custom geometric sans-serif.
- Color tokens: Background: #000000, Text-Primary: #ffffff, Text-Secondary: #a1a1aa (zinc-400).
