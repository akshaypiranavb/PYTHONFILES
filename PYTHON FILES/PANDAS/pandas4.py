import pandas as pd
file=pd.read_csv("dirtydata.csv")
print(file)
# x=file.mean()
# file.fillna(x,inplace=True)
# print(file)
print("--------------------------")
# x=file.median()
# file.fillna(x,inplace=True)
# print(file)
# x=file["Calories"].mode()[0]#engalam nan oh antha edathulam .mode() oda value based on calories
# file.fillna(x,inplace=True)
# print(file)
file["Date"]=pd.to_datetime(file["Date"])
print(file)
file.dropna(subset=["Date"],inplace=True)
print(file)
for i in file.index:
    if file.loc[i,"Duration"] >120 :
        file.loc[i,"Duration"]=120
print(file)