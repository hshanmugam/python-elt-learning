# Topic 15 Answers

1. Raw stores source-like data, staging prepares and standardizes it, and curated presents analytics-ready outputs.
2. A dimension table stores descriptive business attributes such as customer name or product category.
3. A fact table stores measurable business events such as sales amounts or order counts.
4. `customer_id` or `order_id`
5. Deduplication prevents duplicate records from distorting downstream reporting.
6. Load only records newer than the last processed timestamp or key.
7. Standardized types reduce reporting errors and broken joins.
8. Customer name, country, segment, or signup date
9. Sales amount, quantity, discount amount, or revenue
10. Curated tables are easier because they already reflect business logic and reporting-friendly structure.
11. Convert raw order events into a fact table joined to customer and date dimensions.
12. Python may orchestrate extraction and validation while SQL performs set-based warehouse transformations.
