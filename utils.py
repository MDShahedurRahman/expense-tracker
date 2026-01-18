from datetime import datetime
from config import DATE_FORMAT


def validate_amount(amount):
    return amount > 0


def validate_date(date_str):
    try:
        datetime.strptime(date_str, DATE_FORMAT)
        return True
    except ValueError:
        return False


def generate_id(expenses):
    if not expenses:
        return 1
    return max(e["expense_id"] for e in expenses) + 1
