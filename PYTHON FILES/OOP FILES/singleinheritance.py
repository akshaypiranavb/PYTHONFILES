class akshay():
    name1="AKSHAY"
    age1=19
    def address(self):
        print("3/87-14,VASANTHAM NAGAR,PADANTHAL,SATTUR")
class piranav(akshay):
    name2="PIRANAV"
    age2=20
    def fullname(self):
        print("FIRST NAME :",self.name1)
        print("SECOND NAME :",self.name2)
        print("AKSHAY'S AGE :",self.age1)
        print("PIRANAV'S AGE :",self.age2)
obj=piranav()
obj.fullname()
obj.address()