class Library:
    def __init__(self, books):
        self.books = books

    def display_books(self):
        print("Available Books:")
        for book in self.books:
            print(book)

    def borrow_book(self, book_title):
        if book_title in self.books:
            self.books.remove(book_title)
            print(f"Book '{book_title}' borrowed successfully.")
        else:
            print(f"Book '{book_title}' not available.")

    def return_book(self, book_title):
        self.books.append(book_title)
        print(f"Book '{book_title}' returned successfully.")


class Student:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def display_borrowed_books(self):
        if not self.borrowed_books:
            print("No books borrowed.")
        else:
            print("Borrowed Books:")
            for book in self.borrowed_books:
                print(book)

    def borrow_book(self, library, book_title):
        library.borrow_book(book_title)
        self.borrowed_books.append(book_title)

    def return_book(self, library, book_title):
        library.return_book(book_title)
        self.borrowed_books.remove(book_title)


# Sample books in the library
library_books = ["Introduction to Python", "Data Structures and Algorithms", "Machine Learning Basics", "Web Development with Flask"]

# Creating instances of Library and Student classes
library = Library(library_books)
student = Student("John Doe")

# Display available books in the library
library.display_books()

# John borrows a book
student.borrow_book(library, "Introduction to Python")

# Display borrowed books by John
student.display_borrowed_books()

# Display updated list of available books in the library
library.display_books()

# John returns a book
student.return_book(library, "Introduction to Python")

# Display updated list of available books and borrowed books by John
library.display_books()
student.display_borrowed_books()
















