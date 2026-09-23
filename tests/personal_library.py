# ============================================================
# PROJECT 4 - PERSONAL LIBRARY
# ============================================================

"""
Build a personal library management application.

Menu:

1. Add Book
2. Remove Book
3. Search Book
4. Borrow Book
5. Return Book
6. Show All Books
7. Show Borrowed Books
8. Show Available Books
9. Exit

Each book should contain at least:

- Book ID
- Title
- Author
- Publication Year
- Category
- Borrowed / Available status

Requirements:

- Add books.
- Remove books.
- Search books.
- Search by title.
- Search by author.
- Search by category.
- Borrow a book.
- Return a book.
- Display all books.
- Display borrowed books.
- Display available books.

Search should support partial matches.

For example, searching for:

    python

could find:

    Python Crash Course
    Fluent Python
    Python Cookbook

The program must prevent a book that is already borrowed
from being borrowed again.

Persistence requirement:

All books and their current status must be saved.

Closing and reopening the application must not reset the library.
"""
