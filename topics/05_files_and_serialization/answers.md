# Topic 5 Answers

1. `import csv`
2. `import json`
3. `from pathlib import Path`
4. `with open("log.txt", "w", encoding="utf-8") as file: file.write("Pipeline started")`
5. `with open("log.txt", "r", encoding="utf-8") as file: print(file.read())`
6. Use `csv.DictWriter` with `writerows(rows)`
7. Use `csv.DictReader(file)` and cast to `list`
8. `json_text = json.dumps({"customer_id": 101})`
9. `json.dump({"customer_id": 101}, file)`
10. `row = json.load(file)`
11. `path = Path("data") / "raw" / "customers.csv"`
12. The `with` block closes the file automatically even if an error happens.
