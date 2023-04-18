import numpy as np
a=np.array([1,2,3,4])
print(a.dtype)
b=np.array([1,4,5,6,7],dtype="S")
print(b.dtype)

c=np.array([1,2,3,4,5])
d=c.astype("S")
print(d.dtype)
e=np.array([1,2,3,4,5],dtype="i1")
print(e.dtype)
f=np.array([1,3,4,5],dtype=int)
print(f.dtype)
x=[1,2,3,4]
y=x
y[0]=1000
print(x)
t=np.array([1,2,3])
u=t
u[0]=1000
print(t)