class Book:

    def __init__(self, book_id, title, author, category, status="Available"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.status = status

    def __str__(self):
        return f"{self.book_id},{self.title},{self.author},{self.category},{self.status}"