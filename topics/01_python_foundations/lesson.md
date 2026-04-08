# Topic 1: Python Foundations

## Core ideas

Python foundations include variables, data types, operators, and string formatting. These are the smallest building blocks of every pipeline script.

## Variables

A variable stores a value so you can reuse it later.

```python
source_name = "crm_export"
record_count = 1250
success_rate = 99.2
```

In ETL and ELT work, variables often hold file names, row counts, batch ids, and source system names.

## Common data types

- `str` for text values such as source names and dates before conversion
- `int` for row counts and ids
- `float` for amounts and measures
- `bool` for pass or fail flags
- `None` for missing values

## String formatting

Readable output matters in logs and debugging.

```python
pipeline_name = "daily_sales_load"
message = f"Pipeline {pipeline_name} loaded 125 rows."
```

## Type conversion

Raw source data often arrives as strings and must be converted.

```python
raw_quantity = "7"
quantity = int(raw_quantity)
```

Almost every ETL or ELT job begins by reading raw values, assigning them to variables, and converting them into the right types before loading or transforming them.
