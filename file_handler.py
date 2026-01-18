import json
from config import DATA_FILE


def load_expenses():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
