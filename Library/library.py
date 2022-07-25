from project_bookshelf import *

print("""***************************************

SUMER LIBRARY

1.Show Books
2.Search Books
3.Add Book
4.Delete Book
5.Update Year
6.Show Books(Only Names)
7.Search Books(Writer)
8.Sort By Name
EXIT:Q
***************************************""")

library = Library()
while True:
    operation = input("Operation: ")
    if operation == 'Q':
        print("Goodbye")
        library.unconnect()
        break
    else:
        if operation == '1':
            library.show_books()
        elif operation == '2':
            name = input("Book name: ")
            library.search_book(name)
        elif operation == '3':
            name = input("Book Name: ")
            writer = input("Writer: ")
            publisher = input("Publisher: ")
            type = input("Type: ")
            year = input("Book Year: ")
            book = Book(name,writer,publisher,type,year)
            library.add_book(book)
        elif operation == '4':
            name = input("Book Name: ")
            library.delete_book(name)
        elif operation == '5':
            name = input("Book Name: ")
            library.update_year(name)
        elif operation == '6':
            library.show_books_only_name()
        elif operation == '7':
            writer = input("Writer: ")
            library.search_book_writer(writer)
        elif operation == '8':
            library.sort_books()
        else:
            print("Unvalid operation")
