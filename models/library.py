from models.book import Book


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'"{book.title}" added successfully.')

    def display_all_books(self):

        if not self.books:
            print("No books available.")
            return

        print("\nLibrary Books")
        print("=" * 40)

        for book in self.books:
            book.display_info()