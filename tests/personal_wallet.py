# ============================================================
# PROJECT 2 - PERSONAL WALLET
# ============================================================

"""
Build a personal wallet application.

The application should provide functionality similar to:

1. Add Income
2. Add Expense
3. Show Balance
4. Show Transactions
5. Search Transactions
6. Show Statistics
7. Delete Transaction
8. Exit

Each transaction should contain at least:

- A unique ID
- Amount
- Type (income / expense)
- Category
- Description
- Date

Example transactions:

Income:
    Salary
    50,000,000

Expense:
    Food
    350,000
    Lunch

The application must be able to:

- Add income.
- Add expenses.
- Calculate the current balance.
- Display all transactions.
- Search transactions.
- Filter transactions by category.
- Delete a transaction.
- Calculate total income.
- Calculate total expenses.

Example report:

    Total Income:   50,000,000
    Total Expenses: 12,500,000
    Balance:         37,500,000

Category statistics should also be possible.

Example:

    Food:       3,000,000
    Transport:  1,500,000
    Shopping:   4,000,000

The user should also be able to search for transactions
based on an amount, category or part of the description.

Persistence requirement:

All transactions must survive program restarts.

When the program starts, previously stored transactions must
be loaded automatically.

The file format and internal data structures are up to you.
"""
