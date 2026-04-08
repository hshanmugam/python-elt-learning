# Topic 6 Answers

1. `try: value = int("12")`
2. `except ValueError: print("Conversion failed")`
3. `finally: print("Finished")`
4. `import logging`
5. `logging.basicConfig(level=logging.INFO)`
6. `logging.info("Pipeline started")`
7. `logging.error("Rejected record: missing customer_id")`
8. Use `try`/`except` inside a loop and `continue` on bad values
9. Use `WARNING` when something unusual happened but the system can still continue safely.
10. `except KeyError: print("Missing customer_id")`
11. `def safe_float(value): ... return None on ValueError`
12. Logs help you understand runtime behavior, failures, counts, and where a pipeline stopped.
