import json

from models.book import Book


class FileHandler:

    @staticmethod
    def save_books(library, filename):

        books_data = []

        for book in library.books:

            books_data.append({
                "book_id": book.book_id,
                "title": book.title,
                "author": book.author,
                "publication_year": book.publication_year,
                "is_available": book.is_available
            })

        with open(filename, "w", encoding="utf-8") as file:

            json.dump(books_data, file, indent=4)

    @staticmethod
    def load_books(filename):

        books = []

        try:

            with open(filename, "r", encoding="utf-8") as file:

                books_data = json.load(file)

                for item in books_data:

                    book = Book(
                        item["book_id"],
                        item["title"],
                        item["author"],
                        item["publication_year"]
                    )

                    book.is_available = item["is_available"]

                    books.append(book)

        except (FileNotFoundError, json.JSONDecodeError):
            return []

        return books