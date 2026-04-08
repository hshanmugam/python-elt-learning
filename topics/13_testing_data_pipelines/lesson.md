# Topic 13: Testing Data Pipelines

## Core ideas

Pipeline code should be tested just like application code. Testing helps you catch logic errors before they corrupt reporting data or break scheduled jobs.

## Why it matters for ETL and ELT

- transformations must produce expected outputs
- validation rules should behave predictably
- edge cases such as nulls, duplicates, and bad amounts should be covered

## Key concepts

- unit testing
- assertions
- test fixtures
- expected versus actual results
- pytest structure
- data quality checks alongside code tests

## Pipeline examples

- test a tax calculation function
- test that invalid rows are rejected
- test that only complete orders appear in a reporting output
