try:
    import pandas as pd
except ImportError:
    print("pandas is not installed. Run: pip install pandas")
else:
    # Simulate raw file input as a DataFrame
    orders_df = pd.DataFrame(
        [
            {"order_id": 1, "customer_id": 101, "amount": 120.0, "status": "complete"},
            {"order_id": 2, "customer_id": 101, "amount": 80.0, "status": "complete"},
            {"order_id": 3, "customer_id": 102, "amount": 40.0, "status": "pending"},
        ]
    )

    # Standardize and enrich the dataset
    orders_df["status"] = orders_df["status"].str.upper()
    orders_df["tax"] = orders_df["amount"] * 0.1

    complete_df = orders_df[orders_df["status"] == "COMPLETE"]
    summary_df = complete_df.groupby("customer_id", as_index=False)["amount"].sum()
    summary_df = summary_df.rename(columns={"amount": "total_amount"})

    print("Enriched orders:")
    print(orders_df)
    print("\nCustomer summary:")
    print(summary_df)
