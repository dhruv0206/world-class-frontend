# Premium UI Component Architecture & Motion Patterns

Extracted from deep autopsies of shadcn/ui (v4) and Magic UI, to be used when generating or evaluating high-end React UI components.

## Architecture & DX (The shadcn v4 standard)
- **Headless Primitives**: Delegate to `@base-ui/react` or Radix `<Slot>` for flawless `asChild` polymorphism. Avoid manual `React.forwardRef` and prop-drilling boilerplate.
- **The `data-slot` Pattern**: Attach `data-slot="[component-name]"` to every rendered element (e.g., `data-slot="dialog-content"`). This allows consumers to write clean global CSS overrides without battling Tailwind specificity.
- **Tokenized Class Variants**: Use prefixed classes (e.g., `cn-button-variant-default`) instead of hardcoded inline utilities (`bg-primary text-primary-foreground`) to enable seamless, pure-CSS theme swapping.

## Micro-Aesthetics & Performance (Beyond Magic UI)
- **XOR CSS Masking for Shines**: For premium glowing or shining borders, do not use `border-color`. Use a background radial gradient and punch out the center using `mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0); maskComposite: exclude;` (or `WebkitMaskComposite: xor`).
- **High-Performance Tracing**: Use CSS `offset-path: rect(...)` for "border beam" effects where a light particle perfectly traces a container's edge, bypassing heavy JS coordinate calculations.
- **React State vs. CSS Variables**: Never bind Framer Motion `useMotionValue` or `useSpring` directly to an `onPointerMove` event for grids of interactive cards—it causes massive JS main-thread blocking. Abstract hover physics to pure CSS variables updated by a single, throttled vanilla JS event listener at the document level.
- **Hardware Acceleration**: Always apply `will-change: transform, opacity` or `transform: translateZ(0)` to elements with large animated gradients to force GPU rendering and prevent layout repaints.