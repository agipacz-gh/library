import json

class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author
        self.is_borrowed = False

    def to_dict(self):

        book_as_a_dict = {
            "title": self.title,
            "author": self.author,
            "is borrowed": self.is_borrowed,
        }
        return book_as_a_dict

class Reader:
    def __init__(self, name: str) -> None:
        self.name = name
        # self.borrowed_books = borrowed_books

class Library:
    def __init__(self):
        self.books = []
        self.readers = []

    def add_book(self, book: Book):
        self.books.append(book)

    def add_reader(self, reader: Reader):
        self.readers.append(reader)

    def borrow_book(self, book_title: str) -> None:
        for book in self.books:
            if book.title == book_title:
                if book.is_borrowed == False:
                    print(f"Udało Ci się wypożyczyć książkę: {book_title}")
                    book.is_borrowed = True
                else:
                    print(f"Książka {book_title} jest obecnie wypożyczona.")
                return
            return
        print(f"Brak książi {book_title} w systemie.")

    def return_book(self):
        pass

    def save_to_file(self, file_path):
        add_book_to_list = []

        for book in self.books:
            add_book_to_list.append(book.to_dict())

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(add_book_to_list, file, indent=4)

    def load_from_file(self, file_path) -> None:
        with open(file_path, "r+") as file:
            return json.load(file)

    def show_books_list(self):
        for book in self.books:
            if book.is_borrowed:
                availability = "Wypożyczona"
            else:
                availability = "Dostępna"

            print(book.title, book.author, availability)


my_library = Library()

book_1 = Book("Droga królów", "Brandon Sanderson")
book_2 = Book("Dzieci czasu", "Adrian Tchaikovsky")
# print(book_1.title, book_1.author)

my_library.add_book(book_1)
my_library.add_book(book_2)

reader_1 = Reader("Jan Kowalski")

# library.add_reader(reader_1)
# print(reader_1.name)

# my_library.show_books_list()

# print(book_1.to_dict())
my_library.save_to_file("library.json")
my_library.borrow_book("Droga królów")
my_library.borrow_book("Dzieci czasu")
my_library.borrow_book("Ostrze")
my_library.borrow_book("Dzieci czasu")
# status wupozyczenia obu ksiazek zmienil sie z False na True
my_library.save_to_file("library.json")
