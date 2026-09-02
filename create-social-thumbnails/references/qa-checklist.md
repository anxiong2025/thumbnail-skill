# Thumbnail QA checklist

## Content

- [ ] Platform and content type are identified.
- [ ] Headline matches the user's topic and contains no invented claim.
- [ ] Spelling, numbers, brand names, and punctuation are correct.
- [ ] Reference-image text was not mistaken for a user instruction.

## Real-asset fidelity

- [ ] Every exact-use screenshot, product, logo, chart, and portrait comes from the supplied source.
- [ ] No fake UI or AI lookalike replaced a real asset.
- [ ] Portrait identity, face, hands, clothing, logos, and edges survive cutout/editing.
- [ ] Collages remain readable enough to function as proof.

## Visual hierarchy

- [ ] One promise, one dominant subject, and one supporting proof area are obvious.
- [ ] Main title is readable at a small feed preview.
- [ ] Contrast is sufficient without excessive outlines or glow.
- [ ] Gradient improves the title-to-image transition without hiding key proof.
- [ ] Essential content stays inside the recommended safe area.

## Technical export

- [ ] Pixel dimensions and aspect ratio match the selected preset.
- [ ] Output is PNG or JPG in sRGB.
- [ ] No accidental alpha fringe, crop, stretching, or compression artifact is visible.
- [ ] File opens successfully at full resolution.
- [ ] `verify_thumbnail.py` passes, or a deliberate exception is documented.

## Rights and delivery

- [ ] Commercial-use wording matches the documented asset rights.
- [ ] Third-party or public-figure demo limitations are disclosed.
- [ ] Delivery lists the file path, dimensions, preset, preserved assets, and assumptions.
