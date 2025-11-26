import json
import logging
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"

def get_airport_name(code: str) -> str:
    json_path = DATA_DIR / "airports.json"
    with json_path.open(encoding="utf-8") as f:
        airports = json.load(f)

    try:
        return airports[code]["airport_name"]
    except KeyError:
        raise ValueError(f"Airport code not found in JSON: {code}")


