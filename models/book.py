class Book:
    """
    Represents a single book in the library.
    """

    def __init__(self, book_id, title, author, publication_year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f'"{self.title}" has been borrowed.')
        else:
            print(f'"{self.title}" is already borrowed.')

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f'"{self.title}" has been returned.')
        else:
            print(f'"{self.title}" is already available.')

    def display_info(self):
        status = "Available" if self.is_available else "Borrowed"

        print("\nBook Information")
        print("-" * 30)
        print(f"Book ID          : {self.book_id}")
        print(f"Title            : {self.title}")
        print(f"Author           : {self.author}")
        print(f"Publication Year : {self.publication_year}")
        print(f"Status           : {status}")