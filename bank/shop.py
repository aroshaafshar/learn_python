products= [
    {"name": "iphone 15", "price":700, "category":"phone"},
    {"name": "samsung s24", "price":650, "category":"phone"},
    {"name": "macbook air", "price":1200, "category":"laptop"},
    {"name": "Dell XPS", "price":1100, "category":"laptop"},
    {"name": "airpods", "price":200, "category":"audio"}
]
search_query = input("search:")
max_price = int(input("maximum price:"))
category_query = input("category:")
for p in products:
 if (
     search_query in p["name"]
     and p["price"] <= max_price
     and p["category"] == category_query
     ):
     print(f"{p["name"]} - ${p["price"]}")