import logging

# Topic 6 example: log pipeline progress and handle a bad source value

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")

raw_amounts = ["100.50", "bad-value", "75.25"]
clean_amounts = []

for raw_amount in raw_amounts:
    try:
        # Attempt to convert raw text into a numeric value
        amount = float(raw_amount)
        clean_amounts.append(amount)
        logging.info("Converted amount %s", raw_amount)
    except ValueError:
        # Capture the failure but keep the batch moving
        logging.error("Failed to convert amount: %s", raw_amount)

logging.info("Finished processing %s clean amounts", len(clean_amounts))
