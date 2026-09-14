# activetheory.net — https://activetheory.net
Analyzed: 2026-09-14
Screenshots taken: 1 (WebGL 100vh layout)

## Snapshot
- Category: agency / portfolio
- Feel: cinematic, immersive, cybernetic
- Stack: WebGL (custom engine)

## Layout & Spacing
- Max-width container: Full width / 100vw
- Section vertical padding: Full viewport / 100vh
- Grid columns and gutter: Custom 3D spatial layout, floating UI elements
- White space philosophy: Outer space void, using depth (z-axis) instead of traditional x/y padding.

## Typography
- H1: nbarchitekt / monospace, uppercase, ~36px, fw-400
- H2: nbarchitekt / monospace, uppercase, ~14px, fw-400
- Body: nbarchitekt / monospace, uppercase, ~12px, fw-400

## Color System
- Background: #000000 (with space/nebula particle effects)
- Text primary: #E6E6E6
- Text secondary: #9F82F9 (purple accent)
- Accent: #9F82F9
- Border: #4A4A4A (translucent glass borders)
- Card bg: #ffffff1a (glassmorphism)
- Mode: dark

## Motion & Animation
- Special effects: Heavy WebGL, 3D particle systems, floating glass panels with refraction.
- Motion personality: cinematic, highly expressive.

## Standout Patterns
- 3D Spatial Navigation: UI elements exist in Z-space, floating in front of a deep background rather than flat DOM nodes.
- Refractive Glass: Cards distort the complex particle background behind them.
- Monospace Cyber-aesthetic: Strict use of uppercase monospace fonts for all UI elements contrasts with the organic particle physics.

## Hermes Implementation Notes
- Animation library: Three.js / React Three Fiber for the 3D scene, Framer Motion for the UI overlay.
- Key techniques: 
  - Absolute positioning of a 3D canvas behind DOM UI.
  - Glassmorphism (`backdrop-filter: blur()`) on UI panels to interact with the 3D background.
- Font stack: nbarchitekt, monospace
- Color tokens: bg=#000000 text=#E6E6E6 accent=#9F82F9 border=#4A4A4A
