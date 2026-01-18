# Expense Tracker (Python CLI)

A lightweight command-line expense tracker built with Python.
The project demonstrates modular design, clean separation of concerns, and disciplined Git commit practices.

## Overview

The Expense Tracker allows users to record daily expenses, store them persistently, and generate summary reports.
The codebase is intentionally split into small, focused modules to improve readability, maintainability, and testability.

## Features

- Add, update, and delete expenses
- Validate expense amount and date format
- Persist data using JSON storage
- Generate reports:
  - Total expenses
  - Expenses by category
  - Expenses by date
- Centralized configuration for file paths and date formats

## Project Structure

```
expense-tracker/
├── main.py              # Application entry point
├── config.py            # Configuration constants
├── expense.py           # Expense model
├── expense_manager.py   # Business logic for expenses
├── file_handler.py      # File I/O operations
├── report.py            # Reporting utilities
├── utils.py             # Validation and helper functions
└── expenses.json        # Stored expense data
```

## Getting Started

### Prerequisites
- Python 3.8 or higher

### Run the Application

```bash
python main.py
```

## Design Notes

- Each module has a single responsibility
- Functions are small and easy to test
- Git commits were intentionally kept granular (one feature or method per commit)

## Future Improvements

- Interactive CLI menu
- Unit tests with pytest
- CSV export support
- REST API version using Flask or FastAPI

## Technologies Used

- Python 3
- JSON
- Git & GitHub

## Author

Md Shahedur Rahman
