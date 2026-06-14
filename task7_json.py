''' Pharse JSON file representing product details (name, price, quality) and display the details in tabular format.'''

import json
with open("products.json", "w") as file:
    products = [
        {"name": "Laptop", "price": 1000, "quality": "High"},
        {"name": "Smartphone", "price": 500, "quality": "Medium"},
        {"name": "Headphones", "price": 100, "quality": "Low"}
    ]
    json.dump(products, file)
with open("products.json", "r") as file:
    products = json.load(file)
    print(f"{'Name':<15} {'Price':<10} {'Quality':<10}")
    print("-" * 35)
    for product in products:
        print(f"{product['name']:<15} {product['price']:<10} {product['quality']:<10}")

