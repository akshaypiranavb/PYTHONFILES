class grandfather:
    def house(self):
        print("HAVING HOUSE")
class father(grandfather):
    def car(self):
        print("HAVING CAR")
        
class son(father):
    def bike(self):
        print("HAVING BIKE")
obj=son()
obj.house()
obj.car()
obj.bike()