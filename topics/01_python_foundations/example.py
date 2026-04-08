# Topic 1 example: Python foundations for pipeline work

# Store raw values from a source file or API
source_name = "crm_export"
raw_customer_id = "101"
raw_order_total = "249.50"
raw_is_active = "True"

# Convert string values into more useful Python types
customer_id = int(raw_customer_id)
order_total = float(raw_order_total)
is_active = raw_is_active == "True"

# Build a readable status message for logs or debugging
status_message = (
    f"Source={source_name}, customer_id={customer_id}, "
    f"order_total={order_total}, is_active={is_active}"
)

print(status_message)

# Simple validation logic starts with comparisons
minimum_order_total = 100.0
is_large_order = order_total >= minimum_order_total

print(f"Is this a large order? {is_large_order}")
