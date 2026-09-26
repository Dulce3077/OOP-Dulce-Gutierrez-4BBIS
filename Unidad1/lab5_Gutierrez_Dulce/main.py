# Hay que tener una clase para cada tabla

from books import books
from users import user
from library import Library

book1 = books("001","OOP Fundamentals","John L","BBC")
book2 = books("002","Python for dummies","Stef Maruzh","For dummies")

user1 = user("001","Dulce Gutierrez","1234")

library = Library()# Creación de la instancia "library"
library.add_books(book1)
library.add_books(book2)
library.add_users(user1)

library.show_books()

# Requirements
# 1. The system must allow book registration.
# 2. The system must allow user registration.
# 3. The system must allow a book to be borrowed by a user.
# 4. A book that has already been borrowed can't be borrowed again.
# 5. The system must allow a book to be returned.

# For the past three we must work with self.available

print("\n\t...::Menu::...")
print("\n\t1. Register a book.")
print("\n\t2. Register a user.")
print("\n\t3. Borrow a book.")
print("\n\t4. Return a book.")
opt = input("\n\tPlease declare the option selected: ")

match opt:
    case "1":
        print("\033c")
        id_book = input("\n\tPlease declare the book id: ")
        title = input("\n\tPlease declare the book title: ")
        author = input("\n\tPlease declare the book author: ")
        editorial = input("\n\tPlease declare the book editorial: ")
        new_book = books(id_book,title,author,editorial)
        library.add_books(new_book)

    case "2":
        print("\033c")
        id_user = input("\n\tPlease declare the user id: ")
        name = input("\n\tPlease declare the user name: ")
        password = input("\n\tPlease declare the user password: ")
        new_user = user(id_user,name,password)
        library.add_users(new_user)

    case "3":
        print("\033c")
        id_book = input("Please declare the book id: ")
        for book_in_library in library.books:

            if book_in_library.id_book == id_book:

                if book_in_library.available == True:
                    book_in_library.available = False
                    print("\n\tBook borrowed successfully!")
                else:
                    print("\n\tThe book is not available.")
                break

    case "4":
        print("\033c")
        id_book = input("Please declare the book id: ")

        for book_in_library in library.books:

            if book_in_library.id_book == id_book:

                if book_in_library.available == False:
                    book_in_library.available = True
                    print("\n\tBook returned successfully!")
                else:
                    print("\n\tThe book was not borrowed.")
                break
