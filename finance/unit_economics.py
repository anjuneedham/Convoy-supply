#!/usr/bin/env python3
"""
ConvoySupply unit economics calculator.

Every figure in finance/unit-economics.md is produced by this script.
Change the inputs, re-run, paste the output. Nothing in the doc is a
hard-coded conclusion.

    python3 finance/unit_economics.py

ALL COST INPUTS ARE ESTIMATES [A] PENDING SUPPLIER QUOTES.
Replace LANDED_COST and SHIP_COST with real figures on Day 5.
"""

from dataclasses import dataclass

# ---------------------------------------------------------------- inputs

# Shopify Payments, Basic plan: 2.9% + $0.30 online  [V7]
PAY_PCT, PAY_FIXED = 0.029, 0.30

# Shopify Basic: $39/mo month-to-month  [V7]
PLATFORM_MONTHLY = 39.00
ORDERS_PER_MONTH = 60          # [A] planning assumption; divides the fixed cost

REFUND_RATE = 0.05             # [A] 5% allowance on gross product revenue
FREE_SHIP_THRESHOLD = 75.00
FLAT_SHIP_CHARGE = 6.95        # charged to customer below the threshold


@dataclass
class Offer:
    name: str
    price: float               # product revenue
    landed_cost: float         # [A] unit cost + freight + duty, delivered to us
    ship_cost: float           # [A] what WE pay to ship it out
    packaging: float           # mailer + insert card

    @property
    def ship_revenue(self) -> float:
        return 0.0 if self.price >= FREE_SHIP_THRESHOLD else FLAT_SHIP_CHARGE

    @property
    def gross(self) -> float:
        return self.price + self.ship_revenue

    @property
    def payment_fee(self) -> float:
        return self.gross * PAY_PCT + PAY_FIXED

    @property
    def refund_allowance(self) -> float:
        return self.price * REFUND_RATE

    @property
    def platform_cost(self) -> float:
        return PLATFORM_MONTHLY / ORDERS_PER_MONTH

    @property
    def variable_costs(self) -> float:
        return (self.landed_cost + self.ship_cost + self.payment_fee
                + self.packaging + self.refund_allowance + self.platform_cost)

    @property
    def gross_profit(self) -> float:
        """Price less landed cost only. The classic gross margin line."""
        return self.price - self.landed_cost

    @property
    def gross_margin(self) -> float:
        return self.gross_profit / self.price

    @property
    def contribution(self) -> float:
        """What is left to pay for advertising and profit. = break-even CPA."""
        return self.gross - self.variable_costs

    @property
    def contribution_margin(self) -> float:
        return self.contribution / self.price

    # break-even CPA IS contribution: spend more than this per order and you lose money
    @property
    def breakeven_cpa(self) -> float:
        return self.contribution

    @property
    def breakeven_roas(self) -> float:
        """On product revenue. Meta reports on order value — see the doc."""
        return self.price / self.contribution

    def target_cpa(self, target_margin: float) -> float:
        return self.contribution - (self.price * target_margin)

    def target_roas(self, target_margin: float) -> float:
        t = self.target_cpa(target_margin)
        return self.price / t if t > 0 else float("inf")


# ---------------------------------------------------------- the catalogue
# Landed and shipping costs are [A] estimates. Replace after supplier quotes.

OFFERS = [
    Offer("CS-01 Cab Command Organizer", 54.99, 15.50, 7.50, 0.85),
    Offer("CS-02 Bunk Shelf Net",        29.99,  6.80, 5.50, 0.60),
    Offer("CS-03 Manifest Folio",        27.99,  6.50, 5.50, 0.60),
    Offer("CS-04 Haul Bag",              49.99, 14.00, 8.50, 0.95),
    Offer("Cab Reset Kit",               89.00, 28.80, 8.50, 1.20),
    Offer("Full Rig Kit",               129.00, 42.80,10.00, 1.50),
]

# order mix scenarios: (label, {offer name: share})
MIXES = {
    "Base":        {"CS-01 Cab Command Organizer": .55, "Cab Reset Kit": .35, "Full Rig Kit": .10},
    "Pessimistic": {"CS-02 Bunk Shelf Net": .40, "CS-01 Cab Command Organizer": .35,
                    "Cab Reset Kit": .20, "Full Rig Kit": .05},
    "Optimistic":  {"CS-01 Cab Command Organizer": .40, "Cab Reset Kit": .40, "Full Rig Kit": .20},
}

TARGET_MARGIN = 0.30   # contribution profit retained after advertising


def money(x): return f"${x:,.2f}"
def pct(x):   return f"{x*100:.1f}%"


