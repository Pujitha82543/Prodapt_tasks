import math
import statistics
import string
from functools import reduce

# ==========================
# 1. SHAPES PACKAGE
# ==========================

def circle_area(radius):
    return math.pi * radius * radius

def circle_perimeter(radius):
    return 2 * math.pi * radius

def rectangle_area(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width)

print("----- SHAPES PACKAGE -----")
print("Circle Area:", circle_area(7))
print("Circle Perimeter:", round(circle_perimeter(7), 2))
print("Rectangle Area:", rectangle_area(10, 5))
print("Rectangle Perimeter:", rectangle_perimeter(10, 5))


# ==========================
# 2. ECOMMERCE PACKAGE
# ==========================

cart = []

def add_item(item, price):
    cart.append((item, price))

def remove_item(item):
    for i in cart:
        if i[0] == item:
            cart.remove(i)
            break

def total_bill():
    return sum(price for item, price in cart)

print("\n----- ECOMMERCE PACKAGE -----")
add_item("Laptop", 50000)
add_item("Mouse", 1000)
remove_item("Mouse")
print("Cart:", cart)
print("Total Bill:", total_bill())
print("Payment Successful")


# ==========================
# 3. UTILITIES PACKAGE
# ==========================

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

numbers = [10, 20, 30, 40]

print("\n----- UTILITIES PACKAGE -----")
print("Without Punctuation:", remove_punctuation("Hello, Python!"))
print("Vowel Count:", count_vowels("Hello Python"))
print("Mean:", statistics.mean(numbers))
print("Median:", statistics.median(numbers))


# ==========================
# 4. SCHOOL PACKAGE
# ==========================

students = []
teachers = {}

def add_student(name):
    students.append(name)

def assign_subject(teacher, subject):
    teachers[teacher] = subject

def grade(mark):
    if mark >= 85:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 50:
        return "C"
    else:
        return "Fail"

add_student("Ravi")
add_student("Anu")
assign_subject("Mr. Kumar", "Python")

print("\n----- SCHOOL PACKAGE -----")
print("Students:", students)
print("Teachers:", teachers)
print("Grade for 82 Marks:", grade(82))


# ==========================
# 5. BANKING PACKAGE
# ==========================

balance = 0

def deposit(amount):
    global balance
    balance += amount

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount

deposit(5000)
withdraw(1000)

print("\n----- BANKING PACKAGE -----")
print("Current Balance:", balance)


# ==========================
# LAMBDA FUNCTIONS
# ==========================

print("\n----- LAMBDA FUNCTIONS -----")

# 1. Sort Employees
employees = [("Asha", 85), ("Bala", 92), ("Chitra", 78)]
sorted_employees = sorted(employees, key=lambda x: x[1], reverse=True)
print("Sorted Employees:", sorted_employees)

# 2. Square Numbers
readings = [2, 3, 4]
squares = list(map(lambda x: x**2, readings))
print("Squares:", squares)

# 3. Filter Odd Numbers
player_ids = [101, 102, 103, 104, 105]
odd_ids = list(filter(lambda x: x % 2 != 0, player_ids))
print("Odd IDs:", odd_ids)

# 4. Product Using Reduce
dimensions = [2, 3, 5]
product = reduce(lambda x, y: x * y, dimensions)
print("Product:", product)

# 5. Sort Dictionary by Marks
student_marks = {
    "Asha": 78,
    "Bala": 90,
    "Chitra": 65
}

rank_list = sorted(student_marks.items(), key=lambda x: x[1], reverse=True)
print("Rank List:", rank_list)