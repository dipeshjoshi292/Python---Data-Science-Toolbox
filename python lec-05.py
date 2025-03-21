import numpy as np
'''
#0d array
a=np.array([28])
print(a)
print(a.ndim)
'''
'''
#1d array
b=np.array([1,2,3])
print(b)
print(b.ndim)
'''
'''

#2d array and objects
c=np.array([[1,2,3],[4,5,6]])
print(c)
print(type(c))
print(c.ndim)
print(c.size)
print(c.shape)
print(c.dtype)
print(c.itemsize)
a=c.reshape(3,2)
print(a)
'''
'''
#3d array
d=np.array([[[1,2,3],[4,5,6]],[[5,6,7],[7,8,9]]])
print(d)
print(d.ndim)
print(d.shape)
print(d.size)
print(d[0,1,2])
'''
'''
#zeros
zero=np.zeros((2,5))
print(zero) 
'''
'''
#ones
ones=np.ones((2,2,2))5
print(ones)
print(ones.ndim)
'''
'''
#full
full=np.full((3,4),1.23)
print(full)

#range
w=np.arange(10,30,5) # 30 will not be included
print(w)
'''
'''
#line space
print(np.linspace(0,30,6)) # 30 will be included
'''
'''
a=np.linspace(10,30,5)
print(a)
b=np.arange(6)
print(b)
c=np.arange(1,6)
print(c)
'''
'''
d=np.linspace(1,6)
print(d)
'''






