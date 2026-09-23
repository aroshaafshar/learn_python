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
