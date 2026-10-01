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

PRODUCT_FILE = "tests/products.json"
ORDERS_FILE = "orders.json"

try:
     with open(PRODUCT_FILE, "r") as file:
         products = json.load(file)
except FileNotFoundError:
     products = []

try:
     with open(ORDERS_FILE, "r") as file:
         orders = json.load(file)
except FileNotFoundError:
     orders = []

cart = []

while True:
     print("""
     1. Show products
     2. Add product to cart
     3. Remove product from cart
     4. Show cart
     5. Change product quantity
     6. Checkout
     7. Show order history
     8. Exit 
    """ )
     choice = input("Choose: ")

     if choice == "1": 
         for product in products:
             print(
                 product["id"],
                 product["name"],
                 f"{product['price']:}",
                 "stock:",
                 product["stock"]
             )

     elif choice == "2":
         for product in products:
                     print(
                         product["id"],
                         product["name"],
                         f"{product["price"]:}",
                         "stock:",
                         product["stock"]
                     )
         product_id = int(input("Product ID: "))
         quantity = int(input("Quantity: "))

         for product in products:
             if product["id"] == product_id:
                 if quantity > product["stock"]:
                     print("Not enough stock.")
                     break
                 found = False

                 for item in cart:
                     if item["id"] == product_id:
                         if item["quantity"] + quantity > product["stock"]:
                             print("Not enough stock.")
                             break

                         item["quantity"] += quantity
                         found = True
                         print("Product added.")
                         break
             if not found:
                 cart.append({
                         "id": product["id"],
                         "name": product["name"],
                         "price": product["price"],
                         "quantity": quantity
                 })
                 print("Product added.")
                 break
             
     elif choice == "3":
         if not cart:
             print("Cart is empty.")
             continue
         for item in cart:
             print(
                 item["id"],
                 item["name"],
                 "x",
                 item["quantity"]
             )
         product_id = int(input("Product ID: "))
         for item in cart:
             if item["id"] == product_id:
                 cart.remove(item)
                 print("Product removed.")
                 break
             
     elif choice == "4":
         if not cart:
             print("Cart is empty.")
             continue
         total = 0
         for item in cart:
             subtotal = item["price"] * item["quantity"]
             total += subtotal
             print(
                 item["name"],
                 "x",
                 item["quantity"],
                 "=",
                 f"{subtotal:,}"
             )
             print("Total:", f"{total:,}")

     elif choice == "5":
         if not cart:
             print("Cart is empty.")
             continue
         for item in cart:
             print(
                     item["id"],
                     item["name"],
                     "x",
                     item["quantity"]
             )
         product_id = int(input("Product ID: "))
         quantity = int(input("New quantity: "))
         for item in cart:
             for product in products:
                 if product["id"] == product_id:
                     if quantity > product["stock"]:
                         print("Not enough stock.")
                     else:
                         item["quantity"] = quantity
                         print("Quantity changed.")
                     break
             break
         
     elif choice == "6":
         if not cart:
             print("Cart is empty.")
             continue
         total = 0
         for item in cart:
             total += item["price"] * item["quantity"]

         for item in cart:
             if product["id"] == item["id"]:
                 product["stock"] -= item["quantity"]
         order = {
             "items": cart.copy(),
             "total": total
         }
         orders.append(order)

         with open(PRODUCT_FILE, "r") as file:
             json.dump(products, file, indent=4)

         with open(ORDERS_FILE, "w") as file:
             json.dump(orders, file, indent=4)

         cart.clear()
         print("Checkout successful.")
         print("Total:", f"{total:,}")

     elif choice == "7":
         if not orders:
             print("No orders yet.")
             continue
         for number, order in enumerate(orders, start=1):
             print(f"\nOrder {number}")
             for item in order["items"]:
                 print(
                     item["name"],
                     "x",
                     item["quantity"]
                 )
                 print("Total:", f"{order["total"]:,}")
     elif choice == "8":
         break
     else:
         print("Invalid choice")