# ConvoySupply — Experiment Log

Every test, with its hypothesis written **before** the result. A hypothesis recorded after the fact is not a hypothesis — it is a story, and it will make a lucky result look like a skilled one.

**Format**

```
## EXP-XXX — Title
Status: PLANNED | RUNNING | COMPLETE | ABANDONED
Hypothesis:    what we predict, and why
Method:        what we change, what we hold constant
Success:       the number that means it worked, decided in advance
Result:        (blank until it runs)
Learning:      (blank until it runs)
Action:        (blank until it runs)
```

**Rule: `Hypothesis` and `Success` are filled in before the test starts and are never edited afterward.**

---

## EXP-001 — Broad vs. interest targeting
**PLANNED · Days 25–38 · Channel: Meta**

**Hypothesis:** Broad targeting will beat an interest stack on CPA, because our creative is unusually self-selecting — a photograph of a sleeper cab interior is invisible to anyone who is not a driver — and Meta's occupational interest taxonomy is unreliable.

**Method:** Three cold ad sets — Broad, Interest stack, Advantage+ — under one CBO campaign with **identical creative**. Creative held constant; audience is the only variable.

**Success:** One approach delivers a CPA at least 25% better than the others over 14 days, with 5+ purchases total.

**Known limitation:** CBO concentrates spend unevenly, so this is directional, not clean. See DEC-007.

**Result / Learning / Action:** *pending*

---

## EXP-002 — Which marketing angle moves money
**PLANNED · Days 25–38 · Channel: Meta**

**Hypothesis:** Problem/solution and before/after will beat lifestyle and curiosity on CPA, because this is a *latent* problem — it causes no pain on any given day — and latent problems need to be made visible before they can be sold against.

**Method:** Five Wave 1 creatives across five distinct angles, identical placement, same ad sets. Two Wave 2 concepts introduced on Day 7.

**Success:** A clear CPA ranking with the top creative at least 30% better than the median, over 1,000+ impressions each.

**Watch for:** AD-10 (objection-first, "we're not cheaper than Amazon") is the highest-variance concept. **Prediction on record: lowest CTR, highest conversion rate on the clicks it gets.** If that holds it is the most valuable thing learned all month, because it says the audience responds to honesty over persuasion.

**Result / Learning / Action:** *pending*

---

## EXP-003 — Does the bundle carry the economics?
**PLANNED · Days 25–38 · Channel: Meta + site**

**Hypothesis:** Bundle-led traffic will show a **worse CPA and better contribution profit per order** than single-item traffic, because the Cab Reset Kit's break-even CPA is $42.52 against CS-01's $32.59 — nearly $10 more room per order.

**Method:** AD-09 (bundle) runs against AD-01 (hero single). Compare on contribution profit per purchase, not CPA.

**Success:** Bundle traffic delivers higher contribution profit per order even at a worse CPA.

**Why this matters:** if true, **CPA is the wrong primary metric for judging creative** and the whole account should optimize toward AOV. That would be the single most consequential finding of the test.

**Result / Learning / Action:** *pending*

---

## EXP-004 — Is Facebook Marketplace real for these goods?
**PLANNED · Days 19–40 · Channel: Marketplace**

**Hypothesis:** Marketplace will produce sales at a meaningfully lower effective acquisition cost than Meta ads, because there is no ad spend attached — but volume will be low because our audience is mobile and Marketplace skews local.

**Method:** Five listings, renewed weekly, sub-1-hour response time, scripts from `marketing/marketplace-strategy.md`. Log views, inquiries, and sales.

**Success:** 5+ sales in 21 days, or an inquiry→sale rate above 15%.
**Kill:** 30+ listing-weeks across 21 days with zero sales.

**If it succeeds:** a CPA-free channel that converts changes the entire economics and the paid budget gets reconsidered.

**Result / Learning / Action:** *pending*

---

## EXP-005 — Does the $29.99 entry SKU outperform the $54.99 hero?
**PLANNED · Days 32–38 · Channel: Meta**

