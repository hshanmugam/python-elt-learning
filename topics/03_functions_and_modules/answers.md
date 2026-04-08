# Topic 3 Answers

1. `def add_numbers(a, b): return a + b`
2. `def normalize_name(name): return name.strip().title()`
3. `def is_valid_amount(amount): return amount >= 0`
4. `def line_total(quantity, price): return quantity * price`
5. `def build_customer(customer_id, email): return {"customer_id": customer_id, "email": email}`
6. `def lowercase_names(names): return [name.lower() for name in names]`
7. `PIPELINE_NAME = "daily_orders_pipeline"`
8. `def print_load_status(rows_loaded): print(f"Loaded {rows_loaded} rows")`
9. `def get_customer_id(record): return record["customer_id"]`
10. `def reject_record(): return "Missing required field"`
11. Split code into more than one module when one file becomes too large or when logic belongs to different responsibilities such as extract, transform, and load.
12. `def build_location(city, country="USA"): return {"city": city, "country": country}`
