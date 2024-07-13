def display_menu():
     print("\nLibrary Management System")
     print("1. Add Book")
     print("2. Search Book by Title or ISBN")
     print("3. Search Book by Author")
     print("4. Remove Book")
     print("5. Lend Book")
     print("6. View Lent Book")
     print("7. Return Book")
     print("8. Exit")
     
def get_menu_choice():
    return input("Enter your choice: ")

def get_book_details():
    title = input("Enter book title: ")
    authors = input("Enter authors (comma-separated): ").split(',')
    isbn = input("Enter ISBN: ")
    year = input("Enter publishing year: ")
    price = input("Enter price: ")
    quantity = int(input("Enter quantity: "))
    return title, authors, isbn, year, price, quantity

def get_search_term():
    return input("Enter search term: ")

def get_borrower_details():
    term = input("Enter book title or ISBN: ")
    borrower = input("Enter borrower name: ")
    return term, borrower

def get_return_details():
    term = input("Enter book title or ISBN: ")
    borrower = input("Enter borrower name: ")
    return term, borrower     