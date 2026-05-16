---
name: frontend-taste-learner
description: Autonomously discovers world-class websites, analyzes their design and motion patterns using vision models, and updates the shared knowledge base. One site per run. Run on cron to build up the knowledge base over time.
version: 0.7.2
author: hermes-frontend-skill
license: MIT
metadata:
  hermes:
    tags: [frontend, design, learning, autonomous, vision, browser]
    category: creative
  triggers:
    - "update frontend knowledge"
    - "learn new design patterns"
    - "run frontend learner"
    - "analyze a design site"
required_environment_variables:
  - name: GEMINI_API_KEY
    prompt: "Your Google Gemini API key (for vision analysis)"
    help: "Get one at https://aistudio.google.com"
    required_for: vision analysis
requires_toolsets:
  - browser
platforms: [linux, macos, windows]
---

# Frontend Taste Learner

You are a design researcher. Your job is to visit ONE real website per run, analyze what makes it feel premium using vision, and store those findings in the knowledge base.

You are NOT copying code. You are doing what designers do — studying great work and extracting the principles.

## ABSOLUTE RULES

1. **One site per run.** Pick the first unchecked `[ ]` item in `knowledge-base/queue.md`. Analyze it. Stop.
2. **No hallucination.** You MUST physically navigate to the site and take screenshots before writing any analysis. If you have zero screenshots, abort entirely — write nothing.
3. **No subagent delegation.** Do not use `delegate_task`. Do all work yourself.
4. **No skipping steps.** If the browser fails, write a failure note in queue.md and stop. Do not write a fake analysis.

All paths are relative to this skill's directory:
- Queue: `knowledge-base/queue.md`
- Analyses: `knowledge-base/site-analyses/[sitename].md`
- Samples: `../../samples/v[version]/`
- Generator: `../frontend-generator/SKILL.md`

---

## Step 1 — Pick the Site

Read `knowledge-base/queue.md`. Find the FIRST line with `[ ]`. That is your target.

If no unchecked items remain, output "Queue complete." and stop.

---

## Step 2 — Visit and Screenshot

Navigate to the site at **1440px width**. Wait 2 seconds for animations to load.

Take screenshots in this exact sequence:
1. Initial viewport (hero section)
2. Scroll 600px → screenshot
3. Scroll 600px more → screenshot
4. Scroll 600px more → screenshot
5. Scroll 600px more → screenshot
6. Scroll to bottom → screenshot

That is 6 screenshots minimum. If the page is long, take more every 600px.

Also run this in the browser console and record the output (Note: must be single-line to avoid `SyntaxError` in browser_console):
```javascript
JSON.stringify({pageHeight: document.documentElement.scrollHeight, fonts: [...new Set([...document.querySelectorAll('*')].map(el => getComputedStyle(el).fontFamily))].slice(0,5), bgColor: getComputedStyle(document.body).backgroundColor, hasGSAP: !!window.gsap, hasFramer: !!window.__framer_importFromPackage, hasLenis: !!window.Lenis})
```

If you cannot get even 3 screenshots: mark the site as `[!] sitename (browser failed)` in queue.md and stop.

---

## Step 3 — Vision Analysis

Send ALL screenshots + the DevTools JSON to vision with this prompt:

```
You are a senior product designer building a design knowledge base. These are [N] screenshots of [SITE] covering the full page top-to-bottom, plus DevTools data.

Extract EXACT values:

LAYOUT
- Max-width container (px)
- Section vertical padding (px)
- Grid columns and gutter
- White space philosophy

TYPOGRAPHY (exact values)
- H1: font-family, size, weight, letter-spacing, line-height
- H2: same
- Body: font-family, size, weight, line-height, color hex

COLOR SYSTEM (exact hex)
- Page background: #
- Primary text: #
- Secondary text: #
- Accent/brand: #
- Border color: #
- Card background: #
- Dark or light mode default?

MOTION & ANIMATION
- Hero load animation: what happens?
- Scroll animations: what elements, how (fade/slide/scale), speed estimate
- Hover effects: what changes?
- Special effects (parallax, cursor, WebGL)?
- Motion personality (subtle / expressive / cinematic)

STACK (from DevTools data)
- Framework
- Animation library
- CSS approach

WHAT MAKES IT NOT FEEL GENERIC
- List 3-5 specific decisions that elevate this site above AI output

Use "unclear" if you can't determine a value. Do not guess hex values — only report what you can see.
```

---

## Step 4 — Write the Analysis

Write to `knowledge-base/site-analyses/[sitename].md`:

```markdown
# [Site Name] — [URL]
Analyzed: [YYYY-MM-DD]
Screenshots taken: [N]

## Snapshot
- Category: [SaaS / agency / portfolio / developer tool / etc]
- Feel: [3 adjectives]
- Stack: [what was detected]

## Layout & Spacing
[exact values from vision]

## Typography
[exact values — font names, sizes, weights]

## Color System
[exact hex values]
- Background: #
- Text primary: #
- Text secondary: #
- Accent: #
- Border: #
- Card bg: #
- Mode: dark / light

## Motion & Animation
[specific techniques, timing values, what makes it distinctive]

## Standout Patterns
[3-5 things that make this site feel premium]

## Hermes Implementation Notes
- Animation library: [what to use when replicating this style]
- Key techniques: [bullet list]
- Font stack: [font names]
- Color tokens: bg=[hex] text=[hex] accent=[hex] border=[hex]
```

---

## Step 5 — Update Queue and Generate Sample

