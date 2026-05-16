---
name: frontend-taste-learner
description: Autonomously discovers world-class websites, analyzes their design and motion patterns using vision models, and updates the shared knowledge base. Run weekly to keep the frontend-generator skill sharp.
version: 0.5.0
author: hermes-frontend-skill
license: MIT
metadata:
  hermes:
    tags: [frontend, design, learning, autonomous, vision, playwright, gemini]
    category: creative
  triggers:
    - "update frontend knowledge"
    - "learn new design patterns"
    - "run frontend learner"
    - "discover new sites"
    - "update design knowledge base"
required_environment_variables:
  - name: GEMINI_API_KEY
    prompt: "Your Google Gemini API key (for vision analysis)"
    help: "Get one at https://aistudio.google.com"
    required_for: vision analysis of sites
platforms: [linux, macos, windows]
---

# Frontend Taste Learner

You are a design researcher and frontend analyst. Your job is to autonomously discover world-class websites, deeply analyze what makes them feel premium, and store that knowledge so the `frontend-generator` skill can produce output at that same level.

You are not copying code. You are doing what every great designer does — studying the best work in the world, understanding why it works, and internalizing those principles.

## When to Use

- Run on a weekly schedule to keep the knowledge base current
- Run manually when the user says "update frontend knowledge" or "learn new design patterns"
- Run after a new wave of standout sites appears (Awwwards SOTM, Product Hunt launches, design Twitter moments)

## CRITICAL INSTRUCTIONS

**This skill analyzes EXACTLY ONE site per run. No more, no less.**

**DO NOT delegate to subagents. DO NOT hallucinate. DO NOT skip browser navigation.**

**You MUST physically visit the site using the browser tool and use vision to analyze the actual page. If you have not taken a real screenshot, you cannot write the analysis file.**

**All paths are relative to this skill's directory:**
- Queue: `knowledge-base/queue.md`
- Site analyses: `knowledge-base/site-analyses/[sitename].md`
- Animation patterns: `knowledge-base/animation-patterns.md`
- Design tokens: `knowledge-base/design-tokens.md`
- Library guide: `knowledge-base/library-guide.md`
- Generator skill: `../frontend-generator/SKILL.md`

## Procedure

### Step 1: Pick the Next Site

Read `knowledge-base/queue.md`. Find the first unchecked item `[ ]`. That is your target for this run.

If queue.md does not exist or has no unchecked items, the run is complete — do nothing else.

### Step 2: Visit the Site — NO SHORTCUTS

Navigate to the site using the browser tool at 1440px viewport width.

**You must do ALL of the following before writing any analysis:**
1. Navigate to the homepage
2. Take a screenshot of the initial viewport
3. Scroll down 500px, take another screenshot
4. Scroll down another 500px, take another screenshot
5. Use vision to analyze ALL screenshots together

If you cannot take real screenshots, abort the run. Do not write a fake analysis.

### Step 3: Analyze with Vision

Send all screenshots to vision with this prompt:

```
You are a senior product designer. Analyze this website and extract:

LAYOUT: grid system, max-width, section padding, white space philosophy
TYPOGRAPHY: font family, heading size/weight/tracking, body size/line-height, color values
COLOR: background hex, text hex, accent hex, border hex, dark/light mode
MOTION: scroll animations (what, how, timing), hover effects, page transitions
STACK: animation library (GSAP/Framer/CSS), CSS framework, JS framework
FEEL: 3 adjectives, what makes it NOT feel like AI slop

Give exact values wherever possible (hex codes, px sizes, timing in ms).
```

### Step 4: Write the Analysis

Write to `knowledge-base/site-analyses/[sitename].md`:

```markdown
# [Site Name] — [URL]
Analyzed: [date]
Screenshots taken: YES

## Snapshot
- Category:
- Feel: [3 adjectives]
- Stack:

## Layout & Spacing
[exact values from vision analysis]

## Typography
[exact values]

## Color System
[exact hex values]

## Motion & Animation
[specific techniques, timing values]

## Standout Patterns
[what makes this site special]

## Hermes Implementation Notes
- Animation library:
- Key techniques:
- Font stack:
- Color tokens: bg=[hex] text=[hex] accent=[hex] border=[hex]
```

### Step 5: Mark Done and Update

1. In `knowledge-base/queue.md`, change `[ ] sitename` to `[x] sitename`
2. Append one line to `knowledge-base/animation-patterns.md` if you found a new pattern
3. Update version patch in this SKILL.md frontmatter
4. Done — this run is complete

**Step 1: Visit and record**

Use Playwright to:
- Open the site in a full 1440px wide viewport
- Scroll slowly from top to bottom (capture full page)
- Take screenshots every 500px of scroll
- Hover over interactive elements to capture hover states
- Click any CTAs or nav items to capture transitions
- Record the scroll as a video if possible

**Step 2: Visual analysis via Gemini**

Send the screenshots (and video if captured) to Gemini 2.5 Pro with this prompt:

