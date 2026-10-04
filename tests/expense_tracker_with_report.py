# ============================================================
# PROJECT 9 - EXPENSE TRACKER WITH REPORTS
# ============================================================

"""
Build a more advanced expense tracking application.

Each transaction should contain:

- transaction ID
- Date
- Amount
- Type
- Category
- Description

Menu:

1. Add transaction
2. Delete transaction
3. Show transaction
4. Search transaction
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

The user should be able to request transaction between two dates.

Example:

    From: 2026-09-01
    To:   2026-09-15

Only transaction inside that range should be displayed.

The program should also support searching by category
or description.

Persistence requirement:

All transaction data and previous records must survive
program restarts.
"""
import json
from datetime import datetime

transaction_FILE = "transaction.json"

try:
     with open(transaction_FILE, "r") as file:
        transaction = json.load(file)
except FileNotFoundError:
     transaction = []

def save_transaction():
     with open(transaction_FILE, "w") as file:
         json.dump(transaction, file, indent=4)

def get_next_id():
     if not transaction:
         return 1
     return max(transaction["id"] for transaction in transaction) + 1

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
     transaction.append(transaction)
     save_transaction()
     print("transaction added successfully!")

def delete_transaction():
     transaction_id = int(input("transaction ID: "))
     found = False

     for transaction in transaction:
         if transaction["id"] == transaction_id:
             transaction.remove(transaction)
             save_transaction
             print("transaction deleted successfully!")
             return
     print("transaction not found.")

def show_transaction():
     if not transaction:
         print("No transaction found.")
         return

     else:
         for transaction in transaction:
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
     for transaction in transaction:
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
             print("No transaction found.")

def monthly_report():
     month = input("Enter month (YYYY_MM): ")
     income = 0
     expence = 0
     for transaction in transaction:
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
     for transaction in transaction:
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
     for transaction in transaction:
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
         print("No transaction found.")
             

while True:
     print("""
     1. Add transaction
     2. Delete transaction
     3. Show transaction
     4. Search transaction
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
         show_transaction()

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