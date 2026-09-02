# Thumbnail Skill

English | [简体中文](README.md)

A Codex skill for designing, adapting, and reviewing social-media thumbnails with the user's real portraits, products, and screenshots. It includes working presets for Xiaohongshu, WeChat Channels, YouTube, YouTube Shorts, and Douyin.

> Current version: `v0.1.0`. Visual demos will be added only after their asset rights are documented. The initial release does not pad the gallery with fake interfaces or AI substitute people.

## What it does

- Supports five platform/content presets across horizontal and vertical layouts.
- Separates exact-use assets, style-only references, and generatable decoration.
- Prevents AI redraws or substitutions of real screenshots, products, logos, data, and people.
- Covers headline zones, real UI collages, portrait cutouts, and white-to-transparent title transitions.
- Includes QA guidance for fidelity, rights language, feed-size readability, dimensions, and export.
- Includes dependency-free Python helpers for presets and PNG/JPEG dimension checks.

## Platform presets

| Platform | Default canvas | Ratio | Note |
|---|---:|---:|---|
| Xiaohongshu | 1080 × 1440 | 3:4 | Common image-note working preset |
| WeChat Channels | 1080 × 1260 | 6:7 | Common feed-cover working preset |
| YouTube | 3840 × 2160 | 16:9 | Current official recommendation |
| YouTube Shorts | 2160 × 3840 | 9:16 | Current official recommendation |
| Douyin | 1080 × 1920 | 9:16 | Common vertical working preset |

Platform interfaces change. The Xiaohongshu, WeChat Channels, and Douyin dimensions are practical project presets, so check the current in-app crop preview before publishing. The YouTube values follow [YouTube Help](https://support.google.com/youtube/answer/72431?hl=en).

## Installation

The skill requires a Codex version with Agent Skills support. The two helper scripts require Python 3.10 or newer and have no third-party Python dependencies.

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
    │   └── qa-checklist.md
    └── scripts/
        ├── platform_presets.py
        └── verify_thumbnail.py
```

## Demo policy

Future examples belong in [`demos/`](demos/). Each demo must include its platform, dimensions, inputs, output, reproduction steps, and `LICENSE-ASSETS.md`. Do not publish private user photos, unlicensed celebrity images, third-party templates, or fonts.

## License and commercial-use notice

The repository's code and written workflow are released under the [MIT License](LICENSE). The MIT License does **not** automatically cover demo images, user-uploaded photos, likeness rights, brand logos, software screenshots, fonts, third-party templates, or assets produced by external services.

Only call a finished thumbnail “commercially cleared” when the rights for every included asset are documented. This repository provides a production SOP and validation mechanism, not legal advice.

## Contributing

Issues and pull requests are welcome. For a new platform preset, include its source and verification date. For a new demo, document the asset rights first and remove personal information.
