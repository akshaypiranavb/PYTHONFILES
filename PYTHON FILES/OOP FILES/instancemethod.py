class akshay():
    name="AKSHAY"
    age=19
    def show(ak,gender):
        print(akshay.name)
        print(akshay.age)
        print(gender)
obj=akshay()
obj.show("MALE")
akshay.show(obj,"MALE")
getattr(akshay,"show")(obj,"male")

        
        