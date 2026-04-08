# Topic 3 example: reusable pipeline functions

def clean_name(name):
    # Remove extra spaces and standardize casing
    return name.strip().title()


def build_customer_record(customer_id, customer_name):
    # Return a dictionary that can move to the next pipeline step
    return {
        "customer_id": customer_id,
        "customer_name": clean_name(customer_name),
    }


record = build_customer_record(101, "  aLICIA jONES ")
print(record)
