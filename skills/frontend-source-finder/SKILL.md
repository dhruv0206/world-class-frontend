---
name: frontend-source-finder
description: Autonomously discovers new world-class websites worth analyzing. Scrapes Awwwards, ProductHunt, design Twitter, and SiteInspire to find trending elite sites and appends them to the analysis queue. Runs weekly via cron to keep the pipeline supplied with fresh inspiration.
version: 0.1.0
author: hermes-frontend-skill
license: MIT
metadata:
  hermes:
    tags: [frontend, discovery, autonomous, scraping, queue]
    category: creative
  triggers:
    - "find new design sites"
    - "update queue with new sites"
    - "discover trending websites"
    - "refill design queue"
requires_toolsets:
  - browser
platforms: [linux, macos, windows]
---

# Frontend Source Finder

Your job is to find NEW world-class websites and add them to the analysis queue so `frontend-taste-learner` always has fresh material. You are the eyes of the system.

## Rules

1. **One discovery run per invocation.** Do not loop.
2. **Real browsing only.** Visit the source sites with the browser tool. Do not guess URLs from memory.
3. **Quality over quantity.** Add 5-10 genuinely elite new sites per run, not 50 mediocre ones.
4. **No duplicates.** Read existing `knowledge-base/queue.md` first and skip anything already there (checked or unchecked).

## Procedure

### Step 1 — Pick a source

Rotate through these sources. Check Hermes memory for `frontend_source_finder_last_source` to know which one to use this run.

| Source | URL | Why |
|---|---|---|
| Awwwards SOTD | https://www.awwwards.com/websites/sites_of_the_day/ | Top jury-curated site each day |
| Awwwards Honorable | https://www.awwwards.com/websites/honorable_mentions/ | High-quality runners-up |
| SiteInspire | https://www.siteinspire.com/websites | Curated design directory |
| Godly | https://godly.website/ | Inspirational web design |
| Land-book | https://land-book.com/ | Landing page gallery |
| Lapa Ninja | https://www.lapa.ninja/ | Landing page inspiration |
| One Page Love | https://onepagelove.com/inspiration | Single-page sites |
| Httpster | https://httpster.net/ | Aggregated design feed |
| Mindsparkle Mag | https://mindsparklemag.com/ | Editorial design magazine |
| ProductHunt featured | https://www.producthunt.com/ | New product launches (filter for design quality) |

If memory is empty, start with Awwwards SOTD.

### Step 2 — Navigate and scan

Open the chosen source in the browser. Wait 2 seconds. Take 3 screenshots scrolling down.

Use vision to extract featured site URLs from the screenshots:
```
You are scanning a design inspiration gallery. List the 10 highest-quality websites featured on this page. For each: site URL/name, one-sentence "why it stands out" justification. Skip anything that looks generic, low-effort, or AI-generated. Prefer sites with: unique typography, custom interactions, distinctive layouts, premium feel.

Output JSON:
{
  "sites": [
    {"url": "...", "name": "...", "why": "..."}
  ]
}
```

### Step 3 — Filter against existing queue

Read `../frontend-taste-learner/knowledge-base/queue.md`. Build a set of all domains already listed (whether `[ ]`, `[x]`, or `[!]`). Drop any candidates that are already present.

If after deduping you have fewer than 5 candidates, run Step 1-2 again with a different source.

### Step 4 — Append to queue

Open `../frontend-taste-learner/knowledge-base/queue.md`. At the bottom, add:

```
## Tier — Discovered [YYYY-MM-DD] from [source]
- [ ] site1.com — [why]
- [ ] site2.com — [why]
...
```

### Step 5 — Persist state

Update Hermes memory `frontend_source_finder_last_source` to the source used this run, so the next invocation rotates to the next one.

### Step 6 — Commit

```
git -C C:/Users/dhruv/AppData/Local/hermes/skills/world-class-frontend add .
git -C C:/Users/dhruv/AppData/Local/hermes/skills/world-class-frontend commit -m "queue: +[N] sites from [source]"
git -C C:/Users/dhruv/AppData/Local/hermes/skills/world-class-frontend push
```

## Pitfalls

- **Awwwards may rate-limit or block bots.** If blocked, skip to the next source in rotation, don't retry.
- **ProductHunt is mostly product launches, not design showcases.** Filter aggressively — only add sites where the *website itself* is exceptional, not just the product.
- **Don't add competitor SaaS sites blindly.** "Another email tool's landing page" is not necessarily elite. The bar is: would a senior designer screenshot this for inspiration?
