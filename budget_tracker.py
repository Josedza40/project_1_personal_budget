"""
Program Name: Personal Budget Tracker
Author: Jose Daniel Zambrano
Purpose: Display a menu that allows the user to keep track of income, expenses, and transactions.
Starter Code: None.
Date: 09/27/2026

"""
menu = """
Personal Budget Tracker
-----------------------
1. Add Income
2. Add Expense
3. View Transactions
4. View Spending by Category
5. View Budget Summary
6. Exit
"""

transactions = []

while True:
    print(menu)

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        source = input("Where is the income coming from? ")
        amount = float(input("Enter the income amount: "))
        transactions.append({"type": "income", "source": source, "amount": amount})
        print("Income added successfully.")
    elif choice == "2":
        expense_category = input("Enter the expense category (e.g., Food, Rent, Utilities): ").strip()
        description = input("Give a description of the expense: ").strip()
        amount = float(input("Enter the expense amount: "))
        transactions.append({"type": "expense", "category": expense_category, "description": description, "amount": amount})
        print("Expense added successfully.")
    elif choice == "3":
        print("View Transaction history")
    elif choice == "4":
        print("View spending by category")
    elif choice == "5":
        print("Budget summary") 
    elif choice == "6":
        print("Thank you for using the Personal Budget Tracker")
        break
    else:
        print("Invalid choice. Please try again")                   