class Library:
    
    def __init__(self, booksList, name):
        self.booksList = booksList
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f'We have the following books in our library: {self.name}.')
        for book in self.booksList:
            print(book)

    def addBook(self, book):
        if book in self.booksList:
            print('Book already exists.')
        else:
            self.booksList.append(book)
            print('Book added.')

    def lendBook(self, book, user):
        if book in self.booksList:
            if book not in self.lendDict.keys():
                self.lendDict.update({book: user})
                print('Book has been lended. Database updated.')
            else:
                print(f'Book is already being used by {self.lendDict[book]}.')
        else:
            print("Apologies, We currently do not have this book in our library.")

    def returnBook(self, book):
        if book in self.lendDict.keys():
            self.lendDict.pop(book)
            print('Book returned successfully.')
        else:
            print('The book does not exist in the book lending database.')

library = Library(booksList=[],name='Judy')

def main():
    while True:
        
        print(f'Welcome to {library.name} library. Following are the options, ')
        
        choice = '''1. Display books
        2. Lend a book
        3. Add a book
        4. Return a book'''
        
        print(choice)

        userInput = input('Press C to continue or Q to quit. ').lower()
        if userInput == 'c':
            userChoice = int(input('Select an option to continue:'))
            if userChoice == 1:
                library.displayBooks()
            elif userChoice == 2:
                book = input('Enter the name of the book you want to lend:')
                user = input('Enter the name of the user:')
                library.lendBook(book, user)
            elif userChoice == 3:
                book = input('Enter the name of the book you want to add:')
                library.addBook(book)
            elif userChoice == 4:
                book = input('Enter the name of the book you want to return:')
                library.returnBook(book)
            else:
                print('Please choose a valid option: 1 to display books, 2 to lend a book, 3 to add a book, 4 to return a book. ')
        elif userInput == 'q':
            break
        else:
            print('Please choose a valid option: C to continue or Q to quit.')

main()