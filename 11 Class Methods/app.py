# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls, title):
        cls.title = title
        cls.total_books += 1

Book.increment_book_count("python rules")
Book.increment_book_count("Story of my life")
Book.increment_book_count("Autumn")
Book.increment_book_count("Fairy Tales")
Book.increment_book_count("Unknown")
print(f"Total Books: {Book.total_books}")
