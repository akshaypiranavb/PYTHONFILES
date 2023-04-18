import pandas as pd
file=pd.read_csv("dirtydata.csv")
print(file)
file.fillna(1300,inplace=True)
print(file)
file.to_csv("akshay.csv")
file.to_json("akshay.json")