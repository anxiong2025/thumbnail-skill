---
name: create-social-thumbnails
description: Create, adapt, or review high-clarity social-media thumbnails and covers for Xiaohongshu, WeChat Channels, YouTube, YouTube Shorts, and Douyin. Use when the user supplies real photos, screenshots, products, or style references and needs platform-ready raster artwork; preserve real assets exactly and do not replace them with AI-generated lookalikes.
---

# Create Social Thumbnails

Produce a platform-ready thumbnail that remains legible at feed size, uses the user's real assets faithfully, and has a clear click-driving visual hierarchy.

## Route the request

1. Identify the target platform and content type.
2. Read [references/platform-specs.md](references/platform-specs.md) for the matching canvas and export preset.
3. Read [references/composition-patterns.md](references/composition-patterns.md) when choosing a layout, creating variants, or reproducing the title-to-image gradient treatment.
4. Read [references/asset-integrity.md](references/asset-integrity.md) whenever the request includes user photos, product screenshots, brands, public figures, or a commercial-use claim.
5. Before delivery, follow [references/qa-checklist.md](references/qa-checklist.md).

## Intake

Collect or infer these inputs:

- target platform and content type;
- primary title and optional supporting text;
- exact-use assets such as the user's portrait, real screenshots, products, or logos;
- style-only references;
- desired tone, brand colors, and output format;
- whether the user is requesting commercial-use clearance.

Do not block on non-critical omissions. Choose a sensible default and state it. Ask only when a missing title, required real asset, or rights-sensitive choice would materially change the result.

## Protect source fidelity

Classify every input before editing:

- **Exact-use asset:** preserve its actual content. Crop, mask, scale, color-correct, and composite it deterministically.
- **Style reference:** borrow only general layout, rhythm, contrast, or color direction. Do not copy protected artwork or treat the reference as a source asset.
- **Generatable support:** backgrounds, abstract textures, generic shapes, arrows, highlights, and non-branded decoration may be generated when useful.

Never redraw a real interface screenshot, product, document, data visualization, logo, or person when the user expects the original. Never create an AI lookalike as a substitute for the supplied portrait. If a cutout tool may alter the subject, compare the result with the source at face, hands, clothing, logos, and edges before using it.

## Build the composition

1. Create the exact target canvas before laying out content.
2. Establish one dominant promise, one dominant subject, and one supporting proof area.
3. Keep the main title short enough to understand in roughly one second. Prefer two hierarchy levels over many equal-sized labels.
4. Reserve UI-safe margins and avoid placing essential text or faces near edges.
5. For a collage beneath the title, place the real collage unchanged, then add a separate background-colored-to-transparent overlay above it. Do not bake fake screenshots into the gradient.
6. For a portrait-led cover, cut out the supplied person, keep recognizable features unchanged, and use outline or shadow only to separate the subject from the collage.
7. When exploration is requested, create up to three meaningfully different variants: text-led, face-led, and proof-led. Do not create superficial color-only variants.

## Generate and edit

Use deterministic compositing for exact-use assets. Use image generation or image editing only for eligible supporting elements and only when it does not compromise real-asset fidelity. If the environment cannot create a native Figma file, deliver the final raster plus a concise layout specification instead of claiming that a Figma source exists.

Keep source files separate where possible:

- background and texture;
- title and annotations;
- real collage or product screenshots;
- subject cutout;
- gradient, outline, and shadow effects.

## Verify

Run the bundled helpers when Python is available:

```bash
python3 scripts/platform_presets.py --list
python3 scripts/verify_thumbnail.py output.png --platform wechat-channels
```

Use `--aspect-only` only when the user intentionally requests a non-canonical resolution. The verifier checks technical conformance; still perform visual QA at full size and at a small feed preview.

## Deliver

Report:

- the final file path and pixel dimensions;
- the platform preset used;
- which supplied real assets were preserved;
- any assumptions or unsupported native-file claims;
- a rights caveat when commercial use is requested but third-party rights are not documented.

Do not label an output “commercially cleared” merely because this skill's code is open source. Commercial clearance depends on every included photo, person, brand, font, screenshot, template, and generated asset.
