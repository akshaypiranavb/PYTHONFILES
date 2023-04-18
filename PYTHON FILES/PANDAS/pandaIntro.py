import pandas as pd
print(dir(pd))

x={
    "CARS" : ["BMW","AUDI","TATA"],
    "RANK" : [1,2,5]
}
print(x)
a=pd.DataFrame(x)
print(a)
print(type(a))
print(pd.__version__)

a=[1,2,3,4,5]
y=pd.Series(a)
print(a[2])
print(a[4])
# print(a[9])
z=pd.Series(a,index=[1,2,"AKSHAY","PIRANAV",5])
print(z["AKSHAY"])

c={
    "day1" : 200,
    "day2" : 300
}
dd=pd.Series(c)
print(dd)

ddd=pd.Series(c,index=["nal1","nal2"])
print(ddd)

ddd=pd.Series(c,index=["day1","day2"])
print(ddd)


xx={
    "CALORIE" : [20,300,22,111],
    "BP"      : [120,340,220,111]

}

print(x)

h=pd.DataFrame(xx)
print(h)

h=pd.DataFrame(xx,index=["c1","c4","c2","c3"])
print(h.loc["c1"])

# h=pd.DataFrame(xx,index=["c1","c4","c2","c3"])
# print(h.loc["c1","c2"])

h=pd.DataFrame(xx,index=["c1","c4","c2","c3"])
print(h.loc["c1"])
print(h.loc[["c1","c2"]])