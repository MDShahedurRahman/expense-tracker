class Expense:

    def __init__(self, expense_id, title, amount, category, date):
        self.expense_id = expense_id
        self.title = title
        self.amount = amount
        self.category = category
        self.date = date

    def to_dict(self):
        return {
            "expense_id": self.expense_id,
            "title": self.title,
            "amount": self.amount,
            "category": self.category,
            "date": self.date
        }
