# High-CTR Creator Thumbnail Skill

English | [简体中文](README.md)

Create high-CTR thumbnails and creator covers for Xiaohongshu, WeChat Channels, Douyin, YouTube, and YouTube Shorts from real portraits, real products, and real screenshots.

> **Real assets × click-driving structures × multi-platform ratios × copy-ready prompts**

Start from a proven visual system instead of a blank canvas: choose a style from `S01–S10`, set the ratio, attach the assets, and replace the title. Codex then follows the production and QA workflow.

> Current version: `v0.3.2`. “High-CTR” describes the design objective and does not promise views, click-through rate, virality, or commercial results. The first real finished cover is included as a style demonstration. Rights for third-party people, brands, and interface imagery are not established, so the example is not presented as commercially cleared.

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

See the full [style catalog](create-social-thumbnails/references/style-catalog.md). The compact prompts show the intended formula; select “Copy full prompt” to open the complete editable version.

| ID | Preview | Style | Best for | Prompt example |
|---|---|---|---|---|
| `S01` | <a href="demos/S01-warm-handwritten-collage-6x7/preview.png"><img src="demos/S01-warm-handwritten-collage-6x7/preview.png" width="180" alt="S01 Warm Handwritten Collage thumbnail"></a> | Warm Handwritten Collage | Resource packs, templates, design collections | `S01 + 6:7 + real collage + portrait cutout`<br>[Copy full prompt](PROMPTS_EN.md#s01-warm-handwritten-collage) |
| `S02` | Coming soon | Face-led High CTR | Personal brands, tutorials, reactions | `S02 + 16:9 + real face + short contrast title`<br>[Copy full prompt](PROMPTS_EN.md#s02-face-led-high-ctr) |
| `S03` | Coming soon | Clean UI Showcase | SaaS, apps, Figma, workflows | `S03 + 4:3 + real hero UI + whitespace`<br>[Copy full prompt](PROMPTS_EN.md#s03-clean-ui-showcase) |
| `S04` | Coming soon | Dark Tech Neon | AI, coding, automation, fintech | `S04 + 16:9 + dark field + one neon accent`<br>[Copy full prompt](PROMPTS_EN.md#s04-dark-tech-neon) |
| `S05` | Coming soon | Bold Number List | Collections, rankings, comparisons | `S05 + 3:4 + large number + real examples`<br>[Copy full prompt](PROMPTS_EN.md#s05-bold-number-list) |
| `S06` | Coming soon | Before–After Split | Redesigns, transformations, tests | `S06 + 16:9 + real before/after + matched crop`<br>[Copy full prompt](PROMPTS_EN.md#s06-beforeafter-split) |
| `S07` | Coming soon | News Commentary | News, analysis, explainers | `S07 + 16:9 + real topic image + factual angle`<br>[Copy full prompt](PROMPTS_EN.md#s07-news-commentary) |
| `S08` | Coming soon | Premium Editorial | Brands, interviews, thought leadership | `S08 + 4:5 + high-quality subject + negative space`<br>[Copy full prompt](PROMPTS_EN.md#s08-premium-editorial) |
| `S09` | Coming soon | Playful Sticker | Lifestyle, education, creator tips | `S09 + 3:4 + real subject + original stickers`<br>[Copy full prompt](PROMPTS_EN.md#s09-playful-sticker) |
| `S10` | Coming soon | Product Hero | Launches, reviews, e-commerce | `S10 + 1:1 + real product + core benefit`<br>[Copy full prompt](PROMPTS_EN.md#s10-product-hero) |

The existing Figma-template cover is classified as **`S01 Warm Handwritten Collage` as the primary style, with `S02 Face-led High CTR` as a secondary trait**. It uses `S01` as its main ID because the defining system is ivory paper, marker typography, coral/blue strokes, a real interface collage, and a title gradient; the person strengthens the click driver without defining the base layout. See the [full demo notes](demos/S01-warm-handwritten-collage-6x7/README.md).

To use one, specify something like “`S01 + 6:7`” or “`S02 + 16:9`,” then replace the title and attach the real assets.

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

For a quick starting point, open [PROMPTS_EN.md](PROMPTS_EN.md), choose `S01–S10`, and replace the braced title, ratio, and asset fields.

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
├── PROMPTS.md
├── PROMPTS_EN.md
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
