class akshay():
    count=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        akshay.count+=1
    def show(self):
        print(self.name,self.age)
    @staticmethod
    def welcome():
        print("welcome to sanloop ")
obj=akshay("AKSHAY",19)
obj.show()
obj.welcome()
obj1=akshay("PIRANAV",19)
obj1.show()

obj1.welcome()