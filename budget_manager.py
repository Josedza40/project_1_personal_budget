"""
Program Name: Personal Budget Tracker
Author: Jose Daniel Zambrano
Purpose: Manage transactions and calculate budget totals.
Starter Code: None.
Date: 10/30/2026
"""

from transaction import Income, Expense

class BudgetManager:
    """Manage income and expense transactions."""

    def __init__(self):
        """Initialize the budget manager with an empty transaction list."""
        self.transactions = []

    def add_transaction(self, transaction):
        """Add a transaction to the transaction list."""
        self.transactions.append(transaction)

    def get_total_income(self):
        """Return the total amount of all income transactions."""
        total = 0

        for transaction in self.transactions:
            if isinstance(transaction, Income):
                total += transaction.amount

        return total

    def get_total_expenses(self):
        """Return the total amount of all expense transactions."""
        total = 0

        for transaction in self.transactions:
            if isinstance(transaction, Expense):
                total += transaction.amount

        return total

    def get_remaining_balance(self):
        """Return income minus expenses."""
        return self.get_total_income() - self.get_total_expenses()