def main():
    by_name = {o.name: o for o in OFFERS}

    print("=" * 78)
    print("CONVOYSUPPLY UNIT ECONOMICS".center(78))
    print("ALL COST INPUTS ARE [A] ESTIMATES PENDING SUPPLIER QUOTES".center(78))
    print("=" * 78)

    print(f"\nShared inputs: payment {PAY_PCT*100:.1f}% + {money(PAY_FIXED)} | "
          f"platform {money(PLATFORM_MONTHLY)}/mo over {ORDERS_PER_MONTH} orders "
          f"= {money(PLATFORM_MONTHLY/ORDERS_PER_MONTH)}/order | "
          f"refund allowance {pct(REFUND_RATE)} | free shipping over {money(FREE_SHIP_THRESHOLD)}")

    print("\n" + "-" * 78)
    print("PER-OFFER BREAKDOWN")
    print("-" * 78)
    for o in OFFERS:
        print(f"\n{o.name} — {money(o.price)}")
        print(f"  Product revenue        {money(o.price):>10}")
        print(f"  Shipping charged       {money(o.ship_revenue):>10}")
        print(f"  {'GROSS':<22} {money(o.gross):>10}")
        print(f"  - Landed cost      [A] {money(-o.landed_cost):>10}")
        print(f"  - Outbound shipping[A] {money(-o.ship_cost):>10}")
        print(f"  - Payment fee          {money(-o.payment_fee):>10}")
        print(f"  - Packaging            {money(-o.packaging):>10}")
        print(f"  - Refund allowance     {money(-o.refund_allowance):>10}")
        print(f"  - Platform             {money(-o.platform_cost):>10}")
        print(f"  {'CONTRIBUTION':<22} {money(o.contribution):>10}   (before advertising)")
        print(f"     Gross margin        {pct(o.gross_margin):>10}")
        print(f"     Contribution margin {pct(o.contribution_margin):>10}")
        print(f"     Break-even CPA      {money(o.breakeven_cpa):>10}")
        print(f"     Break-even ROAS     {o.breakeven_roas:>10.2f}")
        print(f"     Target CPA  @{pct(TARGET_MARGIN)}  {money(o.target_cpa(TARGET_MARGIN)):>10}")
        print(f"     Target ROAS @{pct(TARGET_MARGIN)}  {o.target_roas(TARGET_MARGIN):>10.2f}")

    print("\n" + "-" * 78)
    print(f"BLENDED BY ORDER MIX  (target margin {pct(TARGET_MARGIN)})")
    print("-" * 78)
    print(f"{'Scenario':<14}{'AOV':>10}{'Contrib':>10}{'CM%':>8}"
          f"{'BE CPA':>10}{'BE ROAS':>10}{'Tgt CPA':>10}{'Tgt ROAS':>10}")
    for label, mix in MIXES.items():
        aov     = sum(by_name[n].price        * s for n, s in mix.items())
        contrib = sum(by_name[n].contribution * s for n, s in mix.items())
        tgt_cpa = contrib - aov * TARGET_MARGIN
        print(f"{label:<14}{money(aov):>10}{money(contrib):>10}{pct(contrib/aov):>8}"
              f"{money(contrib):>10}{aov/contrib:>10.2f}"
              f"{money(tgt_cpa):>10}{(aov/tgt_cpa if tgt_cpa > 0 else float('inf')):>10.2f}")

    print("\n" + "-" * 78)
    print("SENSITIVITY — CS-01 contribution if landed cost moves")
    print("-" * 78)
    base = by_name["CS-01 Cab Command Organizer"]
    print(f"{'Landed cost':>14}{'Contribution':>16}{'CM%':>10}{'BE CPA':>12}")
    for lc in (10.00, 12.50, 15.50, 18.00, 20.00, 22.00, 25.00):
        o = Offer(base.name, base.price, lc, base.ship_cost, base.packaging)
        flag = "  <- modeled" if abs(lc - base.landed_cost) < 0.01 else ""
        print(f"{money(lc):>14}{money(o.contribution):>16}"
              f"{pct(o.contribution_margin):>10}{money(o.breakeven_cpa):>12}{flag}")

    print("\n" + "-" * 78)
    print("WHAT A GIVEN CPA MEANS  (base mix)")
    print("-" * 78)
    mix = MIXES["Base"]
    aov     = sum(by_name[n].price        * s for n, s in mix.items())
    contrib = sum(by_name[n].contribution * s for n, s in mix.items())
    print(f"{'CPA':>8}{'Profit/order':>15}{'Margin on AOV':>16}{'Verdict':>22}")
    for cpa in (10, 15, 20, 25, 30, 35, 39.16, 45, 50):
        p = contrib - cpa
        if   p <= 0:            v = "LOSS - stop"
        elif p < aov * 0.10:    v = "Marginal"
        elif p < aov * 0.25:    v = "Workable"
        else:                   v = "Scale it"
        print(f"{money(cpa):>8}{money(p):>15}{pct(p/aov):>16}{v:>22}")

    print("\n" + "=" * 78)
    print("Every cost above is an assumption until supplier quotes land (Day 5).")
    print("=" * 78)


if __name__ == "__main__":
    main()
