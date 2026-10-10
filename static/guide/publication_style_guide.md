# Publication Image Style Guide

## Purpose

Use this guide whenever creating a publication image for the HSMI website. Create one image that communicates the paper's central idea and follows the visual language of the existing SVG illustrations in `layouts/partials/hcmi/pub_art.html`.

## Reference artwork

Read `layouts/partials/hcmi/pub_art.html` before creating an image. It contains five recurring visual motifs:

1. **Overlapping circles:** two intersecting concepts, sets, or entities.
2. **Flow with labeled nodes:** inputs, processing, explanation, or transformation.
3. **Axes with curves:** evaluation, comparison, trends, or changing results.
4. **A field of dots:** datasets, samples, distributions, or observations.
5. **A connected graph:** networks, collaboration, relationships, or graph structures.

Use these motifs as visual guidance, not as artwork to copy unchanged. Select a motif that fits the paper, then adapt it to the paper's actual subject.

## Visual requirements

- **Style:** minimal, precise, calm, academic, and suitable for a research laboratory website.
- **Canvas:** horizontal, approximately 2:1. The reference SVG uses `viewBox="0 0 220 110"`.
- **Composition:** center the main diagram and leave generous empty space around it.
- **Palette:** use muted, light blues sampled from the reference:
  - Primary blue: `#7eafd2`
  - Mid blues: `#6ea0c6`, `#4d86b3`
  - Light blues: `#8bb6d4`, `#b7d3e6`
  - Pale node fills: `#eef6fb`, `#e7f2f9`
  - Faint lines: `#d5e4ef`
- **Lines:** use thin, consistent strokes, generally 1 to 1.6 units at the reference viewBox scale.
- **Shapes:** prefer circles, dots, straight connectors, and smooth curves. Keep geometry clean and purposeful.
- **Text:** avoid text inside the image. If a label is essential, use only a few short, readable labels in a sans-serif font and a muted blue.
- **Avoid:** long text, decorative lettering, logos, unrelated icons, photographic decoration, heavy borders, strong shadows, and high-contrast gradients.
- **Clarity:** make the concept recognizable when the image is displayed at small publication-card size. Do not rely on color alone to communicate meaning.
- **Accuracy:** do not invent data, quantitative results, or conclusions that are not stated in the paper.

## Workflow for a new publication

1. Locate or create the publication directory: `content/publication/<slug>/`. The content file is usually `index.md`.
2. Read the paper's title, abstract, and tags. Identify exactly one central concept or relationship to visualize.
3. Choose the most suitable reference motif. Examples: compare two methods, show an input-to-output flow, represent a collaboration network, illustrate an evaluation trend, or depict a dataset.
4. Sketch a sparse diagram that expresses the selected concept accurately. Do not turn the image into a generic decoration.
5. Create the image with the required palette, proportions, line weight, and negative space.
6. Save the final image in the same directory as the publication's `index.md`:

   - Raster: `content/publication/<slug>/featured.png`
   - Vector: `content/publication/<slug>/featured.svg`

   Prefer a clean, self-contained SVG when the image-generation workflow supports it. Otherwise use PNG. For SVG, include a clear `viewBox` and ensure any text remains readable at display size.

7. Update the publication's existing `image` front matter to reference the local file. Example:

   ```yaml
   image:
     filename: featured.png
     caption: 'Conceptual illustration of [paper topic].'
     focal_point: Center
     preview_only: false
   ```

   Use `featured.svg` when the output is SVG. If an `image` block already exists, edit it instead of adding a duplicate block. Preserve its existing values unless they need to change.

8. Confirm that the file exists in the publication directory and that `image.filename` matches its exact name and extension. Inspect the image at small card size. Simplify it or improve contrast if the central concept is not immediately clear.

## File placement and naming

- Use the fixed filename `featured.png` or `featured.svg`.
- Store the image beside the publication's `index.md`, inside `content/publication/<slug>/`.
- Create a distinct image for each paper. Reuse an image only when it accurately represents both papers.
- Keep only the final image in the publication directory. Do not add intermediate generations or prompt files to the website content.

## Reusable image-generation prompt

Replace the bracketed fields with information from the paper before using this prompt:

```text
Read the publication at content/publication/[slug]/index.md and inspect layouts/partials/hcmi/pub_art.html before creating the image.

Create a minimal conceptual illustration for the paper titled "[paper title]". Communicate this single central concept: [one-sentence concept]. Choose and adapt the most suitable motif from the SVG reference: overlapping circles, flow with nodes, curves on axes, a field of dots, or a connected graph.

Style: precise, calm, academic, minimal. Use a horizontal 2:1 composition with generous whitespace, thin consistent lines, and clean circles, dots, connectors, or smooth curves. Match the reference palette: #7eafd2, #6ea0c6, #4d86b3, #8bb6d4, #b7d3e6, #eef6fb, #e7f2f9, and #d5e4ef. Ensure that the concept remains clear at small publication-card size.

Do not add decorative text, long labels, logos, unrelated icons, heavy borders, strong shadows, high-contrast gradients, invented data, or unsupported conclusions. Avoid text unless a very short label is essential.

Save the final image as content/publication/[slug]/featured.png (or featured.svg for a clean vector output). Update the existing image block in content/publication/[slug]/index.md so image.filename references the exact file. Do not create a duplicate image block. Verify the filename and relative placement.
```

## Completion checklist

- [ ] The image communicates one central idea from the paper.
- [ ] The chosen motif fits the paper and is adapted from the SVG reference style.
- [ ] The image uses a horizontal 2:1 composition, muted blues, thin lines, and generous whitespace.
- [ ] The concept is clear at small card size.
- [ ] No unsupported data or conclusions are shown.
- [ ] The final image is inside the publication's directory and uses the standard filename.
- [ ] `image.filename` matches the actual file name and extension.
