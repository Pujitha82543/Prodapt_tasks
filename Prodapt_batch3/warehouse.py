categories = ["Electronics", "Furniture","Groceries"]

products = []
stocks = []

for category in categories:
    product_list = []
    stock_list = []
    
    for i in range(2):
        product = input(f"Enter Product {i + 1} for {category:}")
        stock = int(input(f"Enter Stock for {product:}"))

        product_list.append(product)
        stock_list.append(stock)

    products.append(product_list)
    stocks.append(stock_list)

print("\n --------------------INVENTORY REPORT--------------------")

for i in range(len(categories)):
    print("\nCategory:", categories[i])

    for j in range(len(products[i])):
        print(products[i][j], ":", stocks[i][j], "units")