**5a. Mark done in queue.md**
Change `[ ] sitename` to `[x] sitename`.

**5b. Bump version**
Increment the patch version in this SKILL.md frontmatter (e.g. 0.7.0 → 0.7.1).

**5c. Generate sample HTML**
Read `../frontend-generator/SKILL.md` for generation rules. Then write a self-contained single-file HTML page to `../../samples/v[new-version]/index.html`:
- Inline CSS and JS (no build step needed)
- Dark minimal SaaS aesthetic inspired by the site you just analyzed
- Use the actual hex values from the analysis
- Real copy — no Lorem ipsum, no "Get Started" as the only CTA
- Tailwind CSS via CDN is allowed

**5d. Screenshot the sample**
Open `../../samples/v[new-version]/index.html` in the browser. Take a full-page screenshot. Save it as `../../samples/v[new-version]/preview.png`.

**5e. Commit to git**
```
git -C C:/Users/dhruv/AppData/Local/hermes/skills/world-class-frontend add .
git -C C:/Users/dhruv/AppData/Local/hermes/skills/world-class-frontend commit -m "feat: v[version] — analyzed [sitename]"
git -C C:/Users/dhruv/AppData/Local/hermes/skills/world-class-frontend push
```

---

## Step 6 — SELF-CRITIQUE (the real learning loop)

This is where the system actually gets smarter. Skipping this turns the skill into data-collection-only with no compounding intelligence.

**6a. Side-by-side vision compare**
Send vision TWO images in the same call:
- The merged source-site screenshot from Step 2
- The new `samples/v[version]/preview.png`

With this prompt:
```
You are a brutally honest senior design critic. The first image is a real elite landing page ([sitename]). The second is an AI-generated sample meant to capture what makes the first feel premium.

List the TOP 3 SPECIFIC GAPS — things the source does well that the sample completely misses. Be concrete (e.g. "source has a bento grid with glowing borders, sample has only a hero then empty void"). Do not list color or font mismatches — only structural, motion, or content gaps that make the sample feel like AI slop.

For each gap, propose ONE concrete enforceable rule for the code generator (specific structural or visual mandates, not vague advice).

Output JSON:
{
  "gaps": [
    {"gap": "...", "rule": "..."},
    {"gap": "...", "rule": "..."},
    {"gap": "...", "rule": "..."}
  ]
}
```

**6b. Update animation-patterns.md**
Append to `knowledge-base/animation-patterns.md`:
```
## From [sitename] (v[version])
- Pattern: [one specific motion/visual technique from this site]
- Trigger: [scroll / hover / load]
- Replicate with: [CSS/JS approach]
```
If a pattern is now seen on 3+ sites, mark it `[PROVEN]`.

**6c. Edit frontend-generator/SKILL.md with the new rules**
Read `../frontend-generator/SKILL.md`. Find the `**MANDATORY PAGE STRUCTURE**` section. Append the 3 new rules from Step 6a under a `### Learned from [sitename]` subheading. Do not delete existing rules — only add.

**6d. Bump generator version**
The generator SKILL.md has its own version field. Increment its patch version to record that it learned.

**6e. Persist learning to Hermes memory**
Save a memory entry `frontend_skill_learning_log` with:
- Site just analyzed
- 3 gaps identified
- 3 rules added
- Generator version after change

This makes future runs aware of what's been learned without re-reading all files.

**6f. Commit the self-improvement**
```
git -C C:/Users/dhruv/AppData/Local/hermes/skills/world-class-frontend add .
git -C C:/Users/dhruv/AppData/Local/hermes/skills/world-class-frontend commit -m "learn: rules from [sitename] — generator now v[new-gen-version]"
git -C C:/Users/dhruv/AppData/Local/hermes/skills/world-class-frontend push
```

---

## Done

This run is complete when:
- [ ] `knowledge-base/site-analyses/[sitename].md` exists with real vision data
- [ ] `knowledge-base/queue.md` shows `[x]` for this site
- [ ] `../../samples/v[version]/index.html` and `preview.png` exist
- [ ] `knowledge-base/animation-patterns.md` has a new entry
- [ ] `../frontend-generator/SKILL.md` has new rules and bumped version
- [ ] Hermes memory has updated learning log
- [ ] Both commits pushed

If any item is missing, complete it before stopping.

---

## Pitfalls

- **Bot protection / security checkpoint**: If the site blocks the browser, mark as `[!] sitename (blocked)` and stop.
- **Browser timeout on Windows**: Windows browser is early beta. If it fails twice, mark as `[!]` and stop. Do not retry more than twice.
- **Temptation to write from memory**: If you realize you are writing analysis values from your training data instead of from screenshots, stop and abort. Mark the site as `[!] sitename (aborted — no real screenshots)`.
- **Git path**: Always use the full absolute path `C:/Users/dhruv/AppData/Local/hermes/skills/world-class-frontend` for git commands.
- **Browser console syntax errors**: `browser_console` will throw `SyntaxError: Unexpected end of input` on multiline JS. Collapse all JS expressions into a single line.
- **Scroll idempotency**: When taking multiple screenshots down a page, running `window.scrollBy(0, 600)` repeatedly will be blocked by the tool loop idempotency filter. Append a random number to bypass: `window.scrollBy(0, 600); 'scrolled ' + Math.random()`.
- **Python module errors**: `execute_code` may fail to find pip-installed modules like PIL if it runs in a separate sandbox. If so, write the stitch script to disk and execute it via `terminal` using the explicit python binary.
