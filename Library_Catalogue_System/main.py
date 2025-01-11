class Book:
    def __init__(self, title, author):
        """Initialize a book with its title, author, and availability status."""
        self.title = title
        self.author = author
        self.available = True  

    def check_out(self):
        """Method to check out a book, updating its availability status."""
        if self.available:
            self.available = False
            print(f'You have successfully checked out "{self.title}".')
        else:
            print(f'Sorry, "{self.title}" is currently unavailable.')

    def return_book(self):
        """Method to return a book, updating its availability status."""
        if not self.available:
            self.available = True
            print(f'You have successfully returned "{self.title}".')
        else:
            print(f'"{self.title}" was not checked out.')

    def display_info(self):
        """Display information about the book."""
        status = "Available" if self.available else "Checked Out"
        print(f'Title: {self.title}, Author: {self.author}, Status: {status}')


class LibraryCatalogue:
    def __init__(self):
        """Initialize the library catalogue with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a new book to the catalogue."""
        self.books.append(book)
        print(f'Book "{book.title}" by {book.author} has been added to the catalogue.')

    def list_books(self):
        """List all the books in the catalogue."""
        if not self.books:
            print("No books in the catalogue.")
        else:
            print("\nBooks in the catalogue:")
            for book in self.books:
                book.display_info()

    def find_book(self, title):
        """Find a book by its title."""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        print(f'No book with the title "{title}" was found in the catalogue.')
        return None


def main():
    library = LibraryCatalogue()
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    library.add_book(book1)
    library.add_book(book2)
    library.list_books()
    print("\nAttempting to check out '1984'...")
    book_to_check_out = library.find_book("1984")
    if book_to_check_out:
        book_to_check_out.check_out()
    print("\nAttempting to check out '1984' again...")
    if book_to_check_out:
        book_to_check_out.check_out()
    print("\nReturning '1984'...")
    if book_to_check_out:
        book_to_check_out.return_book()
    print("\nFinal catalogue status:")
    library.list_books()

main()
