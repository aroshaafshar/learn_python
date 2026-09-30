# ============================================================
# PROJECT 8 - SHOPPING CART AND ORDER HISTORY
# ============================================================

"""
Build a small shopping system.

The system should contain products.

Each product should have:

- Product ID
- Name
- Price
- Stock

Menu:

1. Show Products
2. Add Product To Cart
3. Remove Product From Cart
4. Show Cart
5. Checkout
6. Show Order History
7. Exit

Requirements:

- Display available products.
- Add products to a shopping cart.
- Remove products from the cart.
- Change product quantity in the cart.
- Calculate cart total.
- Prevent buying more than the available stock.
- Checkout the cart.
- Decrease product stock after checkout.
- Clear the cart after a successful checkout.
- Store completed orders.
- Display previous orders.

Example cart:

    Keyboard × 1
    Mouse × 2
    Monitor × 1

    Total: 8,500,000

Each completed order should contain enough information to
reconstruct what was purchased.

Persistence requirement:

Products, stock and order history must survive program restarts.
"""
import json

PRODUCTS_FILE = "product.json"
ORDERS_FILE = "orders.json"

class Product:
     def __init__(self, product_id, name, price, stock):
         self.product_id = product_id
         self.name = name

     def to_dict(self):
         return {
             "product_id": self.product_id,
             "name": self.name,
             "price": self.price,
             "stock": self.stock
         }