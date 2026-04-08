# Topic 15: Warehouse-Style Transformations

## Core ideas

Warehouse-style transformations take raw or staged data and convert it into analytics-friendly structures such as dimensions, facts, and curated summary tables.

## Why it matters for ETL and ELT

- business users rely on clean reporting models
- raw source data is rarely shaped ideally for analytics
- Python engineers often prepare data before or around SQL-based modeling

## Key concepts

- raw, staging, and curated layers
- dimensions and facts
- business keys and surrogate keys
- deduplication
- incremental loads
- type standardization and conformed dimensions

## Pipeline examples

- build a customer dimension from CRM data
- build a sales fact from order events
- create a reporting summary by customer, product, or date
