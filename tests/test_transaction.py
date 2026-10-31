"""
Program Name: Personal Budget Tracker
Author: Jose Daniel Zambrano
Purpose: Test the Income and Expense transaction classes.
Starter Code: None.
Date: 10/31/2026
"""

from transaction import Income, Expense


def test_income_creation():
    """Test that an Income object stores its source and amount."""
    income = Income("Honda", 1000)

    assert income.source == "Honda"
    assert income.amount == 1000


def test_expense_creation():
    """Test that an Expense object stores its transaction information."""
    expense = Expense("Food", "Groceries", 200)

    assert expense.category == "Food"
    assert expense.description == "Groceries"
    assert expense.amount == 200