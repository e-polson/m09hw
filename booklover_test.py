import unittest
import pandas as pd
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        """Test adding a book and check if it is in book_list."""
        book_lover = BookLover(name='Carla', email='carla@example.com', fav_genre='Fantasy')
        book_lover.add_book('Harry Potter', 5)
        self.assertTrue('Harry Potter' in book_lover.book_list['book_name'].values)
    
    def test_2_add_book(self):
        """Test adding the same book twice and check if it's in book_list only once."""
        book_lover = BookLover(name='Carla', email='carla@example.com', fav_genre='Fantasy')
        book_lover.add_book('Harry Potter', 5)
        book_lover.add_book('Harry Potter', 4)  # Attempt to add the same book again
        self.assertEqual(book_lover.book_list['book_name'].tolist().count('Harry Potter'), 1)
    
    def test_3_has_read(self):
        """Test has_read() with a book that is in the list."""
        book_lover = BookLover(name='Carla', email='carla@example.com', fav_genre='Fantasy')
        book_lover.add_book('Harry Potter', 5)
        self.assertTrue(book_lover.has_read('Harry Potter'))
    
    def test_4_has_read(self):
        """Test has_read() with a book that is NOT in the list."""
        book_lover = BookLover(name='Carla', email='carla@example.com', fav_genre='Fantasy')
        book_lover.add_book('Harry Potter', 5)
        self.assertFalse(book_lover.has_read('The Hobbit'))
    
    def test_5_num_books_read(self):
        """Test num_books matches the expected number after adding books."""
        book_lover = BookLover(name='Carla', email='carla@example.com', fav_genre='Fantasy')
        book_lover.add_book('Harry Potter', 5)
        book_lover.add_book('The Hobbit', 4)
        book_lover.add_book('Twilight', 3)
        self.assertEqual(book_lover.num_books_read(), 3)
    
    def test_6_fav_books(self):
        """Test fav_books() returns books with a rating > 3."""
        book_lover = BookLover(name='Carla', email='carla@example.com', fav_genre='Fantasy')
        book_lover.add_book('Harry Potter', 5)
        book_lover.add_book('The Hobbit', 4)
        book_lover.add_book('Twilight', 3)
        book_lover.add_book('The Catcher in the Rye', 2)
        
        fav_books = book_lover.fav_books()
        self.assertTrue((fav_books['book_rating'] > 3).all())  # Check all returned ratings > 3
        self.assertEqual(len(fav_books), 2)  # Should return only "Harry Potter" and "The Hobbit"


if __name__ == '__main__':  
    unittest.main(verbosity=3)