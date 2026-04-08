# Topic 8 Answers

1. `import sqlite3`
2. `connection = sqlite3.connect("demo.db")`
3. `cursor.execute("CREATE TABLE customers (customer_id INTEGER, name TEXT)")`
4. `cursor.execute("INSERT INTO customers (customer_id, name) VALUES (?, ?)", (101, "Alicia"))`
5. `cursor.execute("SELECT * FROM customers"); print(cursor.fetchall())`
6. Parameter placeholders help separate SQL from values safely.
7. `connection.commit()`
8. `connection.close()`
9. `cursor.execute("CREATE TABLE orders (order_id INTEGER, amount REAL)")`
10. Insert rows with `executemany` and run `SELECT SUM(amount) FROM orders`
11. ETL transforms data before loading it into the target. ELT loads data first and transforms it inside the target system.
12. SQLite is lightweight, built into Python, and easy to use without external setup.
