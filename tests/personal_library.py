import json

try:
    with open("library.json", "r") as file:
        books = json.load(file)
except FileNotFoundError:
        books = []

class book:
     def __init__(self, book_id, title, author, year, category, borrowed=False):
          self.book_id = book_id
          self.title = title
          self.author = author
          self.year = year
          self.category = category
          self.borrowed = borrowed

class library:
     def __init__(self, books):
          self.books = books

     def save_books(self):
         with open("library.json", "w") as file:
              json.dump(self.books, file, indent=4)

library = library(books)

while True:
     print("1. add book\n2. remove book\n3. search book\n4. borrow book\n5. return book\n6. show all books\n7. show borrowed books\n8. show avaible books\n9. exit")
     choice = input("enter your choice: ")
     if choice == "1":
         if books:
             book_id = max(book["id"] for book in books) + 1
         else:
             book_id = 1
         print(f"your book id is : {book_id}")
         title = input("enter book title: ")
         author = input("enter author: ")
         while True:
             try:
                 year = int(input("enter publication year: "))
                 break
             except ValueError:
                 print("please enter a valid year.")
         category = input("enter category: ")
         book = {
              "id": book_id,
              "title": title,
              "author": author,
              "year": year,
              "category": category,
              "borrowed": False
         }
         books.append(book)
         library.save_books()
         print("book added successfully.")
              
     elif choice == "2":
          book_id = int(input("enter book id to remove: "))
          for book in books:
             if book["id"] == book_id:
                  books.remove(book)
                  library.save_books()
                  print("book removed successfully.")
                  break
             else:
                  print("book not found.")

     elif choice == "3":
         search = input("enter search term: ").lower()
         found = False
         for book in books:
                 if (search in book["title"].lower()
                       or search in book["author"].lower()
                       or search in book["category"].lower()):
                     print(book)
                     found = True
         if not found:
               print("book not found.")
                
     elif choice == "4":
         book_id = int(input("enter book id to borrow: "))
         for book in books:
             if book["id"] == book_id:
                 if book["borrowed"]:
                      print("book is already borrowed.")
                 else:
                      book["borrowed"] = True
                      library.save_books()
                      print("book borrowed successfully.")
                 break
                
     elif choice == "5":
         book_id = int(input("enter book id to return: "))
         for book in books:
             if book["id"] == book_id:
                 if not book["borrowed"]:
                      print("book already avaible.")
                 else:
                      book["borrowed"] = False
                      library.save_books()
                      print("book returned successfully.")
                 break
         else:
             print("book not found.")

     elif choice == "6":
         if not books:
             print("no books in the library.")
         else:
             for book in books:
                 print(book)

     elif choice == "7":
         found = False
         for book in books:
             if book["borrowed"]:
                 print(book)
                 found = True
         if not found:
             print("no borrowed books.")        
          
     elif choice == "8":
         found = False
         for book in books:
             if not book["borrowed"]:
                 print(book)
                 found = True
         if not found:
             print("no avaible books.")

     elif choice == "9":
          print("Goodbye!see you later!")
          break
     else:
          print("invalid choice.")