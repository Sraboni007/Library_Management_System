# file_management.py
import json
from books import Book, Library

def save_to_file(library, filename="library.json"):
    data = {
        "books": [vars(book) for book in library.books],
        "lent_books": [(vars(lent_book[0]), lent_book[1]) for lent_book in library.lent_books]
    }
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_from_file(filename="library.json"):
    library = Library()
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            for book_data in data["books"]:
                book = Book(book_data["title"], book_data["authors"], book_data["isbn"], book_data["year"], book_data["price"], book_data["quantity"])
                library.add_book(book)
            for lent_book_data in data["lent_books"]:
                book_data, borrower = lent_book_data
                book = Book(book_data["title"], book_data["authors"], book_data["isbn"], book_data["year"], book_data["price"], book_data["quantity"])
                library.lent_books.append((book, borrower))
    except FileNotFoundError:
        pass
    return library
