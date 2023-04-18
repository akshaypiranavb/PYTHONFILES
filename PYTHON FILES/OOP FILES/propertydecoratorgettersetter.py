class student():
    def __init__(self,total):
        self._total=total
    def average(self):
        return self._total/5.0
    @property
    def total(self):
        return self._total
    @total.setter
    def total(self,total):
        self._total=total
obj=student(450)
print(obj.total)
print(obj.average())
obj.total=77
print(obj.total)
print(obj.average())