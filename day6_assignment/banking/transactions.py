import banking.accounts as accounts

def deposit(amount):
    accounts.balance += amount

def withdraw(amount):
    if amount <= accounts.balance:
        accounts.balance -= amount