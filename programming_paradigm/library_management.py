class Book:
    def __init__(self, title, author, is_checked_out=False):
        self.title = title
        self.author = author
        self.is_checked_out = is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}, {'Checked out' if self.is_checked_out else 'Available'}"

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, title):
        if title in self._books:
            return("This title already exists.")
        else:
            self._books.append(title)
    def check_out_book(self, title):
        if title not in self.books:
            return("Book not found.")
        elif self._books[title].self.is_checked_out:
            return("Book is already checked out.")
        else:
            self._books[title].self.is_checked_out = True
            return("Book checked out successfully.")  
    def return_book(self, title):
        if title not in self._books:
            return("Book not found.")
        elif not self._books[title].self.is_checked_out:
            return("Book is not checked out.")
        else:
            self._books[title].self.is_checked_out = False
            return("Book checked in successfully.")
        def list_availabele_books(self):
            return(self._books)
