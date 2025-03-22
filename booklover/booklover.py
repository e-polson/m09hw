import pandas as pd

class BookLover:
    
    # constructor
    def __init__(self, name, email, fav_genre, num_books=0, book_list=None):
        """
        Initialize a BookLover object.

        INPUTS:
        name (str): The name of the person.
        email (str): The person's email (serves as a unique identifier).
        fav_genre (str): The person's favorite book genre.
        num_books (int, optional): Number of books the person has read. Default is 0.
        book_list (pd.DataFrame, optional): DataFrame with columns ['book_name', 'book_rating']. Default is an empty DataFrame.
        """
        self.name = name #String
        self.email = email #String
        self.fav_genre = fav_genre #String
        self.num_books = num_books #Integer
        self.book_list = book_list if book_list is not None else pd.DataFrame({'book_name': [], 'book_rating': []}) #DataFrame
    
    def add_book(self, book_name, rating):
        """
        Adds a book to a person's book_list
        
        INPUTS:
        book_name (str)
        rating    (int, 0-5)
        """  
        if book_name in self.book_list['book_name'].values:
             print(f"The book '{book_name}' has already been read by {self.name}")
        else:
            # First, validate the rating is an integer between 0 and 5
            if not isinstance(rating, int):
                raise ValueError('Rating must be an integer')
            
            if not (0 <= rating <= 5):
                print('Error: Rating must be an integer between 0 and 5')
                return None
            
            # Add the book to the book_list and increase the number of books read
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1  # Increment the number of books read
            print(f"The book '{book_name}' has been added to {self.name}'s book list")
            
    def has_read(self, book_name):
        """
        Checks if the person has read the specified book.
        
        INPUTS:
        book_name (str)
        """
        return book_name in self.book_list['book_name'].values
    
    def num_books_read(self):
        return self.num_books
            
    def fav_books(self):
        """
        Returns a filtered DataFrame of the highest-rated books (rating > 3).
        
        RETURNS:
        pd.DataFrame: DataFrame containing books with a rating > 3.
        """ 
        return self.book_list[self.book_list['book_rating'] > 3]
    
    
if __name__ == '__main__':  
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    # And so forth