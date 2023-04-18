import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(a)
print(a.shape)#2 array 6 ellements
print(a.reshape(6,2))
print(a.reshape(6,2).base)
print(a.reshape(2,2,-1))
b=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(b.reshape(-1))
