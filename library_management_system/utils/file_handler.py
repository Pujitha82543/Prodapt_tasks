import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BOOK_FILE = os.path.join(BASE_DIR, "data", "books.csv")
MEMBER_FILE = os.path.join(BASE_DIR, "data", "members.csv")


def read_books():

    books = []

    if not os.path.exists(BOOK_FILE):
        raise FileNotFoundError("Books file not found")

    with open(BOOK_FILE, "r") as file:

        for line in file:
            books.append(line.strip().split(","))

    return books


def write_books(books):

    with open(BOOK_FILE, "w") as file:

        for book in books:
            file.write(",".join(book) + "\n")


def read_members():

    members = []

    if not os.path.exists(MEMBER_FILE):
        raise FileNotFoundError("Members file not found")

    with open(MEMBER_FILE, "r") as file:

        for line in file:
            if line.strip():
                members.append(line.strip().split(","))

    return members


def write_members(members):

    with open(MEMBER_FILE, "w") as file:

        for member in members:
            file.write(",".join(member) + "\n")