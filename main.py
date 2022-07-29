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

    def returnBook(self, book):
        if book in self.lendDict.keys():
            self.lendDict.pop(book)
            print('Book returned successfully')
        else:
            print('The book does not exist in the book lending database')

library = Library()

def main():
    while True:
        
        print(f'Welcome to {library.name} library. Following are the options,')
        
        choice = '''1. Display books
        2. Lend a book
        3. Add a book
        4. Return a book'''
        
        print(choice)

        userInput = input('Press Q to quit or C to continue').lower()
        if userInput == 'c':
            userChoice = int(input('Select an option to continue:'))
            if userChoice == 1:
                library.displayBooks()
            elif userChoice == 2:
                