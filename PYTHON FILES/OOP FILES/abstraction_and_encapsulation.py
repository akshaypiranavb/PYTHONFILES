#ABSTRACTION AND ENCAPSULATION
from tkinter import messagebox
class library():
    def __init__(self,books):
        self.books=books
    def showbooks(self):
        print("AVAILABLE BOOKS :")
        for book in self.books:
            print(book)
    def borrowbook(self,book):
        if book in self.books:
            print("COLLECT THE BOOK IN THE COUNTER")
            self.books.remove(book)
        else:
            print("BOOKS IS NOT AVAILABLE")
    def returnbook(self,returnbook):
        print("YOU RETURNED THE BOOK")
        self.books.append(returnbook)
books=["C","C++","JAVA","PYTHON","C#","HTML","JAVASCRIPT","CSS","AI","ML"]
obj=library(books)
msg="""
    1)AVAILABLE BOOKS
    2)TO BORROW
    3)TO RETURN
    """
while True:
    try:
        ch=int(input("ENTER YOUR CHOICE : "))
        if ch==1:
            obj.showbooks()
        elif ch==2:
            required=input("ENTER THE BOOK YOU WANT :")
            obj.borrowbook(required)
        elif ch==3:
            returnbook=input("ENTER THE NAME OF THE BOOK YOU WANT TO RETURN :")
            obj.returnbook(returnbook)
        else:
            print("THANK YOU WELCOME ")
            quit()
    except:
        messagebox.showerror("ERROR","ENTER THE CHOICE CORRECTLY")
    