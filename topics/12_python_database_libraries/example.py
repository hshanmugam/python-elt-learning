import sqlite3
from pathlib import Path

try:
    from sqlalchemy import create_engine
except ImportError:
    create_engine = None


database_path = Path(__file__).parent / "db_library_demo.sqlite3"

# Use sqlite3 to show connector-style work with parameterized SQL
connection = sqlite3.connect(database_path)
connection.execute("PRAGMA journal_mode=MEMORY")
connection.execute("PRAGMA synchronous=OFF")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS customers (customer_id INTEGER, name TEXT)")
cursor.execute("DELETE FROM customers")
cursor.executemany(
    "INSERT INTO customers (customer_id, name) VALUES (?, ?)",
    [(101, "Alicia"), (102, "Marcus")],
)
connection.commit()

for row in cursor.execute("SELECT customer_id, name FROM customers ORDER BY customer_id"):
    print(row)

connection.close()

if create_engine is None:
    print("SQLAlchemy is not installed. Run: pip install sqlalchemy")
else:
    print("SQLAlchemy is available for engine-based database work.")
