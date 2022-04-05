# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# HarryLibrary = Library(listofbooks, library_name)


# dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input
import webbrowser



class HarshLibrary:

    book_list = ["01:Attack on Titan", "02:Naruto", "03:The Shining", "04:The Shawshank Redemption",
                 "05: Game of Thrones", "06: GOT-Clash Of Kings", "07: GOT-Storm of Swords",
                 "08: GOT-Feast for Crows", "09: GOT-Dance with Dragons"]

    global books
    books = {}

    def op_book(self):

        book_list = {"01": "Attack on Titan", "02": "Naruto", "03": "The Shining", "04": "The Shawshank Redemption",
                     "05": "Game of Thrones", "06": "GOT-Clash Of Kings", "07": "GOT-Storm of Swords",
                     "08": "GOT-Feast for Crows", "09": "GOT-Dance with Dragons"}
        lor = int(input ("Press 1 to rent book or Press 2 to Return a book: "))
        if lor == 1:
            a = input("Enter the code of the book: ")
            name = input("Enter Your Name: ")
            book_name = book_list[a]
            books.update({f"{name}": f"{book_name}"})

        elif lor == 2:
            a = input("Enter the code of the book: ")
            name = input("Enter Your Name: ")
            del books[f"{name}"]
        print(books)

    def display_book(self):
        a = input("Enter the code of the book You want to read: ")
        path = f"books\{a}.pdf"
        webbrowser.open_new(path)

    def add_book(self):
        a = input("Enter the name of the book with the serial number in format as above list of the books: ")
        print("Note: Please keep the file on desktop\n "
              "RENAME the file and Put it's CODE as the NAME of the File")
        num1 = a.split(":")
        num2 = str(num1[0])
        num3 = str(num1[1])
        ss = HarshLibrary.book_list.append(f"{num2}:{num3}")


class PersonalLibrary(HarshLibrary):

    def __init__(self, listofbooks, library):

        listofbooks = listofbooks
        library = library

    def add_book(self):
        a = input("Enter the name of the book with the serial number in format as above list of the books: ")
        print("Note: Please keep the file on desktop\n "
              "RENAME the file and Put it's CODE as the NAME of the File")
        num1 = a.split(":")
        num2 = str(num1[0])
        num3 = str(num1[1])
        ss = lbooks.append(f"{num2}:{num3}")

if __name__ == '__main__':

    data = HarshLibrary()

    i = 1
    while i > 0:
        tt = int(input("Choose the Operation-:\n"
                       "1 to Display Book\n"
                       "2 to Add a Book\n"
                       "3 to Lend or Return a Book\n"
                       "4 to create your own library: "))
        if tt == 1:
            print("The name of the books with their code:")
            a = HarshLibrary.book_list
            for items in a:
                print(items)
            data.display_book()
        elif tt == 2:
            data.add_book()
            print(data.book_list)
        elif tt == 3:
            data.op_book()
        elif tt == 4:
            user_name = input("Enter Your name: ")
            lbooks = []
            libb= f"{user_name}library"
            personal_lib = PersonalLibrary(lbooks, libb)
            gg = int(input("Choose the Operation-:\n"
                           "1 to Display Book\n"
                           "2 to Add a Book: "))
            if gg == 1:
                print("The name of the books with their code:")
                for items in lbooks:

                    print(items)
                personal_lib.display_book()
            elif gg == 2:
                personal_lib.add_book()
                print(lbooks)

        print("Thank you, Please Visit Again")
        i += 1
