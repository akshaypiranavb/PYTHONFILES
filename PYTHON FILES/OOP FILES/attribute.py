class akshay():
    name="AKSHAY"
    age=18888
print(getattr(akshay,"name"))
print(getattr(akshay,"age"))
print(akshay.name)
print(akshay.age)
setattr(akshay,"name","ak")
print(akshay.name)
print(getattr(akshay,"name"))
akshay.oru="sattur"
print(akshay.oru)
print(getattr(akshay,"gender","content illa pa"))