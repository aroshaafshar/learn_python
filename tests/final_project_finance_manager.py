# ============================================================
# FINAL PROJECT - PERSONAL FINANCE MANAGER
# ============================================================

"""
Build a complete personal finance management application.

This project combines the concepts from the previous exercises.

The application should manage income, expenses, transfers,
transactions and financial reports.

The system should support:

1. Add Income
2. Add Expense
3. Transfer Money
4. Show Balance
5. Show Transactions
6. Search Transactions
7. Filter By Category
8. Monthly Report
9. Category Report
10. Date Range Report
11. Delete Transaction
12. Exit

Each transaction should contain enough information to identify:

- Transaction ID
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
    4. Transactions
    5. Reports
    6. Search
    7. Exit

Important requirements:

- The application must preserve its state between runs.
- Previously created transactions must be loaded automatically.
- New transactions must be saved.
- Deleted transactions must remain deleted after restarting.
- Calculated values must remain consistent with stored data.
- Invalid input must not crash the application.
- The application must be divided into logical functions.
- Avoid creating one huge function containing the entire program.

Do not hard-code the current balance.

The balance should be calculated from the stored financial data.

Do not manually write reports into the file.

Reports should be generated from the stored transactions.

The choice of data structures and file format is completely up to you.
"""
