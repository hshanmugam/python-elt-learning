# Topic 9: NumPy for Data Engineering

## Core ideas

NumPy is a foundational Python library for working with arrays and numeric operations at scale. Even when you use pandas, many operations rely on NumPy underneath.

## Why it matters for ETL and ELT

- It encourages column-style thinking instead of row-by-row loops
- It performs numeric calculations efficiently
- It helps with reshaping, filtering, and standardizing data before loading

## Key concepts

- arrays instead of regular Python lists for numerical work
- vectorized calculations
- boolean filtering
- aggregation with functions like `sum`, `mean`, and `max`
- reshaping arrays for matrix-style operations

## Pipeline examples

- normalize numeric scores
- calculate totals for many records at once
- detect outliers in sensor or event data
- prepare values for machine learning or reporting workloads
