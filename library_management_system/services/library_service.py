from utils.file_handler import *

from exceptions.custom_exceptions import *


def view_books():

    books = read_books()

    print("\nAvailable Books\n")

    for book in books:

        print("Book ID :", book[0])
        print("Title   :", book[1])
        print("Author  :", book[2])
        print("Category:", book[3])
        print("Status  :", book[4])
        print()


def add_book():

    books = read_books()

    book_id = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    category = input("Enter Category: ")

    books.append([book_id, title, author, category, "Available"])

    write_books(books)

    print("Book added successfully.")


def register_member():

    members = read_members()

    member_id = input("Enter Member ID: ")
    name = input("Enter Name: ")
    email = input("Enter Email: ")

    members.append([member_id, name, email, ""])

    write_members(members)

    print("Member registered successfully.")


def borrow_book():

    books = read_books()
    members = read_members()

    member_id = input("Enter Member ID: ")
    book_id = input("Enter Book ID: ")

    member = None

    for m in members:

        if m[0] == member_id:
            member = m
            break

    if member is None:
        raise MemberNotFound("Member not found")

    book = None

    for b in books:

        if b[0] == book_id:
            book = b
            break

    if book is None:
        raise BookNotFound("Book not found")

    if book[4] == "Borrowed":
        raise BookUnavailable("Book is already borrowed")

    book[4] = "Borrowed"

    if member[3] == "":
        member[3] = book_id
    else:
        member[3] += ";" + book_id

    write_books(books)
    write_members(members)

    print("Book borrowed successfully.")


def return_book():

    books = read_books()
    members = read_members()

    member_id = input("Enter Member ID: ")
    book_id = input("Enter Book ID: ")

    member = None

    for m in members:

        if m[0] == member_id:
            member = m
            break

    if member is None:
        raise MemberNotFound("Member not found")

    borrowed = member[3].split(";") if member[3] else []

    if book_id not in borrowed:
        raise BookNotBorrowed("Book not borrowed by this member")

    borrowed.remove(book_id)

    member[3] = ";".join(borrowed)

    for b in books:

        if b[0] == book_id:
            b[4] = "Available"

    write_books(books)
    write_members(members)

    print("Book returned successfully.")