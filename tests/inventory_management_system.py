# ============================================================
# PROJECT 3 - INVENTORY MANAGEMENT SYSTEM
# ============================================================

"""
Build a small inventory management application.

Menu:

1. Add Product
2. Remove Product
3. Increase Stock
4. Decrease Stock
5. Show All Products
6. Search Product
7. Show Low Stock Products
8. Show Inventory Value
9. Exit

Each product should contain at least:

- Product ID
- Name
- Price
- Quantity
- Category

Example:

    ID: 15
    Name: Keyboard
    Price: 2,500,000
    Quantity: 7
    Category: Computer

Requirements:

- Product IDs must be unique.
- A product can be added.
- A product can be removed.
- Stock can be increased.
- Stock can be decreased.
- The stock quantity can never become negative.
- A product cannot be removed if it does not exist.
- Products can be searched.
- Products can be filtered by category.
- Low-stock products should be displayed.

The user should be able to define what "low stock" means.

For example:

    Quantity <= 5

The program must also calculate the total value of the inventory.

Example:

    Keyboard: 7 × 2,500,000
    Mouse:    10 × 1,200,000

    Total Inventory Value: 29,500,000

Persistence requirement:

Products and their current stock levels must be saved to a file.

After restarting the program, all products must still exist
with their latest quantities.
"""
