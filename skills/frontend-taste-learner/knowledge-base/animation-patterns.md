# Animation Patterns

Patterns discovered from analyzing world-class sites. Marked `[PROVEN]` when seen on 3+ elite sites.

---

## Entrance Animations

### Fade Up — The Standard [PROVEN]
The most common pattern on premium sites. Simple, never wrong.
```js
// Framer Motion
initial={{ opacity: 0, y: 16 }}
animate={{ opacity: 1, y: 0 }}
transition={{ duration: 0.5, ease: [0.16, 1, 0.3, 1] }}
```
Use for: hero text, section headings, any primary content

### Staggered List Entrance [PROVEN]
When a grid or list of items enters, stagger them. 0.08s between items feels natural.
```js
// Framer Motion container
variants={{
  hidden: {},
  show: { transition: { staggerChildren: 0.08 } }
}}
// Each child
variants={{
  hidden: { opacity: 0, y: 12 },
  show: { opacity: 1, y: 0, transition: { duration: 0.4, ease: [0.16, 1, 0.3, 1] } }
}}
```
Use for: feature grids, testimonial lists, pricing cards

### Blur In
Seen on more expressive/editorial sites. Adds depth.
```js
initial={{ opacity: 0, filter: 'blur(8px)' }}
animate={{ opacity: 1, filter: 'blur(0px)' }}
transition={{ duration: 0.6, ease: 'easeOut' }}
```
Use for: hero images, background elements, secondary content

---

## Scroll Animations

### ScrollTrigger Fade Up (GSAP) [PROVEN]
```js
gsap.from(element, {
  scrollTrigger: {
    trigger: element,
    start: 'top 85%',
  },
  opacity: 0,
  y: 20,
  duration: 0.6,
  ease: 'power3.out'
})
```

### Framer Motion whileInView [PROVEN]
```jsx
<motion.div
  initial={{ opacity: 0, y: 20 }}
  whileInView={{ opacity: 1, y: 0 }}
  viewport={{ once: true, margin: '-50px' }}
  transition={{ duration: 0.5, ease: [0.16, 1, 0.3, 1] }}
>
```
Use `once: true` — elements shouldn't re-animate on scroll up.

---

## Hover Effects

### Subtle Scale [PROVEN]
```css
transition: transform 0.2s ease;
&:hover { transform: scale(1.02); }
```
Never go above 1.03. Anything more looks cheap.

### Border Glow (Dark Themes)
```css
transition: border-color 0.2s ease, box-shadow 0.2s ease;
&:hover {
  border-color: rgba(255,255,255,0.15);
  box-shadow: 0 0 0 1px rgba(255,255,255,0.05);
}
```

### Text Underline Slide
```css
background: linear-gradient(currentColor, currentColor) bottom / 0 2px no-repeat;
transition: background-size 0.3s ease;
&:hover { background-size: 100% 2px; }
```

---

## Navigation

### Backdrop Blur Nav [PROVEN]
```css
position: fixed;
top: 0;
background: rgba(0,0,0,0); /* transparent by default */
backdrop-filter: blur(0px);
border-bottom: 1px solid transparent;
transition: all 0.3s ease;

/* on scroll — add via JS */
.scrolled {
  background: rgba(10,10,10,0.8);
  backdrop-filter: blur(12px);
  border-bottom-color: rgba(255,255,255,0.06);
}
```

---

## Page Transitions

### Fade Between Pages (Next.js)
```jsx
// Using Framer Motion AnimatePresence in layout.tsx
<AnimatePresence mode="wait">
  <motion.div
    key={pathname}
    initial={{ opacity: 0 }}
    animate={{ opacity: 1 }}
    exit={{ opacity: 0 }}
    transition={{ duration: 0.2 }}
  >
    {children}
  </motion.div>
</AnimatePresence>
```

---

## Easing Reference

| Name | Values | Use |
|------|--------|-----|
| Snappy entrance | `[0.16, 1, 0.3, 1]` | Most UI entrances |
| Smooth out | `[0.25, 0.46, 0.45, 0.94]` | Exits, hover releases |
| Cinematic | `[0.76, 0, 0.24, 1]` | Dramatic reveals |
| Spring (Framer) | `type: 'spring', stiffness: 400, damping: 30` | Interactive elements |

---

*This file is updated by `frontend-taste-learner` each run.*
*Last updated: bootstrap*
# Animation Patterns
[PROVEN] Cinematic Scroll-jacking (Arc)
[PROVEN] Border beam animations (Resend)
[PROVEN] Spring-based micro-interactions (Raycast)
