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
4. View Budget Summary
5. Exit
"""

transactions = []

while True:
    print(menu)

    choice = input("Enter your choice (1-5): ")

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
        if not transactions:
            print("No transactions found.")
        else:
            for transaction in transactions:
                if transaction["type"] == "income":
                    print(f"Source: {transaction['source']}, Amount: ${transaction['amount']:.2f}")
                elif transaction["type"] == "expense":
                    print(f"Category: {transaction['category']}, Description: {transaction['description']}, Amount: ${transaction['amount']:.2f}")
    elif choice == "4":
        total_income = 0
        total_expenses = 0    
        if not transactions:
            print("No transactions found.")
        else:
            for transaction in transactions:
                if transaction["type"] == "income":
                    total_income += transaction["amount"]
                elif transaction["type"] == "expense":
                    total_expenses += transaction["amount"]
            print("Budget summary")
            print(f"Total Income: ${total_income:.2f}")
            print(f"Total Expenses: ${total_expenses:.2f}")
            print(f"Remaining Balance: ${total_income - total_expenses:.2f}")


    elif choice == "5":
        print("Thank you for using the Personal Budget Tracker")
        break
    else:
        print("Invalid choice. Please try again")                   