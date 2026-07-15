# Online Food Delivery Order Management System

orders = {}

while True:
    print("\n===== Online Food Delivery Order Management System =====")
    print("1. Add New Order")
    print("2. Add Food Items to Order")
    print("3. Remove Item from Order")
    print("4. Display All Orders")
    print("5. Search Order by Order ID")
    print("6. Remove Order After Delivery")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # Add New Order
    if choice == "1":
        order_id = input("Enter Order ID: ")

        if order_id in orders:
            print("Order ID already exists.")
        else:
            customer = input("Enter Customer Name: ")

            orders[order_id] = {
                "customer": customer,
                "items": [],
                "total_bill": 0
            }

            print("Order created successfully")

    # Add Food Items
    elif choice == "2":
        order_id = input("Enter Order ID: ")

        if order_id in orders:
            item = input("Enter food item: ")
            price = float(input("Enter item price: "))

            orders[order_id]["items"].append(item)
            orders[order_id]["total_bill"] += price

            print("Item added to order")
        else:
            print("Order not found.")

    # Remove Item
    elif choice == "3":
        order_id = input("Enter Order ID: ")

        if order_id in orders:
            item = input("Enter item to remove: ")

            if item in orders[order_id]["items"]:
                orders[order_id]["items"].remove(item)
                print("Item removed from order")
            else:
                print("Item not found in the order.")
        else:
            print("Order not found.")

    # Display All Orders
    elif choice == "4":
        if len(orders) == 0:
            print("No orders available.")
        else:
            for order_id, details in orders.items():
                print("\nOrder ID:", order_id)
                print("Customer:", details["customer"])
                print("Items:", details["items"])
                print("Total Bill:", details["total_bill"])

    # Search Order
    elif choice == "5":
        order_id = input("Enter Order ID to search: ")

        if order_id in orders:
            print("Order Found")
            print("Customer:", orders[order_id]["customer"])
            print("Items:", orders[order_id]["items"])
            print("Total Bill:", orders[order_id]["total_bill"])
        else:
            print("Order not found.")

    # Remove Order
    elif choice == "6":
        order_id = input("Enter delivered order ID: ")

        if order_id in orders:
            del orders[order_id]
            print("Order removed from system")
            print("Remaining Orders:", orders)
        else:
            print("Order not found.")

    # Exit
    elif choice == "7":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")