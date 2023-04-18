import random
class akshay:
    course="python"
    
obj=akshay()
print(akshay.course)
print(obj.course)
print(obj.__dict__)
obj.course="SQLITE"
print(obj.__dict__)
obj.name="AKSHAY"
print(obj.__dict__)
print(akshay.course)
print(getattr(akshay,"gender","Gender is not found ra ambi"))
print(random.random())
