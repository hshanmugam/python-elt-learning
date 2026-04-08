import json
from pathlib import Path

project_folder = Path(__file__).parent
state_file = project_folder / "state.json"
raw_output_file = project_folder / "raw_incremental_payload.json"


def read_state():
    if not state_file.exists():
        return {"last_updated_at": "2026-04-08T08:00:00"}
    with state_file.open("r", encoding="utf-8") as file:
        return json.load(file)


def fetch_api_records():
    # Simulated API results for learning purposes
    return [
        {"ticket_id": 1, "updated_at": "2026-04-08T08:30:00", "status": "OPEN"},
        {"ticket_id": 2, "updated_at": "2026-04-08T09:30:00", "status": "CLOSED"},
        {"ticket_id": 3, "updated_at": "2026-04-08T10:45:00", "status": "OPEN"},
    ]


def filter_incremental(records, watermark):
    return [record for record in records if record["updated_at"] > watermark]


def main():
    state = read_state()
    watermark = state["last_updated_at"]
    records = fetch_api_records()
    incremental_records = filter_incremental(records, watermark)

    with raw_output_file.open("w", encoding="utf-8") as file:
        json.dump(incremental_records, file, indent=2)

    if incremental_records:
        new_watermark = max(record["updated_at"] for record in incremental_records)
    else:
        new_watermark = watermark

    with state_file.open("w", encoding="utf-8") as file:
        json.dump({"last_updated_at": new_watermark}, file, indent=2)

    print(f"Previous watermark: {watermark}")
    print(f"Incremental records loaded: {len(incremental_records)}")
    print(f"New watermark: {new_watermark}")


if __name__ == "__main__":
    main()
