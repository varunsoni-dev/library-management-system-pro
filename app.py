from models.book import Book
from models.library import Library


def main():

    library = Library()

    book1 = Book("B101", "Atomic Habits", "James Clear", 2018)
    book2 = Book("B102", "The Alchemist", "Paulo Coelho", 1988)
    book3 = Book("B103", "Deep Work", "Cal Newport", 2016)

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    library.display_all_books()


if __name__ == "__main__":
    main()