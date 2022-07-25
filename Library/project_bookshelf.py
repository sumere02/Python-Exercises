import sqlite3
class Book():
    def __init__(self,name = "None",writer = "None",publisher ="None",type = "None",year = 0):
        self.name = name
        self.writer = writer
        self.publisher = publisher
        self.type = type
        self.year = year
    def __str__(self):
        print("Book: {}\nWriter: {}\nPublisher: {}\nType: {}\nYear: {}\n".format(self.name,self.writer,self.publisher,self.type,self.year))

class Library():
    def __init__(self):
        self.connection()
    def connection(self):
        self.connect = sqlite3.connect("database.db")
        self.cursor = self.connect.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Books (Name TEXT,Writer TEXT,Publisher TEXT,Type TEXT,Year INT)")
        self.connect.commit()
    def unconnect(self):
        self.connect.close()
    def show_books(self):
        self.cursor.execute("SELECT * FROM Books")
        books = self.cursor.fetchall()
        if len(books) == 0:
            print("Empty Library")
        else:
            for i in books:
                book = Book(i[0],i[1],i[2],i[3],i[4])
                book.__str__()
    def show_books_only_name(self):
        self.cursor.execute("SELECT Name FROM Books")
        books = self.cursor.fetchall()
        if len(books) == 0:
            print("Empty Library")
        else:
            for i in books:
                print(i[0])
    
    
    def search_book(self,name):
        self.cursor.execute("SELECT * From Books where name = ?",(name,))
        books = self.cursor.fetchall()
        if len(books) == 0:
            print("Selected book is not exists")
        else:
            for i in books:
                book = Book(i[0],i[1],i[2],i[3],i[4])
                book.__str__()
            
    def search_book_writer(self,writer):
        self.cursor.execute("SELECT * FROM Books WHERE Writer = ?",(writer,))
        books = self.cursor.fetchall()
        if len(books) == 0:
            print("Writer does not exists in table")
        else:
            for i in books:
                book = Book(i[0],i[1],i[2],i[3],i[4])
                book.__str__()


    def add_book(self,book):
        self.cursor.execute("INSERT INTO Books VALUES (?,?,?,?,?)",(book.name,book.writer,book.publisher,book.type,book.year))
        self.connect.commit()
    def delete_book(self,name):
        self.cursor.execute("SELECT * FROM Books where name = ?",(name,))
        books = self.cursor.fetchall()
        if len(books) == 0:
            print("Book not exists in library")
        else:
            self.cursor.execute("DELETE FROM Books where name = ?",(name,))
            self.connect.commit()
    def update_year(self,name):
        self.cursor.execute("SELECT * FROM Books where name = ?",(name,))
        books = self.cursor.fetchall()
        if len(books) == 0:
            print("Book does not exists")
        else:
            year = books[0][4]
            year += 1
            self.cursor.execute("UPDATE Books set year = ? where name = ?",(year,name))
            self.connect.commit()
    def sort_books(self):
        self.cursor.execute("SELECT * FROM Books")
        books = self.cursor.fetchall()
        if len(books) == 0:
            print("Empty Library")
        else:
            self.cursor.execute("DELETE FROM Books")
            books.sort(key = lambda x: x[1])
            for i in books:
                temp = Book(i[0],i[1],i[2],i[3],i[4])
                self.cursor.execute("INSERT INTO Books VALUES (?,?,?,?,?)",(temp.name,temp.writer,temp.publisher,temp.type,temp.year))
                
            self.connect.commit()