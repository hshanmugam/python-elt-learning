import sqlite3
from pathlib import Path

# Topic 8 example: load transformed rows into a small SQLite warehouse

topic_folder = Path(__file__).parent
database_path = topic_folder / "warehouse.db"

rows = [
    (1, 101, 250.0),
    (2, 101, 125.0),
    (3, 102, 80.0),
]

connection = sqlite3.connect(database_path)
cursor = connection.cursor()

# Use an in-memory journal so the demo runs reliably in restricted environments
cursor.execute("PRAGMA journal_mode=MEMORY")
cursor.execute("PRAGMA synchronous=OFF")

# Create a warehouse-like fact table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS sales (
        order_id INTEGER,
        customer_id INTEGER,
        amount REAL
    )
    """
)

# Reset the demo table so reruns stay easy to understand
cursor.execute("DELETE FROM sales")

# Load the transformed rows
cursor.executemany(
    "INSERT INTO sales (order_id, customer_id, amount) VALUES (?, ?, ?)",
    rows,
)

connection.commit()

# Query an aggregated result as a mini reporting example
for result in cursor.execute(
    "SELECT customer_id, SUM(amount) AS total_amount FROM sales GROUP BY customer_id"
):
    print(result)

connection.close()
