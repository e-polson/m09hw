from booklover.booklover import BookLover

# Create a BookLover object
book_lover = BookLover(name="Jen", email="jen@example.com", fav_genre="fiction")

# Add books using the add_book method
book_lover.add_book("Farenheit 451", 4)
book_lover.add_book("Iron Flame", 5)

# Add a new book
book_lover.add_book("Emma", 2)

# Print the number of books read
print(f"Number of books read: {book_lover.num_books_read()}")

# Print favorite books
print("Favorite books (rating > 3):")
print(book_lover.fav_books())