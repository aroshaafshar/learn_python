import json
from datetime import datetime
FILENAME = "personal_wallet.json"
try:
    with open(FILENAME, "r") as file:
        transactions = json.load(file)
except FileNotFoundError:
    transactions = []
def save_transactions():
   with open(FILENAME, "w") as file:
      json.dump(transactions, file, indent=4)
def get_next_id():
   if not transactions:
      return 1
   return max(transaction["id"] for transaction in transactions) + 1

while True:
     print("1.add income\n2. add expense\n3. show balance\n4. show transaction\n5. search transaction\n6. show statistics\n7. delete transaction\n8. exit ")
     choice = input("enter your choice: ")
     if choice == "1":
      amount = int(input("enter amount: "))
      category = input("enter category: ")
      description = input("enter description: ")
      date = datetime.now().strftime("%Y-%m-%d")
      transaction = {
         "id": get_next_id(),
         "amount": amount,
         "type": "income",
         "category": category,
         "descrioption": description,
         "date": date
      }
      transactions.append(transaction)
      save_transactions()
      print("income added successfully.")
     elif choice == "2":
        amount = int(input("enter amount: "))
        category = input("enter category: ")
        description = input("enter description: ")
        date = datetime.now().strftime("%Y-%m-%d")
        transaction = {
           "id": get_next_id(),
           "amount": amount,
           "type": "expense",
           "category": category,
           "description": description,
           "date": date
        }
        transactions.append(transaction)
        save_transactions()
        print("expense added successgully.")
     elif choice == "3":
         total_income = sum(
           transaction["amount"]
           for transaction in transactions
           if transaction["type"] == "income"
        )
         total_expenses = sum(
            transaction["amount"]
            for transaction in transactions
            if transaction["type"] == "expense"
        )
         balance = total_income - total_expenses
         print(f"total_income: {total_income:,}")
         print(f"total_expenses: {total_expenses:,}")
         print(f"balance: {balance:,}")

     elif choice == "4":
        if not transactions:
           print("no transaction found.")
        else:
           for transaction in transactions:
              print("--------------------")
              print(f"id: {transaction["id"]}")
              print(f"amount: {transaction["amount"]}")
              print(f"type: {transaction["type"]}")
              print(f"category: {transaction["category"]}")
              print(f"description: {transaction['description']}")
              print(f"date: {transaction["date"]}")

     elif choice == "5":
        search = input(
           "search by amount, category or description:"
        ).lower()
        found = False
        for transaction in transactions:
           if(
              search in str(transaction["amount"])
              or search in transaction["category"].lower()
              or search in transaction["description"].lower()
           ):
              print("----------------")
              print(f"id: {transaction["id"]}")
              print(f"amount: {transaction["amount"]}")
              print(f"type: {transaction["type"]}")
              print(f"category: {transaction["category"]}")
              print(f"description: {transaction["description"]}")
              print(f"date: {transaction["date"]}")
              found = True
        if not found:
           print("no matching transactions found.")

     elif choice == "6":
        total_income = sum(
           transaction["amount"]
           for transaction in transactions
           if transaction['type'] == "income"
        )
        total_expenses = sum(
           transaction["amount"]
           for transaction in transactions
           if transaction['type'] == "expense"
        )
        print(f"total income: {total_income:,}")
        print(f"total expenses: {total_expenses:,}")
        print(f"balance: {total_income - total_expenses:,}")

        print("\ncategory statistics:")
        categories = {}
        for transaction in transactions:
           category = transaction["category"]
           if category not in categories:
              categories[category] = 0
           if transaction["type"] == "expense":
              categories[category] += transaction["amount"]
        for category, amount in categories.items():
           print(f"{category}: {amount:,}")  

     elif choice == "7":
        transaction_id = int(input("enter transaction id: "))
        found = False
        for transaction in transactions:
           if transaction["id"] == transaction_id:
              transactions.remove(transaction)
              save_transactions
              print("transaction deleted successfully.")

              found = True
              break
           if not found:
              print("transaction not foundd.")
     elif choice == "8":
        print("Goodbye!")
        break  
     else:
        print("invalid choice. ")