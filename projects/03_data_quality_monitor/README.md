# Project 3: Data Quality Monitor

## Scenario

A data platform team wants a reusable quality check step that can run after a pipeline load and flag records with missing keys, invalid amounts, or unsupported countries.

## Data quality flow

1. Read a batch of records
2. Apply validation rules
3. Separate passed and failed rows
4. Write a quality report
5. Summarize findings
