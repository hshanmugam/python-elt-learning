import json
import sqlite3
from pathlib import Path

project_folder = Path(__file__).parent
database_file = project_folder / "reporting_mart_demo.sqlite3"
json_file = project_folder / "api_orders.json"


def create_api_payload():
    # Simulate an API response with nested event data
    payload = [
        {"order_id": 1, "customer_id": 101, "amount": 200.0, "status": "COMPLETE"},
        {"order_id": 2, "customer_id": 101, "amount": 150.0, "status": "COMPLETE"},
        {"order_id": 3, "customer_id": 102, "amount": 75.0, "status": "PENDING"},
    ]
    with json_file.open("w", encoding="utf-8") as file:
        json.dump(payload, file, indent=2)


def load_raw_events(connection):
    with json_file.open("r", encoding="utf-8") as file:
        payload = json.load(file)

    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS raw_orders (
            order_id INTEGER,
            customer_id INTEGER,
            amount REAL,
            status TEXT
        )
        """
    )
    cursor.execute("DELETE FROM raw_orders")
    cursor.executemany(
        "INSERT INTO raw_orders (order_id, customer_id, amount, status) VALUES (?, ?, ?, ?)",
        [
            (row["order_id"], row["customer_id"], row["amount"], row["status"])
            for row in payload
        ],
    )
    connection.commit()


def build_reporting_table(connection):
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS customer_sales_summary (
            customer_id INTEGER,
            total_amount REAL
        )
        """
    )
    cursor.execute("DELETE FROM customer_sales_summary")
    cursor.execute(
        """
        INSERT INTO customer_sales_summary (customer_id, total_amount)
        SELECT customer_id, SUM(amount) AS total_amount
        FROM raw_orders
        WHERE status = 'COMPLETE'
        GROUP BY customer_id
        """
    )
    connection.commit()


def main():
    create_api_payload()
    connection = sqlite3.connect(database_file)
    connection.execute("PRAGMA journal_mode=MEMORY")
    connection.execute("PRAGMA synchronous=OFF")
    load_raw_events(connection)
    build_reporting_table(connection)

    cursor = connection.cursor()
    for row in cursor.execute("SELECT customer_id, total_amount FROM customer_sales_summary"):
        print(row)

    connection.close()


if __name__ == "__main__":
    main()
