def total_expenses(expenses):
    return sum(e["amount"] for e in expenses)


def expenses_by_category(expenses):
    report = {}
    for e in expenses:
        report[e["category"]] = report.get(e["category"], 0) + e["amount"]
    return report
