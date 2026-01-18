from expense import Expense
from utils import generate_id, validate_amount, validate_date


def add_expense(expenses, title, amount, category, date):
    if not validate_amount(amount):
        raise ValueError("Invalid amount")
    if not validate_date(date):
        raise ValueError("Invalid date")

    expense_id = generate_id(expenses)
    expense = Expense(expense_id, title, amount, category, date)
    expenses.append(expense.to_dict())
    return expenses


def delete_expense(expenses, expense_id):
    return [e for e in expenses if e["expense_id"] != expense_id]
