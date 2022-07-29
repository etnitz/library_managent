class Library:
    
    def __init__(self, booksList, name):
        self.booksList = booksList
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f'We have the following books in our library: {self.name}')
        for book in self.booksList:
            print(book)

    def addBook(self, book):
        if book in self.booksList:
            print('Book already exists')
        else:
            self.booksList.append(book)
            print('Book added')

    def lendBook(self, book, user):
        if book in self.booksList:
            if book not in self.lendDict.keys():
                self.lendDict.update({book: user})
                print('Book has been lended. Database updated')
            else:
                print(f'Book is already being used by {self.lendDict[book]}')
        else:
            print("Apologies, We currently do not have this book in our library")

    def returnBook():
        pass