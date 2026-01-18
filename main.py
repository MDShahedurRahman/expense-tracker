from file_handler import load_expenses, save_expenses
from expense_manager import add_expense, delete_expense
from report import total_expenses


def main():
    expenses = load_expenses()
    expenses = add_expense(expenses, "Lunch", 12.5, "Food", "2026-01-15")
    save_expenses(expenses)
    print("Total:", total_expenses(expenses))


if __name__ == "__main__":
    main()
