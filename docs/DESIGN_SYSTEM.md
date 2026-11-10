# ASISH Engineering — Neon Telemetry design system

## Public identity

**Engineering Intelligence × Motorsport × Applied AI**

This is the visual identity for the [GitHub profile](https://github.com/T-Bone47), not for the separate Minecraft Engineering Frontier project. The GitHub README remains a professional engineering profile with an ASISH OS technical terminal influence.

## Visual system (2026 refresh)

A visibly distinctive **graphite + electric cyan + racing red** identity. Graphite remains the quiet foundation; electric cyan replaces amber as the dominant technology signal. Race red gives motorsport identity and smaller domain accents distinguish individual projects.

| Token | Hex | Use |
|---|---|---|
| Deep graphite | `#080D15` | Hero background |
| Carbon | `#111D2B` | Hero gradient, panels |
| Electric cyan | `#22D3EE` | Primary strokes, signal traces, highlights |
| Ice cyan | `#67E8F9` | High-contrast labels and text on dark backgrounds |
| Racing red | `#D71D35` | Small hero motorsport accents, visual signature |
| Silver white | `#F5FAFF` | Hero title and important copy |
| Muted steel | `#BCCBD9` | Supporting copy |
| Signal green | `#34D399` | Semantically positive signal values |
| Graphite background | `#0D1117` | Supporting SVG backgrounds |

### Project-specific accent colours

| Project | Accent | High-contrast label |
|---|---|---|
| Live F1 Intelligence | `#0891B2` | `#67E8F9` |
| RaceMind AI | `#E11D48` | `#FDA4AF` |
| Sentinel AI | `#8B5CF6` | `#C4B5FD` |
| VyaparPulse AI | `#059669` | `#6EE7B7` |
| Football Intelligence OS | `#2563EB` | `#93C5FD` |
| ASISH OS | `#0891B2` | `#67E8F9` |

Avoid amber `#F59E0B` and `#FBBF24` as the main visual identity in profile SVGs; those belong to the prior design. Retain domain colours and genuine status semantics rather than indiscriminate recolouring of every data element.

## Layout and readability

1. The updated main SVG hero is the dominant colour moment and must remain visually readable at GitHub's actual profile width.
2. GitHub's page background itself is controlled by each visitor's GitHub theme; this repository changes **README artwork**, not GitHub's global interface theme.
3. Essential identity, featured projects and contact actions are native text/links that work without rendered artwork.
4. Animated project art is behind an expandable section; it should not overwhelm recruiter scanning.
5. Every project card has an accessible title and description.
6. Do not replace factual content with decorative fake metrics.
7. Preserve the separate ASISH OS and Minecraft-folio experiences.

## Maintenance and QA

- Check all 16 SVG assets as valid XML; new SVGs must have `title` and `desc` elements.
- Run `python3 scripts/validate_profile.py` before publishing.
- Inspect GitHub-rendered banners at normal desktop width and narrow viewport after deployment.
- Avoid relying on third-party images for essential information.
- Do not put arbitrary skill percentages or fabricated success indicators in profile art.
