class Book:
    def __init__(self, title, author, is_checked_out=False):
        self.title = title
        self.author = author
        self.is_checked_out = is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}, {'Checked out' if self.is_checked_out else 'Available'}"

class LibraryManager:
    def __init__(self):
        self._books = {}

    def add_book(self, title):
        if title in self.books:
            print("This book ID already exists.")
        else:
            self.books[title] = title
    def check_out_book(self, title):
        if title not in self.books:
            print("Book not found.")
        elif self.books[title].is_checked_out:
            print("Book is already checked out.")
        else:
            self.books[title].is_checked_out = True
            print("Book checked out successfully.")  
    def return_book(self, title):
        if title not in self.books:
            print("Book not found.")
        elif not self.books[title].is_checked_out:
            print("Book is not checked out.")
        else:
            self.books[title].is_checked_out = False
            print("Book checked in successfully.")
