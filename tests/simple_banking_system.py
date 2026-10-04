import json

FILE_NAME = "bank.json"


class Account:
    def __init__(self, account_id, owner, balance=0, transaction=None):
        self.account_id = account_id
        self.owner = owner
        self.balance = balance
        self.transaction = transaction if transaction is not None else []

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
            return False

        self.balance += amount

        self.transaction.append({
            "type": "deposit",
            "amount": amount,
            "balance": self.balance
        })

        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
            return False

        if amount > self.balance:
            print("Insufficient balance.")
            return False

        self.balance -= amount

        self.transaction.append({
            "type": "withdraw",
            "amount": amount,
            "balance": self.balance
        })

        return True


class Bank:
    def __init__(self):
        self.accounts = []
        self.load_accounts()

    def load_accounts(self):
        try:
            with open(FILE_NAME, "r") as file:
                data = json.load(file)

            for account in data:
                new_account = Account(
                    account["account_id"],
                    account["owner"],
                    account["balance"],
                    account["transaction"]
                )

                self.accounts.append(new_account)

        except FileNotFoundError:
            self.accounts = []

        except json.JSONDecodeError:
            print("Bank file is invalid.")
            self.accounts = []

    def save_accounts(self):
        data = []

        for account in self.accounts:
            data.append({
                "account_id": account.account_id,
                "owner": account.owner,
                "balance": account.balance,
                "transaction": account.transaction
            })

        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

    def find_account(self, account_id):
        for account in self.accounts:
            if account.account_id == account_id:
                return account

        return None

    def create_account(self):
        account_id = input("Enter account ID: ")

        if self.find_account(account_id) is not None:
            print("Account ID already exists.")
            return

        owner = input("Enter owner name: ")

        account = Account(account_id, owner)

        self.accounts.append(account)
        self.save_accounts()

        print("Account created successfully.")

    def deposit(self):
        account_id = input("Enter account ID: ")

        account = self.find_account(account_id)

        if account is None:
            print("Invalid account ID.")
            return

        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Invalid amount.")
            return

        if account.deposit(amount):
            self.save_accounts()
            print("Deposit successful.")

    def withdraw(self):
        account_id = input("Enter account ID: ")

        account = self.find_account(account_id)

        if account is None:
            print("Invalid account ID.")
            return

        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Invalid amount.")
            return

        if account.withdraw(amount):
            self.save_accounts()
            print("Withdrawal successful.")

    def transfer(self):
        sender_id = input("Enter sender account ID: ")
        receiver_id = input("Enter receiver account ID: ")

        sender = self.find_account(sender_id)
        receiver = self.find_account(receiver_id)

        if sender is None or receiver is None:
            print("Invalid account ID.")
            return

        if sender_id == receiver_id:
            print("Sender and receiver cannot be the same account.")
            return

        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Invalid amount.")
            return

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        if amount > sender.balance:
            print("Insufficient balance.")
            return

        sender.balance -= amount
        receiver.balance += amount

        sender.transaction.append({
            "type": "transfer_sent",
            "to": receiver.account_id,
            "amount": amount,
            "balance": sender.balance
        })

        receiver.transaction.append({
            "type": "transfer_received",
            "from": sender.account_id,
            "amount": amount,
            "balance": receiver.balance
        })

        self.save_accounts()

        print("Transfer successful.")

    def show_balance(self):
        account_id = input("Enter account ID: ")

        account = self.find_account(account_id)

        if account is None:
            print("Invalid account ID.")
            return

        print(f"Owner: {account.owner}")
        print(f"Balance: {account.balance}")

    def show_transaction_history(self):
        account_id = input("Enter account ID: ")

        account = self.find_account(account_id)

        if account is None:
            print("Invalid account ID.")
            return

        print(f"\ntransaction history for {account.owner}:")

        if not account.transaction:
            print("No transaction.")
            return

        for transaction in account.transaction:
            print(transaction)

    def show_all_accounts(self):
        if not self.accounts:
            print("No accounts found.")
            return

        for account in self.accounts:
            print(
                f"ID: {account.account_id} | "
                f"Owner: {account.owner} | "
                f"Balance: {account.balance}"
            )


def main():
    bank = Bank()

    while True:
        print("\n===== BANKING SYSTEM =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer Money")
        print("5. Show Balance")
        print("6. Show transaction History")
        print("7. Show All Accounts")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            bank.create_account()

        elif choice == "2":
            bank.deposit()

        elif choice == "3":
            bank.withdraw()

        elif choice == "4":
            bank.transfer()

        elif choice == "5":
            bank.show_balance()

        elif choice == "6":
            bank.show_transaction_history()

        elif choice == "7":
            bank.show_all_accounts()

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
