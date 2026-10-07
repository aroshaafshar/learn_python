import json

FILENAME = "inventory_managment.json"

try:
    with open(FILENAME, "r") as file:
        products = json.load(file)
except FileNotFoundError:
    products = []

def save_products():
    with open(FILENAME, "w") as file:
        json.dump(products, file, indent=4)

def get_next_id():
    if not products:
        return 1
    return max(product["id"] for product in products) + 1

while True:
     print("1. add product\n2. remove product\n3. increase stock\n4. decrease stock\n5. show all products\n6. search product\n7. show low stock product\n8. show inventory value\n9. exit")
     choice = input("enter your choice: ")
     if choice == "1":
         product_id = get_next_id()
         name = input("enter name product: ")
         price = int(input("enter price: "))
         quantity = int(input("quantity: "))
         category = input("enter category: ")
         product = {
             "id": product_id,
             "name": name,
             "price": price,
             "quantity": quantity,
             "category": category
         }
         products.append(product)
         save_products()
         print("product added successfully.")
         print(f"product id: {product_id}")

     elif choice == "2":
         product_id = int(input("enter product id: "))
         for product in products:
             if product["id"] == product_id:
                 products.remove(product)
                 save_products()
                 print("product removed successfully.")
             if not found:
                 print("product not found.")

     elif choice == "3":
         product_id = int(input("enter product id: "))
         amount = int(input("enter amount: "))
         found = False
         for product in products:
             if product["id"] == product_id:
                 product["quantity"] += amount
                 found = True
                 save_products()
                 print("stock increased successfully.")
                 break
             if not found:
                 print("product not found.")

     elif choice == "4":
         product_id = int(input("enter product id: "))
         amount = int(input("enter amount: "))
         found = False
         for product in products:
             if product["id"] == product_id:
                 found = True
                 if product["quantity"] >= amount:
                    product["quantity"] -= amount
                    save_products()
                    print("stock decreased successfully.")
                 else:
                     print("not enough stock.")
                     break
             if not found:
                 print("product not found.") 

     elif choice == "5":
         for product in products:
             print(product)

     elif choice == "6":
         search_type = input("search by (id/name/category):" )
         search_value = input("enter search value: ")
         found = False
         for product in products:
             if search_type == "id":
                 if product["id"] == int(search_value):
                     print(product)
                     found = True
             elif search_type == "name":
                 if search_value.lower() in product["name"].lower():
                     print(product)
                     found = True
             elif search_type == "category":
                 if search_value.lower() in product["category"].lower():
                     print(product)
                     found = True
         if not found:
             print("product not found.")
                 
     elif choice == "7":
         threshold = int(input("enter low stock threshold: "))
         for product in products:
             if product["quantity"] <= threshold:
                 print(product)
                 found = True
         if not found:
             print("no low stock product.")

     elif choice == "8":
         total_value = 0
         for product in products:
             total_value += product["price"] * product["quantity"]
             print(f"total inventory value: {total_value}")
     elif choice == "9":
         print("Goodbye!")
         break
     else:
         print("invalid choice. ")