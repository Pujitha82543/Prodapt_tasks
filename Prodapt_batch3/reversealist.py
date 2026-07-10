stores = 3
days = 7

for store in range(stores):
    total_sales = 0
    for day in range(1, days + 1):
        sale = int(input(f"Enter sales for Day {day}: "))
        total_sales += sale
    print(f"Total sales for Store {store + 1}: {total_sales}")

    