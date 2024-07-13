def print_books(books):
    if books:
        print(f"{'Title':<30} {'Authors':<30} {'ISBN':<15} {'Year':<5} {'Price':<7} {'Qty':<5}")
        print("="*90)
        for book in books:
            authors = ", ".join(book.authors)
            print(f"{book.title:<30} {authors:<30} {book.isbn:<15} {book.year:<5} ${book.price:<7.2f} {book.quantity:<5}")
    else:
        print("No books found.")

def print_lent_books(lent_books):
    if lent_books:
        print(f"{'Title':<30} {'Borrower':<30}")
        print("="*60)
        for lent_book in lent_books:
            print(f"{lent_book[0].title:<30} {lent_book[1]:<30}")
    else:
        print("No books lent.")
