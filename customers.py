#Exercise 1

customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1200
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print(customer)

#Exercise 2

customer["phone"] = "555-123-4567"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)

#Exercise 3

print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist")


#Exercise 4

for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), the loop only returns the keys.
for key in customer:
    print(key)

#Exercise 5

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

tier = customer["tier"]
discount = tier_discounts.get(tier, 0)

price = 200
final_price = price * (1 - discount)

print(f"Tier: {tier}")
print(f"Discount: {discount * 100:.0f}%")
print(f"Final Price: ${final_price:.2f}")

#Exercise 6

customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "gold"},
    {"name": "Charlie", "tier": "silver"}
]

for person in customers:
    name = person["name"]
    tier = person["tier"]
    discount = tier_discounts.get(tier, 0)

    discount_amount = 300 * discount

    print(f"{name} ({tier}): ${discount_amount:.2f} discount")


#Exercise 7

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} - {details['stock']} remaining")


#Exercise 8

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_by_region = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    sales_by_region[region] = sales_by_region.get(region, 0) + amount

for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]}")