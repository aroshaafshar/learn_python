# ============================================================
# PROJECT 5 - SIMPLE BANKING SYSTEM
# ============================================================

"""
Build a simple banking system.

Menu:

1. Create Account
2. Deposit
3. Withdraw
4. Transfer Money
5. Show Balance
6. Show Transaction History
7. Show All Accounts
8. Exit

Each account should contain at least:

- Account ID
- Owner name
- Balance
- Transaction history

Requirements:

- Create a new account.
- Prevent duplicate account IDs.
- Deposit money.
- Withdraw money.
- Transfer money between two accounts.
- Display account balance.
- Display transaction history.
- Display all accounts.

Rules:

- Balance must never become negative.
- A withdrawal cannot be larger than the current balance.
- A transfer cannot be completed if the sender does not have
  enough money.
- Both sides of a transfer must be recorded.
- Invalid account IDs must be handled properly.

Example:

    Ali -> Reza
    Amount: 500,000

After the transfer:

    Ali balance   -= 500,000
    Reza balance  += 500,000

Transaction history should contain enough information to understand
what happened.

Persistence requirement:

All accounts, balances and transaction histories must survive
program restarts.
"""
