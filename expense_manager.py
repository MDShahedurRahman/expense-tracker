from expense import Expense
from utils import generate_id, validate_amount, validate_date


def add_expense(expenses, title, amount, category, date):
    expense_id = generate_id(expenses)
    expense = Expense(expense_id, title, amount, category, date)
    expenses.append(expense.to_dict())
    return expenses
