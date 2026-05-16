# hermes-frontend-skill

A self-learning Hermes skill system that autonomously discovers world-class websites, analyzes their design and motion patterns, and generates production-grade Next.js frontends that actually look and feel like the real thing.

## Skills

### `frontend-taste-learner`
Runs on a schedule. Autonomously discovers new world-class sites, watches their animations, extracts design patterns using vision models, and updates the shared knowledge base. Gets smarter over time.

### `frontend-generator`
Runs on demand. Reads from the accumulated knowledge base and generates Next.js code with the right animation stack for your brief. Output should not feel like AI slop.

## How it works

```
Learner (weekly):
  Discover new elite sites → Watch via Playwright → Analyze via Gemini vision
  → Extract patterns → Update knowledge base → Update generator skill

Generator (on demand):
  Parse brief → Load relevant patterns → Choose animation stack
  → Generate Next.js → Screenshot → Evaluate → Deliver
```

## Knowledge Base

The `knowledge-base/` directory grows over time:
- `site-analyses/` — per-site breakdowns of design decisions
- `animation-patterns.md` — specific techniques and when to use them
- `design-tokens.md` — spacing systems, type scales, color approaches
- `library-guide.md` — when to reach for GSAP vs Framer Motion vs CSS

## Releases

Each weekly run publishes a new version with:
- Changelog of what was learned
- Sample screenshots of generated output
- Updated skill files

## Setup

1. Install [Hermes Agent](https://hermes-agent.nousresearch.com)
2. Clone this repo into your Hermes skills directory
3. Set required environment variables (see each skill's SKILL.md)
4. Run `frontend-taste-learner` once to bootstrap the knowledge base
5. Use `frontend-generator` on demand

## License

MIT
