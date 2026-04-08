import csv
import json
from pathlib import Path

# Topic 5 example: create small staged files for a pipeline demo

topic_folder = Path(__file__).parent
csv_path = topic_folder / "sample_orders.csv"
json_path = topic_folder / "sample_orders.json"

rows = [
    {"order_id": "1", "customer_id": "101", "amount": "250.00"},
    {"order_id": "2", "customer_id": "102", "amount": "125.50"},
]

# Write a CSV file that simulates raw extracted data
with csv_path.open("w", newline="", encoding="utf-8") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["order_id", "customer_id", "amount"])
    writer.writeheader()
    writer.writerows(rows)

# Read the CSV file back into memory
with csv_path.open("r", newline="", encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)
    csv_rows = list(reader)

# Write a JSON file for a semi-structured version of the same data
with json_path.open("w", encoding="utf-8") as json_file:
    json.dump(csv_rows, json_file, indent=2)

print(f"Wrote {len(csv_rows)} rows to {csv_path.name} and {json_path.name}")
