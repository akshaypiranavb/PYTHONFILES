import pandas as pd
import matplotlib.pyplot as mp
try:
    file=pd.read_csv("akshay.csv")
    print(file)
    print(file.corr())
except :
    print("ERROR")

print(file.plot())
file.plot()
mp.show()