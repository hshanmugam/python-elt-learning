# Topic 7 Answers

1. `class PipelineJob: pass`
2. `def __init__(self, name): self.name = name`
3. `def run(self): print(f"Running {self.name}")`
4. `job = PipelineJob("daily_orders")`
5. Use `@dataclass` from `dataclasses`
6. `customer_id: int`, `name: str`, `country: str`
7. `def is_usa(self): return self.country == "USA"`
8. A dataclass automatically builds methods like `__init__`, which reduces repetitive code for record objects.
9. `class Validator: def is_valid_amount(self, amount): return amount >= 0`
10. `validator = Validator(); print(validator.is_valid_amount(20))`
11. `def summary(self): return f"Customer {self.customer_id} from {self.country}"`
12. Classes group related data and behavior, which makes large pipeline code easier to manage.
