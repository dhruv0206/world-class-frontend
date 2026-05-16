# Design Tokens

Spacing systems, type scales, and color approaches extracted from world-class sites.

---

## Dark Theme Color Systems

### Near-Black (Linear-style)
```
Background:     #0a0a0a
Surface:        #111111
Surface raised: #161616
Border:         rgba(255,255,255,0.08)
Border hover:   rgba(255,255,255,0.14)
Text primary:   #f4f4f5
Text secondary: #a1a1aa
Text tertiary:  #71717a
Accent:         #5b6af0  (or brand color)
```

### Charcoal (Vercel-style)
```
Background:     #000000
Surface:        #0d0d0d
Border:         #1a1a1a
Text primary:   #ededed
Text secondary: #888888
Text tertiary:  #555555
```

### Warm Dark (editorial)
```
Background:     #0f0e0d
Surface:        #161513
Border:         rgba(255,248,240,0.08)
Text primary:   #f8f4ef
Text secondary: #a89f96
```

---

## Light Theme Color Systems

### Clean White (Stripe-style)
```
Background:     #ffffff
Surface:        #f6f9fc
Border:         #e3e8ee
Text primary:   #1a1f36
Text secondary: #697386
Text tertiary:  #8792a2
Accent:         #635bff
```

### Off-White (warm minimal)
```
Background:     #fafaf9
Surface:        #f5f4f0
Border:         #e7e5e0
Text primary:   #1c1c1a
Text secondary: #78716c
```

---

## Typography Scales

### Display-focused (hero-heavy pages)
```
Display:  clamp(48px, 6vw, 80px), weight 600, tracking -0.02em, lh 1.1
H1:       clamp(32px, 4vw, 52px), weight 600, tracking -0.015em, lh 1.15
H2:       clamp(24px, 3vw, 36px), weight 600, tracking -0.01em, lh 1.2
H3:       20px, weight 600, tracking -0.005em, lh 1.3
Body:     16px, weight 400, tracking 0, lh 1.6
Small:    14px, weight 400, tracking 0, lh 1.5
```

### Content-focused (documentation, product)
```
H1:   28px, weight 600, tracking -0.01em
H2:   22px, weight 600, tracking -0.005em
H3:   18px, weight 600
Body: 15px, weight 400, lh 1.7
```

---

## Spacing Systems

### 8px base (most common) [PROVEN]
```
4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96, 128
```
In Tailwind: default scale covers this well

### Section vertical rhythm
```
Section padding Y:  py-24 (96px) to py-40 (160px)
Section gap:        gap-16 to gap-24 between major sections
Content max-width:  max-w-6xl (1152px) or max-w-7xl (1280px)
Content padding X:  px-6 mobile, px-8 tablet, container centered desktop
```

---

## Font Pairings

### Geometric sans (developer tools, SaaS)
- Primary: Inter, Geist, or DM Sans
- Mono: JetBrains Mono, Geist Mono, or Fira Code (for code snippets)

### Editorial (agencies, creative tools)
- Primary: Neue Haas Grotesk → use Haas Grot Text (or similar)
- Google Fonts alt: Plus Jakarta Sans, Outfit

### Minimal utility (product dashboards)
- Primary: Inter
- Everything at 14-15px, weight variation does the hierarchy work

### High-end / distinctive
- Primary: Fraunces, Editorial New → use Playfair Display as fallback
- Pairing: with a clean sans for body

---

*Last updated: bootstrap*
*Updated by: frontend-taste-learner*
# Design Tokens
- Pure Black (#000000) for SaaS dark mode (Linear, Resend, Vercel)
- High-contrast 1px borders (#333333 on #000000)
- Typography: Geist, Inter, system-ui

- Deep space dark background (#0D1117) with glowing accents (GitHub)
- Typography: Mona Sans variable font (GitHub), IBM Plex Mono (Replit)
