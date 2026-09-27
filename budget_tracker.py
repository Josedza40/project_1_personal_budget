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

while True:
    print(menu)

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        print("Please add income")
    elif choice == "2":
        print("Please add expense")
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