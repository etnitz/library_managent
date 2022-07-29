class Library:
    
    def __init__(self, booklist, name):
        self.booklist = booklist
        self.name = name
        self.lendDict = {}

    def displayBooks():
        print(f'We have the following books in our library: {self.name}')
        for book in self.booklist:
            print(book)

    def addBook():
        pass

    def lendBook():
        pass

    def returnBook():
        pass