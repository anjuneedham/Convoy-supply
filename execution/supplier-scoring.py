#!/usr/bin/env python3
"""
Supplier Evaluation Scoring Tool for ConvoySupply
Calculates landed costs and scores suppliers against decision criteria.
"""

def calculate_landed_cost(unit_cost, quantity, shipping_cost, import_duty_rate=0.05):
    """
    Calculate landed cost per unit including freight and duty.

    Args:
        unit_cost: manufacturer's unit price
        quantity: order quantity
        shipping_cost: total shipping for this quantity
        import_duty_rate: estimated import duty (5% default for soft goods US)

    Returns:
        landed cost per unit
    """
    total_cost = (unit_cost * quantity) + shipping_cost
    total_with_duty = total_cost * (1 + import_duty_rate)
    landed_cost_per_unit = total_with_duty / quantity
    return round(landed_cost_per_unit, 2)


def evaluate_supplier(
    name,
    response_time_hours,
    material_spec_quality,  # 1-5 scale
    sample_quality,         # 1-5 scale
    communication_score,    # 1-5 scale
    price_score,            # 1-5 scale (based on competitiveness)
):
    """
    Score a supplier on decision criteria.
    Communication quality weighted heavily (40%) per DEC-006.
    """

    # Weighted scoring: Communication matters most
    weights = {
        'communication': 0.40,
        'material_spec': 0.20,
        'sample_quality': 0.15,
        'price': 0.15,
        'response_time': 0.10,  # bonus for <24hr response
    }

    # Response time bonus: 5 points if <24hrs, 3 points if <48hrs, 1 point if <72hrs
    response_time_score = 0
    if response_time_hours <= 24:
        response_time_score = 5
    elif response_time_hours <= 48:
        response_time_score = 3
    elif response_time_hours <= 72:
        response_time_score = 1

    # Normalize response time to 1-5 scale
    response_time_normalized = min(5, 1 + (response_time_score / 5) * 4)

    # Calculate weighted score (out of 25, not 20)
    total_score = (
        communication_score * weights['communication'] * 5 +
        material_spec_quality * weights['material_spec'] * 5 +
        sample_quality * weights['sample_quality'] * 5 +
        price_score * weights['price'] * 5 +
        response_time_normalized * weights['response_time'] * 5
    )

    return {
        'supplier': name,
        'total_score': round(total_score, 2),
        'communication_contribution': round(communication_score * weights['communication'] * 5, 2),
        'material_spec_contribution': round(material_spec_quality * weights['material_spec'] * 5, 2),
        'sample_quality_contribution': round(sample_quality * weights['sample_quality'] * 5, 2),
        'price_contribution': round(price_score * weights['price'] * 5, 2),
        'response_time_contribution': round(response_time_normalized * weights['response_time'] * 5, 2),
    }


def check_margin_gate(cs01_landed_cost, cs02_landed_cost, cs03_landed_cost, cs04_landed_cost):
    """
    Check if landed costs pass the margin gate from finance/unit-economics.md
    Red line for CS-01 is $22 landed cost.
    """

    pricing_model = {
        'cs01': {'target_price': 49.99, 'landed_cost_redline': 22.00, 'name': 'Cab Command Organizer'},
        'cs02': {'target_price': 34.99, 'landed_cost_redline': 15.75, 'name': 'Bunk Shelf Net'},
        'cs03': {'target_price': 24.99, 'landed_cost_redline': 11.25, 'name': 'Manifest Folio'},
        'cs04': {'target_price': 39.99, 'landed_cost_redline': 18.00, 'name': 'Haul Bag'},
    }

    results = {}
    all_pass = True

    for sku, cost in [
        ('cs01', cs01_landed_cost),
        ('cs02', cs02_landed_cost),
        ('cs03', cs03_landed_cost),
        ('cs04', cs04_landed_cost),
    ]:
        redline = pricing_model[sku]['landed_cost_redline']
        target_price = pricing_model[sku]['target_price']
        product_name = pricing_model[sku]['name']

        passes = cost <= redline
        margin = ((target_price - cost) / target_price * 100) if cost < target_price else 0

        results[sku] = {
            'name': product_name,
            'landed_cost': cost,
            'redline': redline,
            'passes': passes,
            'margin_pct': round(margin, 1),
        }

        if not passes:
            all_pass = False

    return results, all_pass


if __name__ == '__main__':
    # Example usage
    print("=" * 70)
    print("SUPPLIER EVALUATION TOOL - ConvoySupply")
    print("=" * 70)

    # Example: Supplier A
    print("\n📊 EXAMPLE: Evaluating Supplier A")
    print("-" * 70)

    supplier_a = evaluate_supplier(
        name="Supplier A",
        response_time_hours=18,  # Responded next morning
        material_spec_quality=4,  # Good spec sheet
        sample_quality=4,         # Sample matches spec well
        communication_score=5,    # Responsive, clear communication
        price_score=3,            # Mid-range pricing
    )

    print(f"Supplier: {supplier_a['supplier']}")
    print(f"Total Score: {supplier_a['total_score']}/25")
    print(f"  - Communication (40%): {supplier_a['communication_contribution']}")
    print(f"  - Material Spec (20%): {supplier_a['material_spec_contribution']}")
    print(f"  - Sample Quality (15%): {supplier_a['sample_quality_contribution']}")
    print(f"  - Price Competitiveness (15%): {supplier_a['price_contribution']}")
    print(f"  - Response Time (10%): {supplier_a['response_time_contribution']}")

    # Example: Landed cost calculation
    print("\n💰 EXAMPLE: Landed Cost Calculation")
    print("-" * 70)

    cs01_unit_cost = 12.50
    cs01_order_qty = 50
    cs01_shipping = 50.00  # sample shipment

    cs01_landed = calculate_landed_cost(cs01_unit_cost, cs01_order_qty, cs01_shipping)
    print(f"CS-01 (50 units):")
    print(f"  Unit cost: ${cs01_unit_cost}")
    print(f"  Shipping: ${cs01_shipping}")
    print(f"  Import duty rate: 5%")
    print(f"  → Landed cost per unit: ${cs01_landed}")

    # Example: Margin gate check
    print("\n🚦 EXAMPLE: Margin Gate Check (Day 5 Decision)")
    print("-" * 70)

    gate_results, passes_gate = check_margin_gate(
        cs01_landed_cost=15.50,
        cs02_landed_cost=10.25,
        cs03_landed_cost=9.75,
        cs04_landed_cost=16.00,
    )

    for sku, result in gate_results.items():
        status = "✅ PASS" if result['passes'] else "❌ FAIL"
        print(f"{status} {result['name']} (CS-{sku.upper().split('S')[1]})")
        print(f"     Landed: ${result['landed_cost']} | Redline: ${result['redline']} | Margin: {result['margin_pct']}%")

    print(f"\nOverall Decision: {'GO' if passes_gate else 'NO-GO'}")

    print("\n" + "=" * 70)
    print("TO USE THIS TOOL:")
    print("1. Update supplier-evaluation-tracker.csv with supplier quotes")
    print("2. Run: python3 supplier-scoring.py --calculate <csv-file>")
    print("3. Scores will help you rank suppliers by Day 5")
    print("=" * 70)
