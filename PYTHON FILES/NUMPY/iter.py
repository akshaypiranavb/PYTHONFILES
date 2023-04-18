import numpy as np
a=np.array([[1,2,3],[2,3,4]])
print(a)
for x in a:
    print(x)
for x in a:
    for y in x:
        print(y)
for x in np.nditer(a,flags=[("buffered")],op_dtypes=["S"]):
    print(x)
for x in np.ndenumerate(a):
    print(x)
for id,x in np.ndenumerate(a):
    print(id,x)