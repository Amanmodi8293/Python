class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)

    def showInfo(self):
        print(f"The library has {self.noBooks} books. The books are")
        for book in self.books:
            print(book)

l = Library()
l.addBook("Mathametics 1")
l.addBook("Mathametics 2")
l.addBook("Mathametics 3")
l.addBook("Mathametics 4")
l.addBook("Mathametics 5")
l.showInfo()