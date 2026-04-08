# Topic 10 Answers

1. `import pandas as pd`
2. `df = pd.DataFrame([{"customer_id": 101, "amount": 50.0}])`
3. `df["amount"]`
4. `df[df["amount"] > 100]`
5. `df["tax"] = df["amount"] * 0.1`
6. `df = df.rename(columns={"amount": "order_amount"})`
7. `df.isna().sum()`
8. `df["country"] = df["country"].fillna("USA")`
9. `df.groupby("customer_id", as_index=False)["amount"].sum()`
10. `orders_df.merge(customers_df, on="customer_id", how="left")`
11. DataFrames make tabular filtering, transformation, joining, and aggregation much easier to express.
12. pandas is often better when you need to transform many columns or aggregate large tabular datasets.
