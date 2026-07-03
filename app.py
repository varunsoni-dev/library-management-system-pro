from models.book import Book
from models.library import Library
from utils.file_handler import FileHandler


def show_menu():
    print("\n" + "=" * 45)
    print("      LIBRARY MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book by ID")
    print("4. Search Book by Title")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. Display All Books")
    print("8. Count Books")
    print("9. Exit")


def main():

    books = FileHandler.load_books("data/books.json")

    library = Library(books)

    BOOK_FILE = "data/books.json"

    while True:

        show_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":

            book_id = input("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Author: ")
            try:
                year = int(input("Publication Year: "))
            except ValueError:
                print("Year must be a number.")
                continue

            book = Book(book_id, title, author, year)

            if library.add_book(book):

                FileHandler.save_books(library, BOOK_FILE)

                print("✅ Book added successfully.")

            else:

                print("❌ Book ID already exists.")

        elif choice == "2":

            book_id = input("Enter Book ID: ")

            if library.remove_book(book_id):

                FileHandler.save_books(library, BOOK_FILE)

                print("✅ Book removed successfully.")

            else:

                print("❌ Book not found.")

        elif choice == "3":

            book_id = input("Enter Book ID: ")

            book = library.search_book_by_id(book_id)

            if book:
                book.display_info()
            else:
                print("Book not found.")

        elif choice == "4":

            title = input("Enter Title: ")

            books = library.search_book_by_title(title)

            if books:

                for book in books:
                    book.display_info()

            else:
                print("Book not found.")

        elif choice == "5":

            book_id = input("Book ID: ")

            book = library.search_book_by_id(book_id)

            if book:

                if book.borrow():

                    FileHandler.save_books(library, BOOK_FILE)

                    print("✅ Borrowed Successfully.")

                else:

                    print("❌ Already Borrowed.")

        elif choice == "6":

            book_id = input("Book ID: ")

            book = library.search_book_by_id(book_id)

            if book:

                if book.return_book():

                    FileHandler.save_books(library, BOOK_FILE)

                    print("✅ Returned Successfully.")

                else:

                    print("❌ Book was already available.")

        elif choice == "7":

            library.display_all_books()

        elif choice == "8":

            print(f"\nTotal Books : {library.count_books()}")

        elif choice == "9":

            print("\nThank you for using Library Management System.")
            break

        else:
            print("Invalid Choice.")


if __name__ == "__main__":
    main()