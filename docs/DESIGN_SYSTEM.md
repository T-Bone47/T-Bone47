# ASISH engineering profile — design system

## Identity
- Profile owner: Asish Oliver M / [T-Bone47](https://github.com/T-Bone47)
- Positioning: real-time engineering intelligence, AI/ML, motorsport software, simulation and practical software systems
- Two **distinct** portfolio experiences:
  - [ASISH OS](https://asish-os.vercel.app/): professional desktop-inspired workspace
  - [Minecraft-folio](https://github.com/T-Bone47/Minecraft-folio): independent voxel engineering universe (source; do not claim a live deployment before verification)

## Colour system

| Token | Hex | Use |
|---|---|---|
| Base graphite | #0D1117 | Background surfaces |
| Carbon | #161B22 | Layered panels |
| Signal amber | #F59E0B | Primary identity and selected highlights |
| Warm amber | #FBBF24 | Focus and terminal labels |
| Telemetry cyan | #22D3EE | Sparing technical and signal accents |
| Signal green | #34D399 | Only for genuinely meaningful success or status |
| Racing red | #D71D35 | Secondary motorsport-specific emphasis, not global primary |
| Silver white | #F9FAFB | Main text |
| Secondary text | #9CA3AF | Supporting labels |

Keep the overall profile neutral and restrained. Approximate guiding proportions: graphite/neutral 80%, amber/cyan 15%, semantic highlights 5%. Never rely on colour alone for meaning.

## Hierarchy and usability
1. One visual hero banner; no multiple full-height graphics above the introduction.
2. Clear identity and contact destinations immediately below.
3. A scannable table of five major engineering projects.
4. Separate presentation for the two portfolios; do not merge their identities.
5. Engineering evidence and optional animated ASCII gallery behind expandable details.
6. Final contact options with readable text links that do not depend on external badge services.

## Content integrity
- Never invent performance numbers, maturity status, employers, qualifications or achievements.
- Direct repository links should lead to public projects. Link Minecraft-folio to source until deployment is confirmed.
- Treat the decorative console and heatmap as illustrations; use the contribution snake only when its generated branch is available.
- Prefer native Markdown text for essential content.
- External image services should never be the only way to access a crucial link.
- Keep contact information user-controlled and publicly intended.

## Build / QA
- Run `python3 scripts/validate_profile.py` before updating README assets.
- The profile CI checks SVG XML structure and local image paths.
- On GitHub, inspect the rendered README in desktop and narrow viewport after merging.
- Review the optional animation gallery for motion overload; the core information works without it.
