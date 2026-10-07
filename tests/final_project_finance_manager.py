# ============================================================
# FINAL PROJECT - PERSONAL FINANCE MANAGER
# ============================================================

"""
Build a complete personal finance management application.

This project combines the concepts from the previous exercises.

The application should manage income, expenses, transfers,
transaction and financial reports.

The system should support:

1. Add Income
2. Add Expense
3. Transfer Money
4. Show Balance
5. Show transaction
6. Search transaction
7. Filter By Category
8. Monthly Report
9. Category Report
10. Date Range Report
11. Delete transaction
12. Exit

Each transaction should contain enough information to identify:

- transaction ID
- Amount
- Type
- Category
- Description
- Date

Example:

    Income:
        Salary
        50,000,000

    Expense:
        Food
        500,000

    Transfer:
        Savings
        5,000,000

The application must calculate:

- Total income
- Total expenses
- Current balance
- Total spending by category
- Monthly income
- Monthly expenses
- Monthly balance

Example:

    ==============================
         PERSONAL FINANCE
    ==============================

    Balance: 18,500,000

    Income:   30,000,000
    Expense:  11,500,000

    ------------------------------

    1. Add Income
    2. Add Expense
    3. Transfer Money
    4. transaction
    5. Reports
    6. Search
    7. Exit

Important requirements:

- The application must preserve its state between runs.
- Previously created transaction must be loaded automatically.
- New transaction must be saved.
- Deleted transaction must remain deleted after restarting.
- Calculated values must remain consistent with stored data.
- Invalid input must not crash the application.
- The application must be divided into logical functions.
- Avoid creating one huge function containing the entire program.

Do not hard-code the current balance.

The balance should be calculated from the stored financial data.

Do not manually write reports into the file.

Reports should be generated from the stored transaction.

The choice of data structures and file format is completely up to you.
"""
import json
import os
from copy import deepcopy

TRANSACTION_FILE = "transactions.json"
CONFIG_FILE = "config.json"
APP_DATA_FILE = "app_data.json"
BACKUP_FILE = "backup.json"

def save_transactions():
     with open(TRANSACTION_FILE, "w") as file:
         json.dump(transactions, file, indent=4)

def save_config():
     with open(CONFIG_FILE, "w") as file:
         json.dump(config, file, indent=4)

def save_app_data():
     with open(APP_DATA_FILE, "w") as file:
         json.dump(app_data, file, indent=4)

def create_backup():
     backup = {
         "transactions": transactions,
         "config": config,
         "app_data": app_data
     }

     with open(BACKUP_FILE, "w") as file:
         json.dump(backup, file, indent=4)

     print("Backup created successfully.")

def restore_backup():
     if not os.path.exists(BACKUP_FILE):
         print("No backup found.")
         return

     try:
         with open(BACKUP_FILE, "r") as file:
             backup = json.load(file)

         if not isinstance(backup, dict):
             print("Invalid backup.")
             return

         if "transactions" not in backup:
             print("Invalid backup.")
             return

         if "config" not in backup:
             print("Invalid backup.")
             return

         if "app_data" not in backup:
             print("Invalid backup.")
             return

         if not isinstance(backup["transactions"], list):
             print("Invalid backup.")
             return

         if not isinstance(backup["config"], dict):
             print("Invalid backup")
             return

         if not isinstance(backup["app_data"], dict):
             print("Invalid backup")
             return

         transactions.clear()
         transactions.extend(deepcopy(backup["transactions"]))

         config.clear()
         config.update(deepcopy(backup["config"]))

         app_data.clear()
         app_data.update(deepcopy(backup["app_data"]))

         save_transactions()
         save_config()
         save_app_data()

         print("Backup restored successfully.")
     except (json.JSONDecodeError, OSError):
         print("Invalid or broken backup.")

try:
     with open(TRANSACTION_FILE, "r") as file:
         transactions = json.load(file)
except FileNotFoundError:
     transactions = []

try:
     with open(CONFIG_FILE, "r") as file:
         config = json.load(file)
except FileNotFoundError:
     config = {}
     save_config()

try:
     with open(APP_DATA_FILE, "r") as file:
         app_data = json.load(file)
except FileNotFoundError:
     app_data = {}
     save_app_data()

history = []

def get_next_id():
     if not transactions:
         return 1
     return max(transaction["id"] for transaction in transactions) + 1

def add_income():
     history.append(deepcopy(transactions))

     amount = int(input("Amount: "))
     category = input("Category: ")
     description = input("Description: ")
     date = input("Date (YYYY-MM-DD): ")

     transaction = {
         "id": get_next_id(),
         "amount": amount,
         "type": "income",
         "category": category,
         "description": description,
         "date": date
     }
     transactions.append(transaction)
     save_transactions()
     print("Income added successfully.")

def add_expence():
     history.append(deepcopy(transactions))

     amount = int(input("Amount: "))
     category = input("Category: ")
     description = input("Description: ")
     date = input("Date (YYYY-MM-DD): ")

     transaction = {
         "id": get_next_id(),
         "amount": amount,
         "type": "expence",
         "category": category,
         "description": description,
         "date": date 
     }
     transactions.append(transaction)
     save_transactions()
     print("Expence added successfully.")

