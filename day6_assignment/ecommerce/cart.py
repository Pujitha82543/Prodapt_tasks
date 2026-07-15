cart = []

def add_item(item, price):
    cart.append((item, price))

def remove_item(item):
    for i in cart:
        if i[0] == item:
            cart.remove(i)
            break

def total():
    return sum(price for item, price in cart)