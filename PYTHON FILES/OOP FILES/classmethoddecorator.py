class akshay():
    count=0
    def __init__(gg,name,age):
        gg.name=name
        gg.age=age
        akshay.count+=1
    def show(gg):
        print(gg.name,gg.age)
    @classmethod
    def total(cls):
        print(akshay.count)
obj=akshay("AKSHAY",19)
obj.show()
obj1=akshay("PIRANAV",19)
obj1.show()
obj.total()
obj1.total()