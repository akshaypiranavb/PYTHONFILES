from abc import ABC,abstractmethod
class bank(ABC):
    @abstractmethod
    def loan(self): pass
    @abstractmethod
    def credit(self):pass
class canara(bank):
    def loan(self):
        print("LOAN WILL PROVIDE BY CANARA")
    def credit(self):
        print("CANARA PROVOIDE CREDIT")
obj=canara()
obj.loan()
obj.credit()