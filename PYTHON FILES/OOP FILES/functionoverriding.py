class employee:
    def workinghours(self):
        self.hour=80
    def show(self):
        print(self.hour)
class trainee(employee):
    def workinghours(self):
        self.hour=50
    def emphours(self):
        super().workinghours()
obj=trainee()
obj.workinghours()
obj.show()
obj1=employee()
obj1.workinghours()
obj1.show()
obj.emphours()
obj.show()
