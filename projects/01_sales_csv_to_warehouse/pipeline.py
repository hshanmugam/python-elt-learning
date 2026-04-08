import csv
import logging
import sqlite3
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")

project_folder = Path(__file__).parent
input_file = project_folder / "sales_input.csv"
database_file = project_folder / "sales_warehouse_demo.sqlite3"


def create_sample_input():
    # Create a small input file so the project can be run immediately
    rows = [
        {"order_id": "1", "customer_id": "101", "amount": "250.00"},
        {"order_id": "2", "customer_id": "102", "amount": "-12.00"},
        {"order_id": "3", "customer_id": "103", "amount": "90.50"},
    ]
    with input_file.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["order_id", "customer_id", "amount"])
        writer.writeheader()
        writer.writerows(rows)


def extract_rows():
    with input_file.open("r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def transform_rows(rows):
    clean_rows = []
    rejected_rows = []

    for row in rows:
        try:
            transformed_row = (
                int(row["order_id"]),
                int(row["customer_id"]),
                float(row["amount"]),
            )
            if transformed_row[2] < 0:
                rejected_rows.append(row)
                continue
            clean_rows.append(transformed_row)
        except ValueError:
            rejected_rows.append(row)

    return clean_rows, rejected_rows


def load_rows(rows):
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    # Use an in-memory journal so the project runs in restricted environments
    cursor.execute("PRAGMA journal_mode=MEMORY")
    cursor.execute("PRAGMA synchronous=OFF")
    cursor.execute(
        """
        CREATE TABLE sales (
            order_id INTEGER,
            customer_id INTEGER,
            amount REAL
        )
        """
    )
    cursor.executemany(
        "INSERT INTO sales (order_id, customer_id, amount) VALUES (?, ?, ?)",
        rows,
    )
    connection.commit()
    cursor.execute("SELECT COUNT(*), SUM(amount) FROM sales")
    summary = cursor.fetchone()
    connection.close()
    return summary


def main():
    create_sample_input()
    extracted_rows = extract_rows()
    clean_rows, rejected_rows = transform_rows(extracted_rows)
    count_loaded, total_amount = load_rows(clean_rows)
    logging.info("Extracted rows: %s", len(extracted_rows))
    logging.info("Rejected rows: %s", len(rejected_rows))
    logging.info("Loaded rows: %s", count_loaded)
    logging.info("Total clean amount: %s", total_amount)


if __name__ == "__main__":
    main()
