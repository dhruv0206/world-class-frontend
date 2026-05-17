# Premium UI Architecture Patterns

During competitive analysis of modern React UI libraries (shadcn v4, Magic UI, Aceternity), the following architectural imperatives were identified to achieve elite visual fidelity without sacrificing performance or accessibility.

When generating components or analyzing sites for the Aether UI standard (or equivalent), enforce these rules:

## 1. Architectural Foundation (The "shadcn v4" Standard)
- **`asChild` Polymorphism:** All interactive components MUST support `asChild` composition using Radix UI's `<Slot>` component. This allows wrapping Next.js `<Link>` tags without breaking semantic HTML.
  ```tsx
  const Comp = asChild ? Slot.Root : "button"
  return <Comp {...props} />
  ```
- **`data-slot` Targeting:** Avoid deep, complex Tailwind class cascading. Assign a `data-slot` attribute (e.g., `data-slot="dialog-content"`) to every component element. This allows clean, universal overrides in global CSS.
- **Tokenized Class Prefixes:** Decouple structure from visual style. Use tokenized class names (e.g., `cn-dialog-content`) and handle the actual Tailwind utility mapping in a global CSS token sheet, allowing effortless theme swapping.

## 2. Micro-Aesthetics & Performance (The "Magic UI" Corrections)
- **The Cost of React State:** Do NOT use Framer Motion `useMotionValue` or `useSpring` attached to React `onPointerMove` events for hover/glow effects. Updating React state on every mouse pixel movement blocks the main thread and causes severe layout jank when rendering grids of components.
- **CSS XOR Masking:** Achieve "shine" and "glowing border" effects using pure CSS gradients combined with CSS Masking, rather than complex DOM structures.
  ```css
  /* The "XOR" masking trick for inside-out shining borders */
  mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  maskComposite: exclude; /* or WebkitMaskComposite: "xor" */
  ```
- **Offset Paths:** For border-beam/tracing animations, prefer the CSS `offset-path: rect(...)` property paired with vanilla JS over heavy React-calculated geometry.
- **Hardware Acceleration:** Any element animating large gradients or complex paths MUST explicitly define its composite layer using `will-change: transform, opacity` or `transform: translateZ(0)` to prevent full document repaints.