# High-CTR Creator Thumbnail Skill

English | [简体中文](README.md)

Create high-CTR thumbnails and creator covers for Xiaohongshu, WeChat Channels, Douyin, YouTube, and YouTube Shorts from real portraits, real products, and real screenshots.

> **Real assets × click-driving structures × multi-platform ratios × copy-ready prompts**

Start from a proven visual system instead of a blank canvas: describe the style you want (for example, “warm handwritten collage”), set the ratio, attach the assets, and replace the title. Codex then follows the production and QA workflow. `S01–S10` are optional catalog labels.

> Current version: `v0.3.4`. “High-CTR” describes the design objective and does not promise views, click-through rate, virality, or commercial results. The first real finished cover is included as a style demonstration. Rights for third-party people, brands, and interface imagery are not established, so the example is not presented as commercially cleared.

## What it does

- Includes ten click-driving creator-cover systems for people, products, knowledge, resources, news, and UI showcases.
- Builds hierarchy around one-second comprehension, small-preview readability, and visible real proof.
- Supports five platform/content presets across horizontal and vertical layouts.
- Separates exact-use assets, style-only references, and generatable decoration.
- Prevents AI redraws or substitutions of real screenshots, products, logos, data, and people.
- Covers headline zones, real UI collages, portrait cutouts, and white-to-transparent title transitions.
- Includes QA guidance for fidelity, rights language, feed-size readability, dimensions, and export.
- Includes dependency-free Python helpers for presets and PNG/JPEG dimension checks.
- Includes bilingual copy-ready prompt templates and a prompt builder.

## Thumbnail examples

See the full [style catalog](create-social-thumbnails/references/style-catalog.md). Each table prompt is a directly reusable starting point; attach the real assets and replace the title, ratio, and subject details.

| ID | Preview | Style | Best for | Prompt example |
|---|---|---|---|---|
| `S01` | <a href="demos/S01-warm-handwritten-collage-6x7/preview.png"><img src="demos/S01-warm-handwritten-collage-6x7/preview.png" width="180" alt="S01 Warm Handwritten Collage thumbnail"></a> | Warm Handwritten Collage | Resource packs, templates, design collections | `$create-social-thumbnails Warm handwritten collage at 6:7 with ivory handwritten type, a real screenshot collage, a real portrait cutout, and a white title gradient; do not generate fake assets.` |
| `S02` | Coming soon | Face-led High CTR | Personal brands, tutorials, reactions | `$create-social-thumbnails Face-led high CTR at 16:9. Let the real person occupy about 40%, use a short high-contrast title, and keep only one real proof image.` |
| `S03` | Coming soon | Clean UI Showcase | SaaS, apps, Figma, workflows | `$create-social-thumbnails Clean UI showcase at 4:3 with a light spacious background, one dominant real product interface, and at most two supporting cards.` |
| `S04` | Coming soon | Dark Tech Neon | AI, coding, automation, fintech | `$create-social-thumbnails Dark tech neon at 16:9 with a near-black field, one neon accent, and a real dashboard or code screen; do not invent data.` |
| `S05` | Coming soon | Bold Number List | Collections, rankings, comparisons | `$create-social-thumbnails Bold number list at 3:4. Make the quantity dominant, arrange 3–6 real examples below it, and use only one emphasis mark.` |
| `S06` | Coming soon | Before–After Split | Redesigns, transformations, tests | `$create-social-thumbnails Before-after split at 16:9 with real before-and-after images, matched crops, and clear labels; do not exaggerate the result.` |
| `S07` | Coming soon | News Commentary | News, analysis, explainers | `$create-social-thumbnails News commentary at 16:9 with a real topic image and a concise factual angle; do not fabricate quotes or conclusions.` |
| `S08` | Coming soon | Premium Editorial | Brands, interviews, thought leadership | `$create-social-thumbnails Premium editorial at 4:5 with muted neutrals, a high-quality real subject, elegant serif type, and deliberate negative space.` |
| `S09` | Coming soon | Playful Sticker | Lifestyle, education, creator tips | `$create-social-thumbnails Playful sticker at 3:4 with a real person or product, original doodles and tape, and two or three accent colors.` |
| `S10` | Coming soon | Product Hero | Launches, reviews, e-commerce | `$create-social-thumbnails Product hero at 1:1. Make the real product the hero, lead with the core benefit, and use a clean brand field with natural light.` |

The existing Figma-template cover is classified as **`S01 Warm Handwritten Collage` as the primary style, with `S02 Face-led High CTR` as a secondary trait**. It uses `S01` as its main ID because the defining system is ivory paper, marker typography, coral/blue strokes, a real interface collage, and a title gradient; the person strengthens the click driver without defining the base layout. See the [full demo notes](demos/S01-warm-handwritten-collage-6x7/README.md).

To use one, say something like “warm handwritten collage + 6:7” or “face-led high CTR + 16:9,” then replace the title and attach the real assets. Catalog IDs are optional.

## Recommended ratios for popular platforms

