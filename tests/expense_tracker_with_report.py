# ============================================================
# PROJECT 9 - EXPENSE TRACKER WITH REPORTS
# ============================================================

"""
Build a more advanced expense tracking application.

Each transaction should contain:

- Transaction ID
- Date
- Amount
- Type
- Category
- Description

Menu:

1. Add Transaction
2. Delete Transaction
3. Show Transactions
4. Search Transactions
5. Monthly Report
6. Category Report
7. Date Range Report
8. Exit

Example:

    Date: 2026-09-23
    Type: Expense
    Amount: 450,000
    Category: Food
    Description: Dinner

Monthly report example:

    September 2026

    Income:   25,000,000
    Expense:  13,500,000
    Balance:  11,500,000

Category report:

    Food:       4,000,000
    Transport:  1,500,000
    Shopping:   3,000,000
    Bills:      5,000,000

The user should be able to request transactions between two dates.

Example:

    From: 2026-09-01
    To:   2026-09-15

Only transactions inside that range should be displayed.

The program should also support searching by category
or description.

Persistence requirement:

All transaction data and previous records must survive
program restarts.
"""
import json
from datetime import datetime

TRANSACTION_FILE = "transactions.json"

try:
     with open(TRANSACTION_FILE, "r") as file:
        transactions = json.load(file)
except FileNotFoundError:
     transactions = []

def save_transactions():
     with open(TRANSACTION_FILE, "w") as file:
         json.dump(transactions, file, indent=4)

def get_next_id():
     if not transactions:
         return 1
     return max(transaction["id"] for transaction in transactions) + 1

def add_transaction():
     while True:
         date = input("Date (YYYY-MM-DD): ")
         try:
             datetime.strptime(date, "%Y-%m-%d")
             break
         except ValueError:
             print("Invalid date.")

     transaction_type = input("Type (Income/Expence): ")
     while transaction_type.lower() not in ["income", "expence"]:
         print("Please enter income or expence.")
         transaction_type = input("Type (Income/Expence): ")

     while True:
         try:
             amount = int(input("Amount: "))
             if amount > 0:
                 break
             print("Amount must be greater than 0.")
         except ValueError:
             print("Please enter a valid number.")

     category = input("Category: ")
     description = input("Description: ")

     transaction = {
         "id": get_next_id(),
         "date": date,
         "type": transaction_type,
         "amount": amount,
         "category": category,
         "description": description
     }
     transactions.append(transaction)
     save_transactions()
     print("Transaction added successfully!")

def delete_transaction():
     transaction_id = int(input("Transaction ID: "))
     found = False

     for transaction in transactions:
         if transaction["id"] == transaction_id:
             transactions.remove(transaction)
             save_transactions
             print("Transaction deleted successfully!")
             return
     print("Transaction not found.")

def show_transactions():
     if not transactions:
         print("No transaction found.")
         return

     else:
         for transaction in transactions:
             print("--------------------")
             print("ID:", transaction["id"])
             print("Date:", transaction["date"])
             print("Type:", transaction["type"])
             print("Amount:", transaction["amount"])
             print("Category:", transaction["category"])
             print("Description:", transaction["description"])

def search_transactionns():
     srarch = input("Search category or description: ").lower()
     found = False
     for transaction in transactions:
         if search in transaction["category"].lower() or search in transaction["description"]:
             print("--------------------")
             print("ID:", transaction["id"])
             print("Date:", transaction["date"])
             print("Type:", transaction["type"])
             print("Amount:", transaction["amount"])
             print("Category:", transaction["category"])
             print("Description:", transaction["description"])

             found = True
         if not found:
             print("No transactions found.")

def monthly_report():
     month = input("Enter month (YYYY_MM): ")
     income = 0
     expence = 0
     for transaction in transactions:
         if transaction["date"].startswith(month):
             if transaction["type"].lower() == "income":
                 income += transaction["amount"]
             elif transaction["type"].lower() == "expence":
                 expence += transaction["amount"]
     balance = income - expence
     print("------------------")
     print("Month:", month)
     print("Income:", income)
     print("Expence:", expence)
     print("Balance:", balance)

def category_report():
     categories = {}
     for transaction in transactions:
         if transaction["type"].lower() == "expence":
             category = transaction["category"]

             if category in categories:
                 categories[category] += transaction["amount"]
             else:
                 categories[category] = transaction["amount"]
     for category, amount in categories.items():
         print(category, ":", amount)

def date_range_report():
     from_date = input("From: ")
     to_date = input("To: ")
     found = False
     for transaction in transactions:
         if from_date <= transaction["date"]:
             print("--------------------")
             print("ID:", transaction["id"])
             print("Date:", transaction["date"])
             print("Type:", transaction["type"])
             print("Amount:", transaction["amount"])
             print("Category:", transaction["category"])
             print("Description:", transaction["description"])
             
             found = True
     if not found:
         print("No transactions found.")
             

while True:
     print("""
     1. Add transaction
     2. Delete transaction
     3. Show transactions
     4. Search transactions
     5. Monthly report
     6. Category report
     7. Date range report
     8. Exit
     """)
     choice = input("Choose: ")

     if choice == "1":
         add_transaction()

     elif choice == "2":
         delete_transaction()

     elif choice == "3":
         show_transactions()

     elif choice == "4":
         search_transactionns()

     elif choice == "5":
         monthly_report()

     elif choice == "6": 
         category_report()

     elif choice == "7":
         date_range_report()
     
     elif choice == "8":
         print("Goodbye.")
         break

     else:
         print("Invalid choice.")