**Hypothesis:** AD-07 (CS-02 Bunk Shelf Net, $29.99) will show a better CPA than the hero ads, because price sensitivity is a real constraint and $29.99 is a low-risk first purchase from an unknown brand.

**Method:** AD-07 introduced in Wave 2 alongside the hero creatives.

**Success:** CS-02 CPA at least 25% below the hero CPA with 3+ purchases.

**The uncomfortable implication:** if CS-02 wins, AOV falls to the pessimistic-mix scenario, blended break-even CPA drops from $39.16 to **$31.30**, and the business gets *harder*, not easier. A "winning" ad can make the model worse. See `finance/unit-economics.md`.

**Result / Learning / Action:** *pending*

---

## EXP-006 — Do educational posts out-save product posts?
**PLANNED · Days 21–50 · Channel: Organic**

**Hypothesis:** Educational posts (E-01 to E-05) will generate more saves and shares than product posts, because saves signal "I'll need this," which is the strongest organic purchase intent signal available.

**Method:** 5 educational vs. 4 benefit posts over four weeks. Compare saves, shares, and comments — not likes.

**Success:** Educational posts average 2× the saves of product posts.
**Action if true:** shift the organic mix toward education and promote the best educational post to a paid creative.

**Result / Learning / Action:** *pending*

---

## EXP-007 — Landing page vs. PDP for paid traffic
**PLANNED · Days 39+ (after the Phase 1 decision) · Channel: Meta + site**

**Hypothesis:** The funnel landing page will beat the PDP on conversion rate for cold paid traffic, because a stranger needs the problem framed before the product is introduced, and the PDP assumes context the visitor does not have.

**Method:** Split the winning creative's traffic between `/pages/cs-01` and `/products/cs-01-cab-command-organizer`. Same creative, same audience, same budget.

**Success:** One destination shows a conversion rate at least 25% better over 500+ sessions each.

**Deliberately scheduled after Phase 1** — running it during the cold test would add a variable and muddy EXP-001 and EXP-002.

**Result / Learning / Action:** *pending*

---

## EXP-008 — Does the fit guide convert better than the product page?
**PLANNED · Days 25–38 · Channel: Meta**

**Hypothesis:** AD-04 (educational, sending to `/pages/what-fits-my-truck`) will show a lower CTR but a higher eventual conversion rate than product-page ads, because it removes the strongest objection — fit — before asking for a sale.

**Method:** AD-04 is the only Wave 1 creative pointing at the fit guide. Compare the full funnel, not just the click.

**Success:** Fit-guide traffic converts to purchase at a rate at least equal to product-page traffic, despite the extra step.

**If true:** the whole funnel should lead with the fit guide, which would be a significant restructure — and a cheap one.

**Result / Learning / Action:** *pending*

---

## EXP-009 — Competitive monitoring
**PLANNED · Ongoing, weekly**

**Hypothesis:** The DTC whitespace claim in `research/competitor-analysis.md` is based on desk research and may be wrong. A Meta Ad Library search may reveal an active, funded DTC competitor that search results did not surface.

**Method:** Weekly Ad Library search on competitor pages and relevant keywords. Monthly Amazon top-20 price and review-velocity check. Weekly scan of Group mentions.

**Success:** Not a pass/fail — this is a standing check on an assumption the whole strategy rests on.

**Action if a funded DTC competitor is found:** the whitespace argument weakens materially and `research/selected-niche.md` needs revisiting. **Do this on Day 1, not Day 20.**

**Result / Learning / Action:** *pending*

---

## Discipline

1. **One variable at a time.** Two changes produce a result that explains nothing.
2. **Write the hypothesis and the success criterion before starting.** Never edit them after.
3. **Decide the sample size in advance.** Stopping when you like the number is how you fool yourself.
4. **Log the negative results.** They are the majority and they are worth more than the wins.
5. **A test that "almost worked" did not work.** Extending once is discipline. Extending twice is hope.
6. **Record what you expected to happen**, so you can tell skill from luck afterward.
