# ConvoySupply — Daily Log

One entry per day. Append only. Five minutes at the end of each day.

**Why this is not optional:** by Day 38 nobody remembers why a creative was killed on Day 7 or why the price changed on Day 11. Thirty days of unrecorded decisions is thirty days of learning thrown away, and the whole point of this test is the learning.

**Format**

```
## Day N — YYYY-MM-DD
Done:      what actually got finished
Learned:   what changed your mind, however small
Decided:   any decision (cross-reference DEC-XXX)
Blocked:   what's stopping progress, and who or what unblocks it
Numbers:   the day's key figures, if any
Tomorrow:  the one thing that matters most
```

**Rules**

1. Write it the same day. A log written three days later is fiction.
2. Record what went wrong. The failures are where the learning is.
3. If nothing was learned, write "nothing." That is a real and useful signal.
4. Cross-reference DEC and EXP numbers so decisions are traceable.

---

## Day 0 — 2026-09-20 — Planning

**Done:**
- Full strategy repository built: niche research across six candidates, selected niche, product catalog, customer avatar, competitor analysis
- Brand strategy and copy library
- Shopify architecture, homepage copy, PDP spec, CS-01 funnel landing page
- Nine custom Dawn sections, two templates, and a static HTML prototype of the landing page
- 30 static post concepts, 30-day organic calendar, Marketplace strategy with five listings and response scripts, Meta ads strategy with ten creative concepts
- Unit economics as a runnable script plus a gated testing budget
- 30-day plan, 12 decisions, 9 experiments, metrics templates

**Learned:**
- **Convoy Supply Ltd. is a real building-materials distributor founded in 1972** **[V2]**. This disqualified what would otherwise have been the second-strongest niche (trades/jobsite) and made trademark clearance a Day 1 gate rather than an afterthought. Found in the first ten minutes of research — an hour later and it would have shaped a week of work first.
- **Marketplace shipped items move fastest at $10–$50** **[V1]**, which ruled out overlanding on price-point grounds despite it being a more attractive market, and directly set CS-02 and CS-03 pricing.
- **Automotive has the lowest tracked Meta CPM at ~$10.01** **[V8]** — a genuine tailwind, and it means any failure here will be a conversion failure rather than a reach failure. Worth knowing before reading any data.
- **The bundle has a worse margin percentage and a better CPA ceiling** ($42.52 vs $32.59). Margin percentage is a vanity metric when the constraint is acquisition cost. This reshaped the entire offer structure.
- **A winning CS-02 ad would make the business harder**, not easier — it drops blended break-even CPA from $39.16 to $31.30. Counterintuitive enough that judging the ad test on CPA alone would pick the wrong winner.
- **Four of five launch ad creatives are blocked on physical samples.** That single dependency drives the whole schedule and is why samples are ordered on Day 1 rather than Day 5.

**Decided:** DEC-001 through DEC-012. Most consequential: DEC-001 (trademark gate), DEC-004 (CS-05 gated out), DEC-005 (retargeting gated), DEC-003 (no dark patterns, enforced in the theme code).

**Blocked:**
- Trademark clearance — not yet run. **Blocks all brand spend.**
- Supplier quotes — every cost figure is **[A]**. Blocks the margin go/no-go.
- Product samples — blocks all photography, which blocks most creative.
- Cab access — blocks the shoot.

**Numbers:** none yet. Everything in `finance/` is an estimate.

**Tomorrow (Day 1):** the three gates, in this order — USPTO TESS search · Meta Ad Library competitor check · supplier outreach and sample orders. Then start asking about cab access.

---

## Day 1 — `[DATE]`

**Done:**
**Learned:**
**Decided:**
**Blocked:**
**Numbers:**
**Tomorrow:**

---

## Day 2 — `[DATE]`

**Done:**
**Learned:**
**Decided:**
**Blocked:**
**Numbers:**
**Tomorrow:**

---

*Copy the block above for each subsequent day.*

---

## Weekly retro template

Run every Friday. Twenty minutes.

```
## Week N retro — [dates]

What worked:
What didn't:
What surprised me:
What I'd do differently:
Hypotheses confirmed:      (update research/ docs — promote [H] to [V])
Hypotheses falsified:      (update research/ docs — delete them, don't soften them)
Decisions made:            (DEC-XXX)
Experiments advanced:      (EXP-XXX)
Numbers:                   (see execution/metrics.md)
Next week's single priority:
```

**"Hypotheses falsified" is the most valuable line.** A repository full of confirmed guesses means the guesses were too safe to be worth testing. **When a hypothesis is falsified, delete it from the research docs rather than softening the wording** — a hedged wrong belief is worse than a deleted one, because it still shapes decisions while looking harmless.
