users = []

while True:
    choice = input("1. Add user\n2. Exit\n")

    if choice == "1":
        name = input("Enter name: ")
        balance = float(input("Enter balance: "))

        user = {
            "name": name,
            "balance": balance,
            "transactions": []
        }

        users.append(user)

    elif choice == "2":
        break


name = input("Enter your name: ")

for user in users:
    if user["name"] == name:

        while True:
            choice = input(
                "1. Deposit\n"
                "2. Withdraw\n"
                "3. Transfer\n"
                "4. Transaction history\n"
                "5. Account information\n"
                "6. Exit\n"
            )

            if choice == "1":
                amount = float(input("Enter deposit amount: "))

                if amount > 0:
                    user["balance"] += amount
                    user["transactions"].append(f"+{amount} deposit")

                elif amount <= 0:
                    print("Invalid amount")

            elif choice == "2":
                amount = float(input("Enter withdraw amount: "))

                if amount > 0 and amount <= user["balance"]:
                    user["balance"] -= amount
                    user["transactions"].append(f"-{amount} withdraw")

                elif amount <= 0:
                    print("Invalid amount")

                elif amount > user["balance"]:
                    print("Insufficient balance")

            elif choice == "3":
                receiver_name = input("Enter receiver name: ")
                amount = float(input("Enter transfer amount: "))

                receiver_found = False

                for receiver in users:
                    if receiver["name"] == receiver_name:
                        receiver_found = True

                        if user["name"] != receiver["name"]:

                            if amount > 0 and amount <= user["balance"]:
                                user["balance"] -= amount
                                receiver["balance"] += amount

                                user["transactions"].append(
                                    f"-{amount} transfer to {receiver['name']}"
                                )

                                receiver["transactions"].append(
                                    f"+{amount} transfer from {user['name']}"
                                )

                            elif amount <= 0:
                                print("Invalid amount")

                            elif amount > user["balance"]:
                                print("Insufficient balance")

                        else:
                            print("Cannot transfer to yourself")

                if not receiver_found:
                    print("User not found")

            elif choice == "4":
                for transaction in user["transactions"]:
                    print(transaction)

            elif choice == "5":
                print("Name:", user["name"])
                print("Balance:", user["balance"])

            elif choice == "6":
                break