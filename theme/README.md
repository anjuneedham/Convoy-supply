# ConvoySupply — Shopify Theme Code

Custom sections and templates layered on top of **Dawn**. These are the parts Dawn does not provide; everything else uses Dawn natively.

```
theme/
  snippets/cs-tokens.liquid      Design tokens + base CSS. Render once in <head>.
  sections/
    cs-hero.liquid               Problem-first hero with image and two CTAs
    cs-cards.liquid              Generic card grid — problem, benefits, how-it-works
    cs-compare.liquid            Honest 4-column comparison table
    cs-proof.liquid              Social proof; renders the honest "no reviews yet" message when empty
    cs-faq.liquid                Accordion FAQ + FAQPage structured data
    cs-specs.liquid              Spec table + fit note + diagram
    cs-offer.liquid              Two-option offer block with direct add-to-cart (landing page)
    cs-cta.liquid                Closing CTA band
    cs-sticky-cta.liquid         Mobile sticky add-to-cart (landing page)
  templates/
    index.json                   Homepage
    page.landing-cs01.json       CS-01 funnel landing page
```

## Install

1. **Add Dawn** — Online Store → Themes → Add theme → Dawn. Duplicate it and work on the copy.
2. **Upload the sections.** Either:
   - Shopify CLI (recommended): `shopify theme dev` from a local pull, copy these files in, then `shopify theme push`
   - Or Edit code → Sections → Add a new section, one file at a time
3. **Upload `snippets/cs-tokens.liquid`** and render it in `layout/theme.liquid`, inside `<head>`, after Dawn's own CSS:
   ```liquid
   {% render 'cs-tokens' %}
   ```
4. **Add the fonts** to `<head>`:
   ```html
   <link rel="preconnect" href="https://fonts.googleapis.com">
   <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
   <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Inter:wght@400;500;600&family=Roboto+Mono:wght@400&display=swap">
   ```
5. **Upload the templates** to `templates/`. `index.json` replaces Dawn's homepage. `page.landing-cs01.json` becomes selectable as a page template.
6. **Create the page** at `/pages/cs-01` and assign it the `landing-cs01` template.
7. **Point the product-backed sections** (`featured-product`, `cs-offer`, `cs-sticky-cta`) at real products in the theme editor. Until then they render a placeholder note.
8. **Suppress nav on the landing template.** In `layout/theme.liquid`, wrap the header nav and footer link lists:
   ```liquid
   {%- unless template.suffix == 'landing-cs01' -%}
     {% sections 'header-group' %}
   {%- endunless -%}
   ```
   Adjust to match your Dawn version's group names.

## Conventions these files enforce

These are not stylistic preferences — they implement rules from `brand/brand-copy.md` and are deliberately baked into the code so they are hard to violate by accident:

- **`cs-proof` has no way to display a review that is not entered as a block**, and the block schema carries a warning that blocks are for genuine customer reviews only. There is no star-rating aggregate, no import, and no placeholder review shipped in any template.
- **`cs-offer` derives the saving from `compare_at_price - price`**, so the displayed saving is always whatever Shopify actually holds. It cannot show a discount that isn't configured.
- **No countdown, stock-counter, "X viewing", or exit-intent component exists in this theme.** Adding one means writing it, which is the point.
- **`cs-sticky-cta` shows the price and the button.** No timer, no urgency copy.
- All images use `loading="lazy"` except the hero, which uses `eager` + `fetchpriority="high"`.
- Every section is mobile-first and collapses to a single column under 600px.

## `[TBC]` markers

Templates contain `[TBC]` where a real value is required — shipping times, return shipping terms, support email, founder first name, and every material spec. **Nothing ships with a bracket in it.** The pre-publish checklists in `store/homepage-copy.md`, `store/product-pages.md` and `store/landing-page.md` cover these.

## Performance

Target: homepage under 1.2 MB, LCP under 2.5s on 4G. The dominant risks are (a) unoptimized hero images and (b) installed apps. Keep hero images under 200 KB as WebP and install no apps at launch. See `store/store-architecture.md`.
