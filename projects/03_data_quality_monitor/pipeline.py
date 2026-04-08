import json
from dataclasses import dataclass
from pathlib import Path

project_folder = Path(__file__).parent
report_file = project_folder / "quality_report.json"


@dataclass
class QualityIssue:
    record_id: int
    issue: str


class QualityChecker:
    def __init__(self):
        # Supported countries can be adjusted as business rules change
        self.allowed_countries = {"USA", "CAN"}

    def validate(self, record):
        issues = []

        if not record.get("customer_id"):
            issues.append("Missing customer_id")

        if record.get("amount", 0) < 0:
            issues.append("Negative amount")

        if record.get("country") not in self.allowed_countries:
            issues.append("Unsupported country")

        return issues


def main():
    records = [
        {"record_id": 1, "customer_id": 101, "amount": 100.0, "country": "USA"},
        {"record_id": 2, "customer_id": None, "amount": 55.0, "country": "USA"},
        {"record_id": 3, "customer_id": 103, "amount": -1.0, "country": "CAN"},
        {"record_id": 4, "customer_id": 104, "amount": 40.0, "country": "MEX"},
    ]

    checker = QualityChecker()
    issues = []

    for record in records:
        record_issues = checker.validate(record)
        for issue in record_issues:
            issues.append(QualityIssue(record_id=record["record_id"], issue=issue))

    with report_file.open("w", encoding="utf-8") as file:
        json.dump([issue.__dict__ for issue in issues], file, indent=2)

    print(f"Quality issues found: {len(issues)}")
    print(f"Report written to: {report_file.name}")


if __name__ == "__main__":
    main()
