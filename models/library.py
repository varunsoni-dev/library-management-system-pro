from models.book import Book


class Library:

    def __init__(self, books=None):
        self.books = books if books else []

    def add_book(self, book: Book) -> bool:

        if self.search_book_by_id(book.book_id):
            return False

        self.books.append(book)
        return True

    def display_all_books(self):

        if not self.books:
            print("No books available.")
            return

        print("\nLibrary Books")
        print("=" * 40)

        for book in self.books:
            book.display_info()

    def search_book_by_id(self, book_id: str) -> Book | None:
        for book in self.books:
            if book.book_id == book_id:
                return book

        return None
    
    def remove_book(self, book_id: str) -> bool:

        for book in self.books:

            if book.book_id == book_id:

                self.books.remove(book)

                return True

        return False

    def search_book_by_title(self, title: str) -> list[Book]:

        found_books = []

        for book in self.books:

            if title.lower() in book.title.lower():
                found_books.append(book)

        return found_books
    
    def count_books(self) -> int:

        return len(self.books)