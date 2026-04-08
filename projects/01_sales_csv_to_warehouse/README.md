# Project 1: Sales CSV to Warehouse

## Scenario

A retail company receives a daily sales CSV export from a store system. The data engineering team must validate it, transform it, and load it into a warehouse table for reporting.

## ETL flow

1. Extract rows from CSV
2. Transform numeric fields into the correct Python types
3. Reject rows with invalid amounts
4. Load clean rows into SQLite
5. Print a sales summary
