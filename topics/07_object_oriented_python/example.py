from dataclasses import dataclass


@dataclass
class OrderRecord:
    # Dataclasses automatically create an initializer for these fields
    order_id: int
    customer_id: int
    amount: float

    def is_high_value(self):
        # Business logic can live on the object itself
        return self.amount >= 200.0


order = OrderRecord(order_id=1, customer_id=101, amount=250.0)
print(order)
print(f"High value order? {order.is_high_value()}")
