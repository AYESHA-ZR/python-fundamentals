class Book:

    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price = price
        self.available = True

    def display_info(self):
        print("Book name =", self.name)
        print("Author =", self.author)
        print("Price =", self.price)
        print("Available status =", self.available)

    def borrow_book(self):
        if self.available:
            self.available = False
            print(self.name, "has been borrowed.")
        else:
            print(self.name, "is already borrowed.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(self.name, "has been returned.")
        else:
            print(self.name, "is already available.")

class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            book.display_info()

    def borrow_book(self, book_name):
        for book in self.books:
            if book.name.lower() == book_name.lower():
                book.borrow_book()
                return

        print("Book not found.")

    def return_book(self, book_name):
        for book in self.books:
            if book.name.lower() == book_name.lower():
                book.return_book()
                return

        print("Book not found.")


book1 = Book("Python", "ABC", 567)
book2 = Book("HTML", "DEF", 876)

library = Library()

library.add_book(book1)
library.add_book(book2)

library.show_books()

library.borrow_book("Python")
library.borrow_book("Python")

library.return_book("Python")
library.return_book("Python")

library.borrow_book("Java")