def transfer_money():
     history.append(deepcopy(transactions))

     amount = int(input("Amount: "))
     category = input("Category: ")
     description = input("Description: ")
     date = input("Date (YYYY-MM-DD): ")
   
     transaction = {
         "id": get_next_id(),
         "amount": amount,
         "type": "transfer",
         "category": category,
         "description": description,
         "date": date 
     }
     transactions.append(transaction)
     save_transactions()
     print("Transfer completed successfully.")

def show_balance():
     balance = 0
     for transaction in transactions:
         if transaction["type"] == "income":
             balance += transaction["amount"]

         elif transaction["type"] == "expence":
             balance -= transaction["amount"]

         elif transaction["type"] == "transfer":
            balance -= transaction["amount"]

     print(f"balance: {balance:,}")

def show_transaction():
     if not transactions:
         print("No transaction found.")
         return

     for transaction in transactions:
         print("---------------------")
         print(f"ID: {transaction['id']}") 
         print(f"Amount: {transaction['amount']}")
         print(f"Type: {transaction['type']}")
         print(f"Category: {transaction['category']}")
         print(f"Description: {transaction['description']}")
         print(f"Date: {transaction['date']}")

def search_transaction():
     search = input("Search: ").lower()
     found = False

     for transaction in transactions:
         if (search in transaction["category"].lower()
             or search in transaction["description"].lower()
             or search in transaction["type"].lower()):
             print("---------------------")
             print(f"ID: {transaction['id']}") 
             print(f"Amount: {transaction['amount']}")
             print(f"Type: {transaction['type']}")
             print(f"Category: {transaction['category']}")
             print(f"Description: {transaction['description']}")
             print(f"Date: {transaction['date']}")

             found = True
     if not found:
         print("No transaction found.")

def filter_by_category():
     category = input("Category: ").lower()

     found = False
     for transaction in transactions:
         if transaction["category"].lower() == category:
             print("---------------------")
             print(f"ID: {transaction['id']}") 
             print(f"Amount: {transaction['amount']}")
             print(f"Type: {transaction['type']}")
             print(f"Category: {transaction['category']}")
             print(f"Description: {transaction['description']}")
             print(f"Date: {transaction['date']}")

             found = True
     if not found:
         print("No transaction found in this category.")

def monthly_report():
     month = input("Enter month (YYYY-MM): ")
     total_income = 0
     total_expence = 0
     for transaction in transactions:
         if transaction["date"].startswith(month):
             if transaction["type"] == "income":
                 total_income += transaction["amount"]

             elif transaction["type"] == "expence":
                 total_expence += transaction["amount"]

     balance = total_income - total_expence
     print("-------------------------")
     print(f"Monthly report: {month}")
     print(f"Income: {total_income}")
     print(f"Expence: {total_expence}")
     print(f"Balance: {balance}")

def category_report():
     category_totals = {}
     for transaction in transactions:
         if transaction["type"] == "expence":
             category = transaction["category"]

             if category not in category_totals:
                 category_totals[category] = 0
             category_totals[category] += transaction["amount"]

     if not category_totals:
         print("No expences found.")
         return

     print("----------------------")
     print("Category report")
     for category, total in category_totals.items():
         print(f"{category}: {total:,}")

def date_range_report():
     start_date = input("start date (YYYY-MM-DD):")
     end_date = input("end date (YYYY-MM-DD): ")
     total_income = 0
     total_expences = 0

     for transaction in transactions:
         date = transaction["date"]
         if start_date <= date <= end_date:
             if transaction["type"] == "income":
                 total_income += transaction["amount"]
             elif transaction["type"] == "expense":
                 total_expences += transaction["amount"]

     balance = total_income - total_expences 
     print("--------------------")
     print("Date range report")
     print(f"From: {start_date}")
     print(f"To: {end_date}")
     print(f"Income: {total_income:,}")
     print(f"Expence: {total_expences:,}")
     print(f"Balance: {balance:,}")

def undo():
     if history:
         previous_satate = history.pop()

         transactions.clear()
         transactions.extend(previous_satate)

         save_transactions
         print("Last operation undone.")
     else:
         print("Nothing to undo.")

def delete_transaction():
     transaction_id = int(input("transaction ID: "))

     for transaction in transactions:
         if transaction["id"] == transaction_id:
             history.append(deepcopy(transactions))

             transactions.remove(transaction)
             save_transactions()
             print("transaction deleted successfully.")
             return

     print("transaction not found.")

while True:
     print("""
     1. Add income
     2. Add expence
     3. Transfer money
     4. Show balance
     5. Show transaction
     6. Search transaction
     7. Filter by category
     8. Monthly reports
     9. Category report
     10. Date range report
     11. Delete transaction
     12. Undo
     13. Create backup
     14. Restore backup
     15. Exit
     """)
     
     choice = input("chose: ")

     if choice == "1":
         add_income()

     elif choice == "2":
         add_expence()

     elif choice == "3":
         transfer_money()

     elif choice == "4":
         show_balance()

     elif choice == "5":
         show_transaction()

     elif choice == "6":
         search_transaction()

     elif choice == "7":
         filter_by_category()

     elif choice == "8":
         monthly_report()

     elif choice == "9":
         category_report()

     elif choice == "10":
         date_range_report()

     elif choice == "11":
         delete_transaction()

     elif choice == "12":
         undo()

     elif choice == "13":
         create_backup()

     elif choice == "14":
         restore_backup()

     elif choice == "15":
         print("Goodbye.")
         break

     else:
         print("Invalid choice")