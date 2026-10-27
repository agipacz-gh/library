import json

class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author
        self.is_borrowed = False


class Reader:
    def __init__(self, name: str) -> None:
        self.name = name
        #self.borrowed_books = borrowed_books


class Library:
    def __init__(self):
        self.books = {}
        self.readers = {}

    def add_book(self, book: Book):
        self.books.append(book)
        

    def add_reader(self, reader: Reader):
        self.readers.append(reader)

    def borrow_book(self):
        pass

    def return_book(self):
        pass

    def save_to_file(self,file_path):
        with open(file_path, "w") as file:
            json.dump(self.books.__dict__, file, indent=4)

    def load_from_file(self,file_path):
        with open (file_path, "r+") as file:
            return json.load(file)

    def show_books_list(self):
        for book in self.books:
            if book.is_borrowed:
                availability = "Wypożyczona"
            else: 
                availability = "Dostępna"

            print(book.title, book.author, availability)
        

my_library = Library()

book_1 = Book("Droga Królów", "Brandon Sanderson")
book_2 = Book("Dzieci czasu", "Adrian Tchaikovsky")
#print(book_1.title, book_1.author)

my_library.add_book(book_1)
my_library.add_book(book_2)

reader_1 = Reader("Jan Kowalski")

#library.add_reader(reader_1)
#print(reader_1.name)

my_library.show_books_list()

my_library.save_to_file("library.json")

