import re

class Book:
    def __init__(self, title: str, author: str, book_id: str):
        """
        Initializes a new book.

        :param title: The title of the book.
        :param author: The author of the book.
        :param book_id: The id of the book.
        """
        self.title = title
        self.author = author
        self.book_id = book_id

class Library:
    def __init__(self):
        """
        Initializes a new library.
        """
        self.books = {}

    def add_book(self, book: Book) -> bool:
        """
        Adds a book to the library.

        :param book: The book object to add.
        :return: True if the book was added, False otherwise.
        """
        # TODO: Implement the method
        pass

    def remove_book(self, book_id: str) -> bool:
        """
        Removes a book from the library using its id. Ensure that the book ID is 
        validated before attempting to remove the book.

        :param book_id: The id of the book to remove.
        :return: True if the book was removed, False otherwise.
        """
        # TODO: Implement the method
        pass

    def find_book(self, book_id: str) -> Book:
        """
        Finds a book in the library using its id.

        :param book_id: The id of the book to find.
        :return: Book object if found, None otherwise.
        """
        # TODO: Implement the method
        pass

    def validate_book_id(self, book_id: str) -> bool:
        """
        Validates the book's id using a regular expression.

        :param book_id: The id of the book to validate.
        :return: True if the id is valid, False otherwise.
        """
        pattern = re.compile(r'^B\d{4}$')
        return bool(pattern.match(book_id))
