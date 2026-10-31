"""
Program Name: Personal Budget Tracker
Author: Jose Daniel Zambrano
Purpose: Test the BudgetManager transaction and calculation methods.
Starter Code: None.
Date: 10/31/2026
"""

from transaction import Income, Expense
from budget_manager import BudgetManager


def test_total_income():
    """Test the calculation of total income."""
    budget = BudgetManager()

    budget.add_transaction(Income("Honda", 1000))
    budget.add_transaction(Income("Other", 500))

    assert budget.get_total_income() == 1500


def test_total_expenses():
    """Test the calculation of total expenses."""
    budget = BudgetManager()

    budget.add_transaction(Expense("Food", "Groceries", 200))
    budget.add_transaction(Expense("Transportation", "Gas", 50))

    assert budget.get_total_expenses() == 250


def test_remaining_balance():
    """Test the calculation of the remaining budget balance."""
    budget = BudgetManager()

    budget.add_transaction(Income("Honda", 1000))
    budget.add_transaction(Expense("Food", "Groceries", 200))
    budget.add_transaction(Expense("Transportation", "Gas", 50))

    assert budget.get_remaining_balance() == 750