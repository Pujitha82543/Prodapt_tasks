from services.library_service import *

while True:

    print("\n===== Library Management System =====")
    print("1. View Books")
    print("2. Add Book")
    print("3. Register Member")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    try:

        if choice == "1":
            view_books()

        elif choice == "2":
            add_book()

        elif choice == "3":
            register_member()

        elif choice == "4":
            borrow_book()

        elif choice == "5":
            return_book()

        elif choice == "6":
            print("Thank you for using the Library Management System.")
            break

        else:
            print("Invalid choice")

    except FileNotFoundError:
        print("Error: Data file not found.")

    except Exception as e:
        print("Error:", e)
