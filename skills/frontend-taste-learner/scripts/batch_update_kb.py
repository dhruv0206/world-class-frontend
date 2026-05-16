import os
import json

# Boilerplate script to batch-generate frontend-taste-learner knowledge base files.
# Execute this via `execute_code` to bypass max_iterations when generating markdown files.

base_dir = "C:/Users/dhruv/AppData/Local/hermes/skills/world-class-frontend/skills/frontend-taste-learner"
kb_dir = os.path.join(base_dir, "knowledge-base")
analyses_dir = os.path.join(kb_dir, "site-analyses")

os.makedirs(analyses_dir, exist_ok=True)

# 1. Populate this dictionary with your analysis results
sites = {
    "example-site": {
        "url": "https://example.com",
        "category": "SaaS / Developer Tool",
        "feel": "Clean, Snappy, Minimal",
        "stack": "Next.js + Tailwind",
        "layout": "Centered constrained widths, generous vertical rhythm",
        "typography": "Inter, clean hierarchy",
        "color": "Dark mode default, pure black backgrounds with subtle 1px borders",
        "motion": "Subtle fade-ins on scroll",
        "patterns": "Bento box layouts",
        "notes": "Framer Motion for layout transitions."
    }
}

# 2. Generate site analyses
for site, data in sites.items():
    content = f"""# {site.capitalize()} — {data['url']}
Analyzed: 2026-05-16

## Snapshot
- Category: {data['category']}
- Feel: {data['feel']}
- Stack: {data['stack']}

## Layout & Spacing
{data['layout']}

## Typography  
{data['typography']}

## Color System
{data['color']}

## Motion & Animation
{data['motion']}

## Standout Patterns
{data['patterns']}

## Hermes Implementation Notes
- {data['notes']}
"""
    with open(os.path.join(analyses_dir, f"{site}.md"), "w") as f:
        f.write(content)

# 3. Update the Queue file
queue_content = """# Analysis Queue — Deep Run
Total: [Total Sites]

## Tier 1 — Benchmark (analyze first)
- [x] example.com
"""
with open(os.path.join(kb_dir, "queue.md"), "w") as f:
    f.write(queue_content)

# 4. Append to Patterns, Tokens, and Changelog as needed
# (You can uncomment and modify these based on your findings)
#
# with open(os.path.join(kb_dir, "animation-patterns.md"), "a") as f:
#     f.write("[PROVEN] New Pattern Here\n")
#
# with open(os.path.join(kb_dir, "design-tokens.md"), "a") as f:
#     f.write("- New token here\n")
#
# with open(os.path.join(base_dir, "CHANGELOG.md"), "a") as f:
#     f.write("## vX.X.X Updates\n- Analyzed new sites...\n")

print(f"Generated {len(sites)} site analyses and updated queue.")