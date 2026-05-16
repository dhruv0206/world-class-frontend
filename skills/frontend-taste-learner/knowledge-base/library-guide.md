# Animation Library Guide

When to reach for which library. Updated by `frontend-taste-learner`.

---

## Decision Tree

```
Is the site cinematic with scroll storytelling? (agency, marketing, editorial)
  → GSAP + ScrollTrigger

Is it a SaaS product UI with lots of interactive components?
  → Framer Motion

Is it ultra-minimal where animations should be invisible?
  → Motion One or CSS transitions

Is smooth scroll important to the experience?
  → Add Lenis on top of whichever you choose
```

---

## GSAP + ScrollTrigger

**Best for**: agency sites, expressive marketing pages, scroll-driven storytelling

**Strengths**:
- Most precise timeline control
- ScrollTrigger is unmatched for scroll-driven animation
- Pinning sections, scrub animations, parallax
- Works outside React (good for vanilla Next.js pages)

**Weaknesses**:
- Heavier (34kb min+gz)
- More verbose for simple cases
- License: free for most uses, paid for some commercial contexts (check gsap.com/licensing)

**When NOT to use**:
- Simple entrance animations only
- Component-level interactive animations
- When bundle size is a concern

**Install**: `npm install gsap`

---

## Framer Motion

**Best for**: SaaS products, component-driven UIs, interactive elements

**Strengths**:
- Declarative — works naturally with React component model
- `whileHover`, `whileTap`, `whileInView` are elegant
- AnimatePresence for route transitions
- Layout animations (FLIP) built in
- Great for shared element transitions

**Weaknesses**:
- Heavier than Motion One (~50kb)
- Can cause hydration issues if not handled correctly in Next.js
- Less control for complex scroll timelines

**When NOT to use**:
- Complex scroll storytelling (use GSAP)
- When you need maximum performance on low-end devices

**Install**: `npm install framer-motion`

**Next.js note**: Use `'use client'` directive. For SSR-safe animations, use `useEffect` to set `isClient` flag before rendering animated components.

---

## Motion One

**Best for**: Minimal sites, performance-critical apps, subtle UI polish

**Strengths**:
- Tiny (18kb)
- Web Animations API based — hardware accelerated
- Simple API for most use cases

**Weaknesses**:
- Less ecosystem / fewer examples
- No built-in React primitives (use `@motionone/react`)

**Install**: `npm install @motionone/dom`

---

## Lenis (Smooth Scroll)

**Always add when**: The site has meaningful scroll animations or the scroll experience matters to the design.

**Install**: `npm install lenis`

```js
// In layout.tsx or a client provider
import Lenis from 'lenis'
import { useEffect } from 'react'

useEffect(() => {
  const lenis = new Lenis()
  function raf(time: number) {
    lenis.raf(time)
    requestAnimationFrame(raf)
  }
  requestAnimationFrame(raf)
  return () => lenis.destroy()
}, [])
```

---

## CSS Transitions Only

**Use when**:
- The design is truly minimal and animations should be nearly invisible
- You want zero JS animation overhead
- Simple hover states, color transitions, opacity changes

**Don't use when**:
- You need scroll-triggered animations
- You need stagger or sequenced animations
- Any animation that requires JavaScript timing

---

## Combinations That Work Well

| Primary | Add-on | Use case |
|---------|--------|----------|
| Framer Motion | Lenis | SaaS landing with scroll sections |
| GSAP | Lenis | Agency / expressive marketing |
| CSS | — | Ultra-minimal, performance-first |

**Never combine**: Framer Motion + GSAP in the same project. Pick one animation controller.

---

*Last updated: bootstrap*
*Updated by: frontend-taste-learner*
