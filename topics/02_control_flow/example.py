# Topic 2 example: control flow for record validation

records = [
    {"customer_id": 101, "order_total": 250.0},
    {"customer_id": 102, "order_total": -10.0},
    {"customer_id": 103, "order_total": 90.0},
]

valid_records = []
invalid_records = []

for record in records:
    # Separate valid and invalid records using an if statement
    if record["order_total"] < 0:
        invalid_records.append(record)
        continue

    # Keep valid records for the next pipeline step
    valid_records.append(record)

print(f"Valid records: {len(valid_records)}")
print(f"Invalid records: {len(invalid_records)}")

# Create a derived list using a comprehension
customer_ids = [record["customer_id"] for record in valid_records]
print(f"Valid customer ids: {customer_ids}")
