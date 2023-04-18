class student():
    def __init__(self,total):
        self._total=total
    def average(self):
        return self._total/5.0

    def getter(self):
        return self._total

    def setter(self,total):
        self._total=total
        
    total=property(getter,setter)
obj=student(450)
print(obj.total)
print(obj.average())
obj.total=77
print(obj.total)
print(obj.average())