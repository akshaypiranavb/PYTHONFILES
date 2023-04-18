class addition:
    def __init__(self,a):
        self.a=a
    def __add__(obj1,obj2):
        return obj1.a+obj2.a
    def __sub__(obj1,obj2):
        return(obj.a-obj2.a)

obj1=addition(10)
obj2=addition(20)
print(obj1+obj2)
print(obj1.a-obj2.a)