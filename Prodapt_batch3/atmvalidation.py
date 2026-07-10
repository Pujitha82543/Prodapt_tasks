balance = 5000
amount = int(input("Enter withdrawal amount: "))

if amount <= balance and amount % 100 == 0:
    balance -= amount
    print("Withdrawal Successfull")
    print("Remaining Balance:", balance)
else:
    print("Invalid withdrawl amount")
    