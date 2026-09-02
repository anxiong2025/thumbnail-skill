# Thumbnail Prompt Library

English | [简体中文](PROMPTS.md)

Choose an ID from the [style catalog](create-social-thumbnails/references/style-catalog.md), copy the matching prompt, replace the `{braced fields}`, and attach the real assets.

Supported general ratios: `1:1`, `4:3`, `3:4`, `4:5`, `6:7`, `16:9`, and `9:16`. A ratio can be specified independently of a platform.

## Master template

```text
$create-social-thumbnails
Create a social-media thumbnail.
Style ID: {S01–S10}
Platform: {Xiaohongshu/WeChat Channels/YouTube/YouTube Shorts/Douyin/unspecified}
Ratio: {1:1/4:3/3:4/4:5/6:7/16:9/9:16}
Main title: {title}
Supporting title: {optional}
Real assets: {describe attached people, products, screenshots, or logos}
Brand colors: {optional}
Output: PNG at the recommended pixel dimensions for the selected ratio.

Use my uploaded real assets. Do not generate, redraw, or replace people, products, logos, data, or interface screenshots. Treat reference images as direction for composition, type hierarchy, and color only. Keep the headline readable at mobile feed size and essential content inside safe margins. On delivery, report dimensions, preserved assets, and unresolved rights risks.
```

## S01 Warm Handwritten Collage

```text
$create-social-thumbnails Use style S01 Warm Handwritten Collage for a {ratio} cover. Main title: “{title}”; emphasize “{number or keyword}.” Use warm ivory paper, dark navy marker lettering, and restrained coral and bright-blue brush accents. The lower half must use my real screenshot collage. Add a separate warm-ivory-to-transparent gradient below the title. Place my real portrait cutout at lower-right, preserve identity and clothing, and use one clean outline. Do not generate fake interfaces.
```

## S02 Face-led High CTR

```text
$create-social-thumbnails Use style S02 Face-led High CTR for a {ratio} cover. Use my real portrait as the main subject at about 40% of the canvas; preserve identity and expression. Main title: “{title},” with “{keyword}” emphasized and no more than two hierarchy levels. Keep the background simple and use one real result screenshot as proof. Use one outline or shadow only. Do not create a substitute face.
```

## S03 Clean UI Showcase

```text
$create-social-thumbnails Use style S03 Clean UI Showcase for a {ratio} cover. Main title: “{title}.” Use a white or light-gray background, modern sans serif type, and generous spacing. Make my real product interface dominant, with at most two supporting cards. Subtle radius, shadow, and a brand gradient are allowed, but interface text, data, logos, and features must remain accurate.
```

## S04 Dark Tech Neon

```text
$create-social-thumbnails Use style S04 Dark Tech Neon for a {ratio} cover. Main title: “{title},” emphasizing “{keyword}.” Use a near-black background and one primary neon color: {blue/cyan/violet/green}. Feature my real dashboard, code, chart, or device screen with restrained edge lighting and depth. Do not invent data, and keep text contrast strong.
```

## S05 Bold Number List

```text
$create-social-thumbnails Use style S05 Bold Number List for a {ratio} cover. Make “{number}” the largest element and “{category or benefit}” the second level. Group {3–6} real uploaded examples below it. Use one underline, circle, or burst behind the number. Avoid competing numbers and explanatory paragraphs.
```

## S06 Before–After Split

```text
$create-social-thumbnails Use style S06 Before–After Split for a {ratio} cover. Main title: “{transformation}.” Use my real BEFORE and AFTER images with matching scale, angle, and comparable crops in a vertical, horizontal, or diagonal split. Label both sides clearly and add at most one directional arrow. Do not exaggerate or fabricate the result.
```

## S07 News Commentary

```text
$create-social-thumbnails Use style S07 News Commentary for a {ratio} cover about “{event or topic}.” Main title: “{factual angle, question, or consequence}.” Use my supplied or rights-cleared real topic image and one simple color block or segment label. Keep it credible: do not fabricate quotes, alter expressions, or add unsupported conclusions.
```

## S08 Premium Editorial

```text
$create-social-thumbnails Use style S08 Premium Editorial for a {ratio} cover. Main title: “{title}.” Use a neutral or muted brand background, elegant serif paired with clean sans serif, and deliberate negative space. Feature my high-quality portrait or product image with fine rules, a small issue label, and subtle grain. Do not imitate a real magazine logo or use cheap glow effects.
```

## S09 Playful Sticker

```text
$create-social-thumbnails Use style S09 Playful Sticker for a {ratio} cover. Main title: “{title},” with an approachable, energetic tone. Use bright color blocks or warm paper and my real portrait or product. Add original doodle arrows, tape, and sticker effects in two or three accent colors. Decoration must not cover faces, product details, or proof.
```

## S10 Product Hero

```text
$create-social-thumbnails Use style S10 Product Hero for a {ratio} cover. Lead with the benefit “{core benefit}” and use “{product name}” as the second level. Make my real product the single large hero on a clean gradient, tabletop scene, or brand-color field, with natural light and one truthful feature or result. Do not alter packaging, logos, ports, materials, or proportions.
```

## Revision template

```text
Keep style {Sxx} and all real assets from the previous version. Change only:
1. Recompose for {new ratio}; do not stretch the design.
2. Replace the headline with “{new title}.”
3. Move {portrait/product/screenshot} to {position}.
4. Keep everything else consistent.
Recheck safe margins, feed-size headline readability, and real-asset fidelity.
```
