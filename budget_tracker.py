"""
Program Name: Personal Budget Tracker
Author: Jose Daniel Zambrano
Purpose: Display a menu that allows the user to keep track of income,
         expenses, transactions, and the remaining budget balance.
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

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        source = input("Where is the income coming from? ").strip()

        while True:
            try:
                amount = float(input("Enter the income amount: $"))

                if amount > 0:
                    break
                else:
                    print("Please enter an amount greater than $0.")

            except ValueError:
                print("Invalid amount. Please enter a number.")

        transactions.append({
            "type": "income",
            "source": source,
            "amount": amount
        })

        print("Income added successfully.")

    elif choice == "2":
        expense_category = input(
            "Enter the expense category (e.g., Food, Rent, Utilities): "
        ).strip().title()

        description = input(
            "Give a description of the expense: "
        ).strip()

        while True:
            try:
                amount = float(input("Enter the expense amount: $"))

                if amount > 0:
                    break
                else:
                    print("Please enter an amount greater than $0.")

            except ValueError:
                print("Invalid amount. Please enter a number.")

        transactions.append({
            "type": "expense",
            "category": expense_category,
            "description": description,
            "amount": amount
        })

        print("Expense added successfully.")

    elif choice == "3":
        if not transactions:
            print("No transactions found.")
        else:
            print("\nTransaction History")
            print("-------------------")

            for transaction in transactions:
                if transaction["type"] == "income":
                    print(
                        f"Income - Source: {transaction['source']}, "
                        f"Amount: ${transaction['amount']:.2f}"
                    )

                elif transaction["type"] == "expense":
                    print(
                        f"Expense - Category: {transaction['category']}, "
                        f"Description: {transaction['description']}, "
                        f"Amount: ${transaction['amount']:.2f}"
                    )

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

            remaining_balance = total_income - total_expenses

            print("\nBudget Summary")
            print("--------------")
            print(f"Total Income:      ${total_income:.2f}")
            print(f"Total Expenses:    ${total_expenses:.2f}")
            print(f"Remaining Balance: ${remaining_balance:.2f}")

    elif choice == "5":
        print("Thank you for using the Personal Budget Tracker!")
        break

    else:
        print("Invalid choice. Please enter a number from 1-5.")                  