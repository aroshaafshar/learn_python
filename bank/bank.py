transactions=[
    {"type": "deposit","amount":500},
    {"type": "withdraw","amount":100},
    {"type": "deposit", "amount":300},
    {"type": "withdraw", "amount":50},
    {"type": "withdraw", "amount":200}
]
balance = 0
total_deposits = 0
total_withdraws = 0
largest_withdrawal = 0
for i in transactions:
    if i ["type"] == "deposit":
        total_deposits += i ["amount"]
    elif i ["type"] == "withdraw":
        total_withdraws += i ["amount"]
    if i ["amount"] > largest_withdrawal:
        largest_withdrawal = i ["amount"]
    transactions_count = len(transactions)
    balance = total_deposits - total_withdraws
    print(f"total deposits: {total_deposits}")
    print(f"total withdrawas: {total_withdraws}")
    print(f"transaction count: {transactions_count}")
    print(f"largest withdrawal: {largest_withdrawal}")
    print(f"final balance: {balance}")

