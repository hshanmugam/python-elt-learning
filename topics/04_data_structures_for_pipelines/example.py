# Topic 4 example: pipeline-friendly data structures

# Each dictionary represents one business record
records = [
    {"customer_id": 101, "country": "USA", "amount": 120.0},
    {"customer_id": 102, "country": "CAN", "amount": 85.0},
    {"customer_id": 101, "country": "USA", "amount": 120.0},
]

# Use a set to track unique customer ids
unique_customer_ids = set()

for record in records:
    unique_customer_ids.add(record["customer_id"])

print(f"Unique customers: {unique_customer_ids}")

# Use a dictionary to summarize total amount by country
totals_by_country = {}

for record in records:
    country = record["country"]
    totals_by_country[country] = totals_by_country.get(country, 0) + record["amount"]

print(totals_by_country)
