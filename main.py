from books import Book, Library
from file_manage import save_to_file, load_from_file
from menu import display_menu, get_menu_choice, get_book_details, get_search_term, get_borrower_details, get_return_details
from utils_custom import print_books, print_lent_books

def main():
    library = load_from_file()
    
    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == '1':
            title, authors, isbn, year, price, quantity = get_book_details()
            book = Book(title, authors, isbn, year, price, quantity)
            library.add_book(book)
            save_to_file(library)
            print("Book added successfully.")
        
        elif choice == '2':
            print_books(library.books)
        
        elif choice == '3':
            term = get_search_term()
            results = library.search_books(term)
            print_books(results)
        
        elif choice == '4':
            author = get_search_term()
            results = library.search_by_author(author)
            print_books(results)
        
        elif choice == '5':
            term = get_search_term()
            if library.remove_book(term):
                save_to_file(library)
                print("Book removed successfully.")
            else:
                print("Book not found.")
        
        elif choice == '6':
            term, borrower = get_borrower_details()
            if library.lend_book(term, borrower):
                save_to_file(library)
                print("Book lent successfully.")
            else:
                print("Not enough books available to lend.")
        
        elif choice == '7':
            term, borrower = get_return_details()
            if library.return_book(term, borrower):
                save_to_file(library)
                print("Book returned successfully.")
            else:
                print("Book not found or borrower incorrect.")
        
        elif choice == '8':
            print_lent_books(library.lent_books)
        
        elif choice == '9':
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
