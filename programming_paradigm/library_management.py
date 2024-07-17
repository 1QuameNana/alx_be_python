class Book:
    """creates a book class with attributes title author and also checks
    if the book is checked out or is available for borrowing
    """
    def __init__(self, title,author):
        self.title = title
        self.author =author
        self.is_checked_out = False
        
    def return_book(self):
        """ This is a method to return borrowed books by using the checkout 
        attribute
        """
        if self.is_checked_out == False:
            return'book available'
        else:
            return 'book returned successfully'
        
    def is_check_out(self):
        """ checks to see a title is checked"""
        if self.is_check_out ==True:
            return f'{self.title} is checked out'
        else:
            return f'{self.title} is available for borrowing '
         
    
    
class library:
    """ Creates a library to add, check out, and return borrowed books by 
    referencing their titles
    """
    def __init__(self):
        self._books = []
        
    def add_book(self, title):
        """ adds books to the list _books by title referencing"""
        if title not in self._books:
            self._books.append(title)
        
        
    def is_checked_out(self, title):
        """ A method to check out a book by referencing the title fromt the list
        _books"""
        if title not in self._books:
            return 'book not found'
        elif title.self.is_checked_out:
            return f'{title} is already'     
        else:
            title.self.is_checked_out = True
        
            return f'{title} is checked out successfully'
        
    def return_book(self, title):
        """Returns borrowed books back to the list _books"""
        if title in self._books:
            
            return f'{title} is available'
        else:
            
            return f'{title} is returned successfully'
        
    def listavailablebooks(self):
        """ Prints the available books for viewing"""
        for book in self._books: 
            print(book)

