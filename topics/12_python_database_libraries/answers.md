# Topic 12 Answers

1. It opens connections and sends SQL or data between Python and a database system.
2. `psycopg` or `psycopg2`
3. `pyodbc`
4. Parameterized SQL keeps data values separate from SQL text, which improves safety and correctness.
5. `INSERT INTO customers (customer_id, name) VALUES (?, ?)`
6. It permanently saves the current transaction.
7. A cursor executes SQL and reads results.
8. SQLAlchemy can simplify connection management and SQL construction patterns.
9. Plain string formatting can create SQL injection risks or broken SQL when values contain special characters.
10. Cleanup matters so that connections are released and locks are not left behind.
11. Loading transformed rows into a staging table.
12. A low-level connector focuses on direct SQL execution, while a higher-level abstraction provides more structure and convenience.
