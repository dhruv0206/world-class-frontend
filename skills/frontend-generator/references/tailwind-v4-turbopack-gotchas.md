# Tailwind v4 + Next.js Turbopack Gotchas

## 1. Plugin Incompatibility & Caching Errors
When migrating to or using Tailwind v4's new `@theme` architecture, older v3 plugins like `tailwindcss-animate` can throw `CssSyntaxError: Can't resolve...` during Next.js Turbopack compilation. 

**The Fix:**
1. Do not use `tailwindcss-animate` with Tailwind v4. Instead, define your animations using pure CSS within the `@theme` block:
   ```css
   @theme {
     --animate-shine: shine 8s linear infinite;
     @keyframes shine {
       0% { background-position: 0% 0%; }
       50% { background-position: 100% 100%; }
       100% { background-position: 0% 0%; }
     }
   }
   ```
2. **Turbopack Cache Busting:** If you trigger a CSS compilation error, Turbopack aggressively caches it. Even if you fix the `globals.css` file, `npm run dev` might continue to throw the same error. You **must** manually clear the cache before restarting:
   ```bash
   rm -rf .next
   npm run dev
   ```

## 2. Port Conflicts
If a Next.js server crashes or runs in the background and holds port 3000, `npm run dev` will auto-fallback to 3001, 3002, etc. If caching errors persist across ports, kill the node process (`taskkill //PID <id> //F` on Windows or `kill -9 <pid>`) and run on a fresh port `npm run dev -- -p 3005`.

## 3. GPU-Accelerated Border Masks (React State Alternative)
Avoid using `framer-motion` and React `onPointerMove` state for complex hover glow effects on grids (as seen in some Magic UI components) because it causes main-thread blocking. 
Instead, use CSS hardware acceleration and `mask-composite`:
```css
.mask-hollow {
  mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  mask-composite: exclude;
  -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
}
.hw-accel {
  will-change: transform, opacity;
  transform: translateZ(0);
}
```
Apply this to a `div` with a radial gradient background that transitions opacity on group-hover.