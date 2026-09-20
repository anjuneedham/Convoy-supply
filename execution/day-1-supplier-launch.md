# Day 1: Supplier Contact Launch Checklist

**Objective:** Contact 5+ suppliers for CS-01 and CS-02 samples and quotes by EOD.

---

## Pre-Launch (30 min)

- [ ] Review `supplier-outreach-template.md` and customize:
  - [ ] Insert your contact info (name, email, phone)
  - [ ] Insert your shipping address
  - [ ] Set target response deadline (suggest: 7-10 days from today)
  - [ ] Set sample delivery deadline (suggest: 14-21 days from today)

- [ ] Open `supplier-evaluation-tracker.csv` in Excel/Google Sheets
  - [ ] Add 5 supplier names and contacts (see "Finding Suppliers" below)
  - [ ] Fill in "Date Contacted" column as you send emails

- [ ] Check that `supplier-scoring.py` is executable:
  ```bash
  chmod +x execution/supplier-scoring.py
  ```

---

## Finding Suppliers (1-2 hours)

**Search Sources (pick 2-3):**

1. **Alibaba.com** (fastest for China-based manufacturers)
   - Search: "soft goods organizer manufacturer" or "nylon duffel bag factory"
   - Filter: 
     - Location: China (Guangdong, Zhejiang, Fujian preferred)
     - Gold Supplier status (more reliable)
     - 5+ years in business
     - English-speaking
   - Look for: 3-4 suppliers in top results

2. **Global Sources** (www.globalsources.com)
   - Search: "nylon organizer" + "soft goods"
   - Filter by region and certifications
   - More vetted than Alibaba, slower lead times

3. **TradeKey.com**
   - Search: "fabric organizer manufacturer"
   - Look for: 2-3 suppliers with clear contact info

4. **LinkedIn Search**
   - Search: "soft goods manufacturer" + location
   - Look for sales managers, not just company pages
   - More personalized outreach = better response rate

**What to Look For in Each Supplier:**
- ✅ **Good signs:**
  - ISO 9001 or similar certification listed
  - 5+ years in business
  - Clear photos of similar products
  - Rapid response to initial inquiry (within 24 hrs)
  - Speaks fluent English in their initial response
  
- ❌ **Red flags:**
  - "Factory direct" claims with no verifiable business history
  - No email response after 3 days
  - Spelling/grammar errors in product descriptions
  - Pressure to commit to large MOQs immediately
  - No clear cost breakdown

---

## Supplier Contact (1-2 hours)

**For each of your 5 suppliers:**

1. **Copy the outreach template** from `supplier-outreach-template.md`
2. **Customize it with:**
   - Supplier's company name
   - Supplier's contact name (use Mr./Ms. if Asian supplier, first name if Western)
   - Your shipping address
   - Your deadlines
3. **Send via:**
   - Direct email (preferred if you have contact info)
   - Alibaba/platform messaging if that's your contact method
4. **Log in tracker:**
   - Column "Date Contacted" = today's date
   - Column "Contact Email" = where you sent it
   - Column "Date Response Received" = leave blank (fill in when they reply)

**Pro Tips:**
- Send all 5 emails at roughly the same time (so you get responses in a similar window)
- In subject line, include product names: "CS-01 Organizer + CS-02 Shelf Net Quote Request"
- If contacting via Alibaba, also send a follow-up email from your personal email so they have your direct contact
- For China-based suppliers, expect responses 12-24 hours later (timezone difference)

---

## Expected Response Timeline

| Timeline | What to Expect |
|----------|----------------|
| **Day 1 (Today)** | Send 5 supplier inquiries |
| **Days 2-3** | 60-70% of suppliers respond with initial feedback |
| **Days 4-5** | 80%+ have sent detailed quotes; some may request clarifications |
| **Days 6-10** | Evaluate responses, request samples from 2-3 finalists |
| **Days 11-21** | Samples arrive; you evaluate against spec sheet |

---

## Evaluation Dashboard (When Responses Arrive)

**As each supplier responds, update the tracker:**

1. **Response Time:**
   - Log the time they responded in "Date Response Received"
   - Calculate hours elapsed in "Response Time (hrs)" column
   - Fast responses (< 24 hrs) = communication quality indicator

