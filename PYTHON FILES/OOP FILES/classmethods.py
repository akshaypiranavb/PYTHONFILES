class akshay:
    name="AKSHAY"
    age=19
    def show():
        print("NAME : ",akshay.name)
        print("AGE : ",akshay.age)
akshay.show()
print(getattr(akshay,"show"))
getattr(akshay,"show")()
print(akshay.__dict__)
akshay.__dict__["show"]()