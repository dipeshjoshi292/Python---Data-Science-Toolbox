import numpy as np
'''
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[10,9,8],[7,6,5]])
print(a)
print(b)
print("addition:",a+b)
print("subtraction:",a-b)
print("division:",a/b)
print("multiplication:",a*b)
print("floor:",a//b)
print("exponent:",a**b)
aa=np.array([[1,2],[3,4]])
bb=np.array([[7,8],[9,10]])
matrix=np.dot(aa,bb)
print("matrix:",matrix)
'''
'''
#n dimension arrange function using reshape
b= np.arange(12).reshape(3,4)
print(b)
'''
'''
m=np.array([20,-3,17,44])
#conditional
print(m<[12,3,4,55])
print(m<25)
#to get element below 25
print(m[m<25])
'''
'''
a=np.array([[-2.5,3,4.1],[12,11,13]])
print(a)
print(type(a))
print("mean:",a.mean())
print("min:",a.min())
print("max:",a.max())
print("sum:",a.sum())
print("std:",a.std())
print("var:",a.var())
print("product:",a.prod())

b=np.arange(12).reshape(3,4)
print(b)
print("sum across columns:",b.sum(axis=0)) #axis=0 for columns.
print("min across the row:",b.min(axis=1)) #axis=1 for the rows.
print("cumulative sum:",b.cumsum(axis=1))

print("Transpose:",b.T) #Transpose
#also .copy()
'''
import pandas as pd
s=pd.Series([1,2,-999,0])
print(s)
print(np.square(s)) #pass as parameter to NumPy
a=s+[1000,2000,3000,4000] #Arithmetic operation
print(a)
print(s+1000) #Broadcasting
print(s<0) #conditional operations




