2. **Cost Data:**
   - Log their unit costs for 50, 100, 500 units
   - Log shipping cost to your address
   - Use `supplier-scoring.py` to calculate **landed cost** (unit cost + freight + duty)

3. **Qualitative Scores (1-5 scale):**
   - **Material Spec Quality:** Did they provide detailed material specs? (5 = comprehensive, 1 = vague)
   - **Communication Score:** Were they clear, responsive, professional? (5 = excellent, 1 = poor)
   - **Sample Lead Time:** Can they deliver samples by your deadline? (5 = 7 days, 1 = 30+ days)

**Run scoring:** Once you have 3+ responses:
```bash
python3 execution/supplier-scoring.py
```

---

## Decision Criteria (By Day 5)

**Rank suppliers by:**
1. **Communication score first** (40% of decision)
   - Response time < 24 hrs
   - Clear, professional tone
   - Answers all your questions completely

2. **Landed cost second** (15% of decision)
   - Must pass the margin gate (CS-01 ≤ $22 landed cost)
   - For comparison: you're targeting 45%+ contribution margin

3. **Lead time third** (15% of decision)
   - Samples by day 14-21 (must meet your timeline)
   - Bulk production in 20-30 days (acceptable range)

4. **Material/sample quality** (30% combined)
   - Detailed spec sheets (shows they know their materials)
   - Willingness to send material samples before you commit

**Example Score (out of 25):**
```
Supplier A: 22/25 → GO (proceed to samples)
Supplier B: 18/25 → MAYBE (get more info, request sample)
Supplier C: 15/25 → HOLD (consider backup, don't lead with)
```

---

## By End of Day 5: Make the Call

**Scenarios:**

| Scenario | Action |
|----------|--------|
| **1-2 suppliers score 20+/25** | Order samples from both (split risk) |
| **0 suppliers pass margin gate** | Re-scope products (cheaper materials) or pause launch |
| **High-scoring supplier slow to respond** | Use them as primary, 2nd supplier as backup |
| **All suppliers 15-18/25** | Get material samples from top 2-3 anyway, make final call on quality |

---

## Success Metrics for Day 1

By end of today, you should have:
- [ ] 5 supplier inquiry emails sent
- [ ] Supplier names and contact info logged in tracker
- [ ] Clear deadline communicated (Day 7-10 for quotes, Day 14-21 for samples)

By end of Day 5, you should have:
- [ ] 4+ supplier quote responses received
- [ ] Landed cost calculated for each (check: do they meet margin gate?)
- [ ] Top 2-3 suppliers identified for sample orders
- [ ] Decision made: GO (order samples) or NO-GO (modify product specs or pricing)

---

## Next: Sample Evaluation (Days 6-10)

Once samples arrive, evaluate against `research/product-selection.md` specifications:

**CS-01 Checklist:**
- [ ] Nylon exterior feels substantial (no thin spots)
- [ ] Zippers open/close smoothly 10x without snagging
- [ ] Padding is firm (doesn't compress permanently)
- [ ] Webbing loop is secure (no stitching separation)
- [ ] Buckle doesn't crack or fade

**CS-02 Checklist:**
- [ ] Mesh is tight, no holes or tears
- [ ] Anchor straps are reinforced at attachment points
- [ ] Buckles secure without twisting
- [ ] Overall weight < 0.5 lbs

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| **No supplier responses by Day 3** | Send follow-up email; may need to adjust timeline or broaden supplier search |
| **Supplier quotes 30%+ above target** | Cost assumption was off; either accept higher cost (re-price product) or simplify design |
| **Supplier wants 500-unit MOQ** | Negotiate down to 50 or find different supplier; not viable for test phase |
| **Sample quality doesn't match spec** | Send detailed feedback; request revision. If no improvement, move to next supplier |
| **Supplier goes silent after quote** | This is a red flag for communication quality; prioritize other supplier |

---

## Files You'll Use

- `supplier-outreach-template.md` — Email template (customize & send)
- `supplier-evaluation-tracker.csv` — Tracking spreadsheet (open in Excel)
- `supplier-scoring.py` — Scoring tool (run on Day 4-5 after responses arrive)
- `research/product-selection.md` — Product specs (use for quality checks on samples)
- `finance/unit-economics.md` — Cost targets (check margin gate on Day 5)

---

**Status:** Ready to launch. Reach out if you need clarification on any supplier question or help evaluating responses.
