try:
    import pandas as pd
except ImportError:
    print("pandas is not installed. Run: pip install pandas")
else:
    # Build a small DataFrame that resembles staged sales data
    sales_df = pd.DataFrame(
        [
            {"order_id": 1, "customer_id": 101, "amount": 250.0, "status": "COMPLETE"},
            {"order_id": 2, "customer_id": 101, "amount": 125.0, "status": "COMPLETE"},
            {"order_id": 3, "customer_id": 102, "amount": 75.0, "status": "PENDING"},
        ]
    )

    # Filter completed orders and create a grouped reporting output
    complete_df = sales_df[sales_df["status"] == "COMPLETE"]
    summary_df = complete_df.groupby("customer_id", as_index=False)["amount"].sum()
    summary_df = summary_df.rename(columns={"amount": "total_amount"})

    print("Raw staged data:")
    print(sales_df)
    print("\nCurated summary:")
    print(summary_df)
