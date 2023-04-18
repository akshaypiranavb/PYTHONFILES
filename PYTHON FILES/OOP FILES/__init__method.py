class akshay():

    def __init__(self,age):
        print("OBJECT CREATED SO CONSTRUCTOR CALLED")
        self.age=age
    def show(self):
        print("AGE : ",self.age)
obj=akshay(19)
obj.show()
obj1=akshay(222)
obj1.show()
print(obj.__dict__)
print(obj1.__dict__)
