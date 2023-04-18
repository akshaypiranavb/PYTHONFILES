class user():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.state=self.name+" is "+str(self.age)
    @property
    def show(self):
        return self.name + " IS "+str(self.age)+" YEARS OLD"
obj=user("AKSHAY",19)
print(obj.name)
print(obj.age)
print(obj.state)
print(obj.show)
obj.age=99
print(obj.state)
print(obj.age)#here not change in run time
print(obj.show)