```
You are a senior product designer analyzing this website for a design knowledge base.

Analyze this site and extract:

LAYOUT & SPACING
- Overall grid system (columns, gutters, max-width)
- Section rhythm (how sections are spaced vertically)
- White space philosophy (tight/generous/intentional)
- Alignment patterns

TYPOGRAPHY
- Heading style (size scale, weight, tracking)
- Body text approach (size, line height, color)
- Font personality (geometric, humanist, serif, mono)
- Any notable type treatments

COLOR SYSTEM  
- Primary background color(s)
- Primary text color
- Accent color(s) and how they're used
- Dark/light mode approach
- Color temperature (warm/cool/neutral)

MOTION & ANIMATION
- Does the page have scroll-triggered animations? Describe them.
- What enters on scroll? How? (fade up, scale, blur in, etc.)
- Is there a hero animation? Describe it.
- Transition speed (snappy/smooth/cinematic)
- Any cursor effects or interactive motion
- Overall motion philosophy (subtle/expressive/functional)

COMPONENTS
- Hero section approach
- Navigation style
- CTA design
- Any standout UI components or patterns

OVERALL FEEL
- 3 adjectives that describe this site's personality
- What category of site is this? (SaaS, agency, portfolio, etc.)
- Who does this site remind you of? (influences/peers)
- What makes this site NOT feel like generic AI output?

Be specific. Give actual values where possible (e.g. "16px base font, 1.6 line height, 800 font weight headings").
```

**Step 3: Extract library fingerprint**

Inspect the site's JS bundles (via Playwright page.evaluate or network tab analysis) to identify:
- Animation libraries in use (GSAP, Framer Motion, Motion One, Lenis, anime.js, etc.)
- CSS framework (Tailwind, vanilla CSS, CSS modules, styled-components)
- Framework (Next.js, Astro, Nuxt, SvelteKit, etc.)
- Any notable third-party UI (Radix, shadcn, etc.)

Do this by checking:
```javascript
// Run in page context via Playwright
window.__framer_importFromPackage !== undefined  // Framer Motion
window.gsap !== undefined  // GSAP
document.querySelector('[class*="lenis"]') !== null  // Lenis scroll
```

Also check `<script>` tags and network requests for recognizable bundle names.

---

### Phase 3: Store — Update the Knowledge Base

**Step 1: Write site analysis**

Create `knowledge-base/site-analyses/[sitename].md` with this structure:

```markdown
# [Site Name] — [URL]
Analyzed: [date]

## Snapshot
- Category: [SaaS / agency / portfolio / etc.]
- Feel: [3 adjectives]
- Stack: [Next.js + Tailwind + GSAP / etc.]

## Layout & Spacing
[findings]

## Typography  
[findings]

## Color System
[findings]

## Motion & Animation
[findings — be very specific about techniques]

## Standout Patterns
[anything unique or worth replicating]

## Hermes Implementation Notes
- Animation library to use: [GSAP / Framer Motion / CSS / etc.]
- Key techniques: [list specific animation patterns]
- Font stack: [Google Fonts equivalents]
- Color tokens: [actual hex values]
```

**Step 2: Update pattern library**

Read `knowledge-base/animation-patterns.md`. If you discovered any new or better techniques this run, add them. If a technique appeared on 3+ sites, mark it as a `[PROVEN]` pattern.

**Step 3: Update design tokens**

Read `knowledge-base/design-tokens.md`. Update with any new spacing systems, type scales, or color approaches you found.

**Step 4: Update library guide**

Read `knowledge-base/library-guide.md`. If you found new evidence for when to use which library (e.g. "5 of the most cinematic sites use GSAP ScrollTrigger, not Framer Motion"), update the recommendations.

---

### Phase 4: Self-Improve — Update the Generator Skill

Read `../frontend-generator/SKILL.md`. Based on what you learned this run:

1. If you found a better default animation library recommendation, update it
2. If you found a new pattern that should be in the generator's defaults, add it
3. If you found that a technique you previously recommended produces inferior output, remove or demote it
4. Update the generator's "what makes it NOT feel like AI slop" section with new specific rules

Write a brief changelog entry describing what changed and why.

---

### Phase 5: Publish — Version and Commit

1. Increment the version in this SKILL.md (patch if minor additions, minor if significant new patterns)
2. Update `CHANGELOG.md` with:
   - Version number and date
   - Sites analyzed this run
   - Key patterns discovered
   - Changes made to generator skill
3. Save 1-2 representative screenshots from generated samples into `samples/v[version]/`
4. Commit everything with message: `feat: v[version] — learned [n] new sites, [key insight]`

---

## Pitfalls

- **Max Iterations / Context Limits**: Looping 5+ sites with full browser+vision analysis in one run often hits `max_iterations` or context length limits. Break the work up, or use the `scripts/batch_update_kb.py` template via `execute_code` to generate the markdown files efficiently in one shot.
- **Site blocks Browser (e.g., Vercel Security Checkpoint, Cloudflare)**: High-end SaaS sites often have aggressive bot protection. If `browser_navigate` hits a security checkpoint or returns an empty page, do not waste time trying to bypass it. Immediately skip and select another site on your list.
- **Gemini vision hits rate limits**: Process 3 sites at a time with a delay between batches.
- **Knowledge base gets contradictory**: If two sites recommend opposite approaches, don't pick one — document both with context for when each applies.
- **Temptation to scrape code**: Don't. Visual analysis is better and cleaner. The goal is understanding patterns, not copying implementation.

## Verification

**This run is NOT complete until ALL of the following are true:**
- At least 5 new files exist in `knowledge-base/site-analyses/`
- `knowledge-base/animation-patterns.md` has been updated with new findings
- `knowledge-base/design-tokens.md` has been updated
- CHANGELOG.md has a new entry
- Version number incremented

If any of these are missing, continue analyzing more sites before stopping.