| Platform | Recommended canvas | Ratio | Best for |
|---|---:|---:|---|
| Xiaohongshu | 1080 × 1440 | 3:4 | Image notes, explainers, product discovery |
| WeChat Channels | 1080 × 1260 | 6:7 | WeChat Channels feed covers |
| YouTube | 3840 × 2160 | 16:9 | Standard landscape video thumbnails |
| YouTube Shorts | 2160 × 3840 | 9:16 | Vertical Shorts thumbnails |
| Douyin | 1080 × 1920 | 9:16 | Full-height vertical short-video covers |

Platform interfaces change. The Xiaohongshu, WeChat Channels, and Douyin dimensions are practical project presets, so check the current in-app crop preview before publishing. The YouTube values follow [YouTube Help](https://support.google.com/youtube/answer/72431?hl=en).

## Installation

The skill requires a Codex version with Agent Skills support. The three helper scripts require Python 3.10 or newer and have no third-party Python dependencies.

### Option 1: Ask Codex to install it (recommended)

Enter this in Codex:

```text
$skill-installer install the create-social-thumbnails skill from https://github.com/anxiong2025/thumbnail-skill/tree/main/create-social-thumbnails
```

Codex normally detects a newly installed skill automatically. Restart Codex if it does not appear.

### Option 2: User-level installation

```bash
git clone https://github.com/anxiong2025/thumbnail-skill.git
mkdir -p ~/.agents/skills
cp -R thumbnail-skill/create-social-thumbnails ~/.agents/skills/
```

A user-level skill is available across local projects for that user.

### Option 3: Repository-level installation

Run this from the target repository root:

```bash
mkdir -p .agents/skills
cp -R /path/to/thumbnail-skill/create-social-thumbnails .agents/skills/
```

Commit `.agents/skills/create-social-thumbnails` when the whole team should use it in that repository. These locations follow the [official OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills).

## Usage

Invoke the skill explicitly in Codex:

```text
$create-social-thumbnails
Create a 6:7 WeChat Channels cover from my real portrait and product screenshots.
Title: 400+ Figma Design Templates
Supporting label: Commercial-use assets
Style: warm ivory and hand-drawn; place a white-to-transparent gradient between the title and the real collage.
Do not generate or redraw the product screenshots, and do not change the person's identity.
```

You can also describe the task normally. Codex may select the skill automatically when the request matches its description.

For a quick starting point, copy a prompt directly from the “Thumbnail examples” table, then add the title and attach the assets.

### Recommended inputs

- target platform and content type;
- main title and optional supporting text;
- real photos, screenshots, products, or logos that must remain authentic;
- style-only references;
- brand colors, tone, and desired output format;
- whether the assets are cleared for public or commercial use.

### More examples

```text
$create-social-thumbnails Use this real portrait and these three real UI screenshots to create two 3:4 Xiaohongshu variants: one text-led and one face-led.
```

```text
$create-social-thumbnails Adapt this WeChat Channels cover to 16:9 YouTube. Preserve the real person and screenshots, rebuild the hierarchy, and do not stretch the original.
```

```text
$create-social-thumbnails Review this Douyin cover for feed-size readability, safe margins, cutout fidelity, real-asset integrity, and commercial-rights wording. Give recommendations only.
```

## Helper scripts

Inspect presets:

```bash
python3 create-social-thumbnails/scripts/platform_presets.py --list
python3 create-social-thumbnails/scripts/platform_presets.py --platform wechat --json
```

Build an editable prompt:

```bash
python3 create-social-thumbnails/scripts/prompt_builder.py --list-styles --language en
python3 create-social-thumbnails/scripts/prompt_builder.py --style S01 --ratio 16:9 --title "400+ Figma Design Templates" --platform YouTube --language en
```

Verify a PNG or JPEG export:

```bash
python3 create-social-thumbnails/scripts/verify_thumbnail.py cover.png --platform wechat-channels
python3 create-social-thumbnails/scripts/verify_thumbnail.py cover.jpg --platform youtube --aspect-only
```

The scripts verify technical properties only. They do not replace visual, factual, or rights review.

## Repository structure

```text
thumbnail-skill/
├── README.md
├── README_EN.md
├── LICENSE
├── demos/
│   └── README.md
└── create-social-thumbnails/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── assets/README.md
    ├── references/
    │   ├── asset-integrity.md
    │   ├── composition-patterns.md
    │   ├── platform-specs.md
    │   ├── qa-checklist.md
    │   └── style-catalog.md
    └── scripts/
        ├── platform_presets.py
        ├── prompt_builder.py
        └── verify_thumbnail.py
```

## Demo policy

Future examples belong in [`demos/`](demos/). Each demo must include its platform, dimensions, inputs, output, reproduction steps, and `LICENSE-ASSETS.md`. Public demos should prefer owned or licensed assets. If the repository owner explicitly includes a rights-unverified style example, it must be labeled separately, excluded from the MIT License, and never presented as commercially cleared.

## License and commercial-use notice

The repository's code and written workflow are released under the [MIT License](LICENSE). The MIT License does **not** automatically cover demo images, user-uploaded photos, likeness rights, brand logos, software screenshots, fonts, third-party templates, or assets produced by external services.

Only call a finished thumbnail “commercially cleared” when the rights for every included asset are documented. This repository provides a production SOP and validation mechanism, not legal advice.

## Contributing

Issues and pull requests are welcome. For a new platform preset, include its source and verification date. For a new demo, document the asset rights first and remove personal information.
