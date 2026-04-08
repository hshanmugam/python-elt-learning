import sqlite3
from pathlib import Path

database_path = Path(__file__).parent / "warehouse_transform_demo.sqlite3"
connection = sqlite3.connect(database_path)
connection.execute("PRAGMA journal_mode=MEMORY")
connection.execute("PRAGMA synchronous=OFF")
cursor = connection.cursor()

# Create raw staging tables that simulate source loads
cursor.execute("CREATE TABLE IF NOT EXISTS stg_customers (customer_id INTEGER, customer_name TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS stg_orders (order_id INTEGER, customer_id INTEGER, amount REAL)")
cursor.execute("DELETE FROM stg_customers")
cursor.execute("DELETE FROM stg_orders")

cursor.executemany(
    "INSERT INTO stg_customers (customer_id, customer_name) VALUES (?, ?)",
    [(101, "Alicia"), (102, "Marcus")],
)
cursor.executemany(
    "INSERT INTO stg_orders (order_id, customer_id, amount) VALUES (?, ?, ?)",
    [(1, 101, 200.0), (2, 101, 150.0), (3, 102, 90.0)],
)

# Build curated warehouse-style outputs
cursor.execute("CREATE TABLE IF NOT EXISTS dim_customers (customer_id INTEGER, customer_name TEXT)")
cursor.execute("DELETE FROM dim_customers")
cursor.execute("INSERT INTO dim_customers SELECT DISTINCT customer_id, customer_name FROM stg_customers")

cursor.execute(
    "CREATE TABLE IF NOT EXISTS fct_orders (order_id INTEGER, customer_id INTEGER, amount REAL)"
)
cursor.execute("DELETE FROM fct_orders")
cursor.execute("INSERT INTO fct_orders SELECT order_id, customer_id, amount FROM stg_orders")

cursor.execute(
    """
    SELECT c.customer_name, SUM(f.amount) AS total_amount
    FROM fct_orders f
    JOIN dim_customers c ON f.customer_id = c.customer_id
    GROUP BY c.customer_name
    ORDER BY c.customer_name
    """
)

for row in cursor.fetchall():
    print(row)

connection.commit()
connection.close()
