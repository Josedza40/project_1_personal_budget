"""
Program Name: Personal Budget Tracker
Author: Jose Daniel Zambrano
Purpose: Define transaction classes used to represent income and expense data.
Starter Code: None.
Date: 10/30/2026
"""

class Transaction:
    """Represents a general financial transaction"""

    def __init__(self, amount):
        """Initialize a transaction with an amount"""

        self.amount = amount


class Income(Transaction):
    """Represents an income transaction"""

    def __init__(self, source, amount):
        """Initialize an income transaction"""
        super().__init__(amount)
        self.source = source

class Expense(Transaction):
    """Represent an expense transaction."""

    def __init__(self, category, description, amount):
        """Initialize an expense transaction."""
        super().__init__(amount)
        self.category = category
        self.description = description                
