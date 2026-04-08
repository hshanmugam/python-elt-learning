import json
from pathlib import Path

try:
    import requests
except ImportError:
    requests = None


def simulate_api_response():
    # Use a local payload so the example stays runnable without network access
    return {
        "page": 1,
        "has_more": False,
        "results": [
            {"order_id": 1, "updated_at": "2026-04-08T09:00:00", "amount": 200.0},
            {"order_id": 2, "updated_at": "2026-04-08T10:00:00", "amount": 350.0},
        ],
    }


payload = simulate_api_response()
output_path = Path(__file__).parent / "api_payload.json"

# Persist the payload as if we had just extracted it from an API
with output_path.open("w", encoding="utf-8") as file:
    json.dump(payload, file, indent=2)

print(f"Saved {len(payload['results'])} records to {output_path.name}")

if requests is None:
    print("requests is not installed. Run: pip install requests")
else:
    print("requests is available for real HTTP calls.")
