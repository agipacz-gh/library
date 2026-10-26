class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author
        self.is_borrowed = False


# book_1 = Book("Droga Królów", "Brandon Sanderson")

# print(book_1.is_borrowed)


class Reader:
    def __init__(self, name: str, borrowed_books: str) -> None:
        self.name = name
        self.borrowed_books = borrowed_books


# reader_1 = Reader("Asia", "Droga Królów")

# print(reader_1.name)


class Library:
    def __init__(self):
        self.books
        pass

    def add_book(self, book):
        self.book
        pass

    def add_reader(self):
        pass

    def borrow_book(self):
        pass

    def return_book(self):
        pass

    def save_to_file(self):
        pass

    def load_from_file(self):
        pass
