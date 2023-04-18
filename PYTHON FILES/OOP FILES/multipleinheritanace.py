class beema():
    def drive(self):
        print("KNOWS DRIVING")
    def business(self):
        print("KNOWS HOW TO DO BUSINESS")
class latha:
    def cook(self):
        print("KNOWS COOKING")
    def teach(self):
        print("KNOWS COOKING")
    def intelligent(self):
        print("KNOWS HOW TO HANDLE")
class akshay(beema,latha):
    def code(self):
        print("KNOWS CODING")
obj=akshay()
obj.drive()
obj.business()
obj.cook()
obj.teach()
obj.intelligent()
obj.code()