# Topic 1 Answers

1. Example: `pipeline_name = "daily_load"`, `source_system = "erp"`, `batch_id = 1001`
2. `raw_rows = "150"` then `rows = int(raw_rows)`
3. `raw_amount = "89.95"` then `amount = float(raw_amount)`
4. `is_file_ready = True`
5. `message = f"Pipeline loaded {500} rows"`
6. `total = success_count + failure_count`
7. `is_large_batch = row_count > 1000`
8. `email_address = None`
9. `message = "Retry count: " + str(25)`
10.

```python
raw_id = "42"
raw_total = "18.5"
record_id = int(raw_id)
total = float(raw_total)
print(record_id, total)
```

11. `raw_discount = "0.10"` then `discount = float(raw_discount)`
12. `status = f"Source {source_name} read {rows_read} rows and loaded {rows_loaded} rows."`
