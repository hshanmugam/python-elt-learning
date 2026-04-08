# Topic 12: Python Database Libraries

## Core ideas

Python can connect to relational databases using driver libraries and higher-level tools. In production data engineering, this is how orchestration code submits SQL, writes data, and checks results.

## Why it matters for ETL and ELT

- Pipelines often load into PostgreSQL, SQL Server, MySQL, or cloud warehouses
- Parameterized SQL is safer than string-built SQL
- Transactions and connection management affect data reliability

## Key concepts

- connector libraries such as `psycopg`, `pyodbc`, and warehouse-specific clients
- parameter placeholders
- transactions and commits
- cursors and result fetching
- SQLAlchemy engines and abstractions

## Pipeline examples

- write transformed rows into a warehouse staging table
- execute a stored procedure after loading
- validate a row count after a batch finishes
