import pandas as pd


file=pd.read_csv("dirtydata.csv")
print(file)
c=file.duplicated()
print(c)
file.drop_duplicates(inplace=True)
print(file)