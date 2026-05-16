# Anthropic — https://anthropic.com
Analyzed: 2026-05-16

## Snapshot
- Category: AI Research / B2B SaaS
- Feel: Editorial, Academic, Confident
- Stack: Custom / React

## Layout & Spacing
- Overall grid system: Classic, robust 12-column grid. Max-width around 1280px to 1440px. Hero uses asymmetrical splits (e.g. 7-column headline, 1-column gap, 4-column secondary text).
- Section rhythm: Generous macro-whitespace between sections (120px to 160px padding), projecting confidence and slowing the pacing.
- White space philosophy: Generous and structural. White space frames the content tightly.
- Alignment patterns: Strict left-alignment dominates the page, creating order and readability. 

## Typography  
- Heading style: The defining feature of the site is the large, elegant Serif typeface (likely a custom cut or something like Recoleta/Tiempos) for main headlines. It's high-contrast and authoritative.
- Body text approach: Clean, highly legible geometric or neo-grotesque sans-serif (like Inter or a custom cut). ~16px-18px base size with generous line height (1.5).
- Font personality: The Serif provides an "Academic/Editorial/Newspaper" feel, while the Sans-serif provides "Modern Technology." The pairing is the core of their brand identity.
- Any notable type treatments: The stark contrast between the heavy, organic serif and the structural, minimal sans-serif.

## Color System
- Primary background color: Off-white/cream (e.g. #FDFDFD or #F7F7F5) instead of pure white, adding to the "print/editorial" feel.
- Primary text color: Deep charcoal/near-black (#1A1A1A).
- Accent colors: Peach/Warm Orange tones are heavily associated with the Anthropic brand, often used in subtle gradients, background blobs, or button hovers.
- Dark/light mode approach: Predominantly light mode, focusing on warmth and accessibility.

## Motion & Animation
- Overall motion philosophy: Extremely subtle, mature, and slow. 
- Detailed interactions: Slow fade-ups for text on scroll. Soft, organic, slow-moving ambient gradients/blobs in the background (the "Claude" aesthetic).

## Standout Patterns
- The "Editorial" Aesthetic: Moving away from the "Dark SaaS / Neon" trend, Anthropic uses serif fonts, cream backgrounds, and strict grid layouts to feel like a high-end magazine or a trusted academic institution. This builds immense trust.
- Organic Ambient Motion: The slow-moving, warm-colored abstract shapes in the hero section are a signature pattern that softens the technical nature of AI.

## Hermes Implementation Notes
- Animation library to use: CSS for simple fades, maybe WebGL/Canvas for the ambient organic background blobs.
- Key techniques: Typography pairings are crucial. Load a high-quality Serif (e.g., Playfair Display or Source Serif Pro) for H1/H2, paired with Inter.
- Font stack: Headings: Serif. Body: Sans-serif.
- Color tokens: Background: #FAFAFA, Text: #171717, Accent: #D97757 (warm peach/terracotta).
