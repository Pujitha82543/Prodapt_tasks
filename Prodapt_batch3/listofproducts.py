products = ["Laptop", "Mouse", "Keybord"]

products.append("Monitor")
print(products)

new_products = ["Tablet", "Webcam"]
products.extend(new_products)
print(products)

products.remove("Mouse")
print(products)

products.pop()
print(products)

print("Laptop Count: ", products.count("Laptop"))
print("Monitor Position: ", products.index("Monitor"))

products.reverse()
print("Reversed: ", products)

backup = products.copy()
print("Backup:",backup)

products.clear()
print("After Clear:", products)

