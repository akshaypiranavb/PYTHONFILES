import pandas as pd

file=pd.read_csv("data.csv")
print(file)

file1=file.to_string()
print(file1)

print(type(file),type(file1))

print(file.head(18))
print(file.head())
print(file.tail(8))
print(file.tail())

#JSON FILE
print("-------------------------------------------------------------------------")
file2=pd.read_json("opendata.json")
print(file2)
print(file2.to_string())
print(file2.head())
print(file2.tail())
print(file.info())