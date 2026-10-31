"""
Program Name: Personal Budget Tracker
Author: Jose Daniel Zambrano
Purpose: Run the main menu and user interaction for the Personal Budget Tracker.
Starter Code: Refactored from Project 1.
Date: 10/30/2026
"""

from transaction import Income, Expense
from budget_manager import BudgetManager
from storage import save_transactions, load_transactions


def display_menu():
    """Display the main program menu."""
    print("""
Personal Budget Tracker
-----------------------
1. Add Income
2. Add Expense
3. View Transactions
4. View Budget Summary
5. Exit
""")


def get_amount(prompt):
    """Get and validate a positive monetary amount from the user."""
    while True:
        try:
            amount = float(input(prompt))

            if amount > 0:
                return amount

            print("Please enter an amount greater than $0.")

        except ValueError:
            print("Invalid amount. Please enter a number.")


def add_income(budget):
    """Create and add an income transaction."""
    source = input("Where is the income coming from? ").strip()
    amount = get_amount("Enter the income amount: $")

    income = Income(source, amount)
    budget.add_transaction(income)

    save_transactions(budget.transactions)

    print("Income added successfully.")


def add_expense(budget):
    """Create and add an expense transaction."""
    category = input(
        "Enter the expense category (e.g., Food, Rent, Utilities): "
    ).strip().title()

    description = input(
        "Give a description of the expense: "
    ).strip()

    amount = get_amount("Enter the expense amount: $")

    expense = Expense(category, description, amount)
    budget.add_transaction(expense)

    save_transactions(budget.transactions)

    print("Expense added successfully.")


def view_transactions(budget):
    """Display all saved income and expense transactions."""
    if not budget.transactions:
        print("No transactions found.")
        return

    print("\nTransaction History")
    print("-------------------")

    for transaction in budget.transactions:
        if isinstance(transaction, Income):
            print(
                f"Income - Source: {transaction.source}, "
                f"Amount: ${transaction.amount:.2f}"
            )

        elif isinstance(transaction, Expense):
            print(
                f"Expense - Category: {transaction.category}, "
                f"Description: {transaction.description}, "
                f"Amount: ${transaction.amount:.2f}"
            )


def view_budget_summary(budget):
    """Display total income, expenses, and remaining balance."""
    if not budget.transactions:
        print("No transactions found.")
        return

    print("\nBudget Summary")
    print("--------------")
    print(f"Total Income:      ${budget.get_total_income():.2f}")
    print(f"Total Expenses:    ${budget.get_total_expenses():.2f}")
    print(f"Remaining Balance: ${budget.get_remaining_balance():.2f}")


def main():
    """Run the Personal Budget Tracker application."""
    budget = BudgetManager()
    budget.transactions = load_transactions()

    while True:
        display_menu()

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_income(budget)

        elif choice == "2":
            add_expense(budget)

        elif choice == "3":
            view_transactions(budget)

        elif choice == "4":
            view_budget_summary(budget)

        elif choice == "5":
            print("Thank you for using the Personal Budget Tracker!")
            break

        else:
            print("Invalid choice. Please enter a number from 1-5.")


if __name__ == "__main__":
    main()