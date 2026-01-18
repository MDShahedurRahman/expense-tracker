from file_handler import load_expenses, save_expenses
from expense_manager import add_expense, delete_expense
from report import total_expenses


def main():
    expenses = load_expenses()


if __name__ == "__main__":
    main()
