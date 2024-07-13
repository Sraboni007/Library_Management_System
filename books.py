# books.py
class Book:
    def __init__(self, title, authors, isbn, year, price, quantity):
        self.title = title
        self.authors = authors  # List of authors
        self.isbn = isbn
        self.year = year
        self.price = float(price)
        self.quantity = quantity

    def __repr__(self):
        return f"Title: {self.title}, Authors: {', '.join(self.authors)}, ISBN: {self.isbn}, Year: {self.year}, Price: ${self.price}, Quantity: {self.quantity}"

class Library:
    def __init__(self):
        self.books = []
        self.lent_books = []

    def add_book(self, book):
        self.books.append(book)

    def view_books(self):
        for book in self.books:
            print(book)

    def search_books(self, term):
        results = [book for book in self.books if term in book.title or term in book.isbn]
        return results

    def search_by_author(self, author_name):
        results = [book for book in self.books if author_name in book.authors]
        return results

    def remove_book(self, term):
        for book in self.books:
            if term in book.title or term in book.isbn:
                self.books.remove(book)
                return True
        return False

    def lend_book(self, term, borrower):
        for book in self.books:
            if (term in book.title or term in book.isbn) and book.quantity > 0:
                book.quantity -= 1
                self.lent_books.append((book, borrower))
                return True
        return False

    def return_book(self, term, borrower):
        for lent_book in self.lent_books:
            if (term in lent_book[0].title or term in lent_book[0].isbn) and lent_book[1] == borrower:
                lent_book[0].quantity += 1
                self.lent_books.remove(lent_book)
                return True
        return False

    def view_lent_books(self):
        for lent_book in self.lent_books:
            print(f"Title: {lent_book[0].title}, Borrower: {lent_book[1]}")
