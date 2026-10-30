"""
Program Name: Personal Budget Tracker
Author: Jose Daniel Zambrano
Purpose: Save and load budget transactions using JSON.
Starter Code: None.
Date: 10/30/2026
"""

import json

from transaction import Income, Expense


DATA_FILE = "transactions.json"


def save_transactions(transactions):
    """Save transaction objects to a JSON file."""
    data = []

    for transaction in transactions:
        if isinstance(transaction, Income):
            data.append({
                "type": "income",
                "source": transaction.source,
                "amount": transaction.amount
            })

        elif isinstance(transaction, Expense):
            data.append({
                "type": "expense",
                "category": transaction.category,
                "description": transaction.description,
                "amount": transaction.amount
            })

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def load_transactions():
    """Load transaction objects from a JSON file."""
    transactions = []

    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        return transactions

    except json.JSONDecodeError:
        print("Transaction data could not be read.")
        return transactions

    for item in data:
        if item["type"] == "income":
            transactions.append(
                Income(item["source"], item["amount"])
            )

        elif item["type"] == "expense":
            transactions.append(
                Expense(
                    item["category"],
                    item["description"],
                    item["amount"]
                )
            )

    return transactions