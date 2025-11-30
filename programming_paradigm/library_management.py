class Book:
    """
    Represents a single book in the library.
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """
        Marks the book as checked out.
        """
        self._is_checked_out = True

    def return_book(self):
        """
        Marks the book as returned/available.
        """
        self._is_checked_out = False

    def is_available(self):
        """
        Returns True if the book is available, False if checked out.
        """
        return not self._is_checked_out


class Library:
    """
    Represents a library containing multiple books.
    """
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """
        Adds a Book instance to the library collection.
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Checks out a book by title if available.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False  # Book not found or already checked out

    def return_book(self, title):
        """
        Returns a book by title if it exists in the collection.
        """
        for book in self._books:
            if book.title == title:
                book.return_book()
                return True
        return False  # Book not found

    def list_available_books(self):
        """
        Prints all books that are currently available.
        """
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
