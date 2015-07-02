import numpy as np

a=np.zeros((2,3,4))

a[0,0,:]=[1,2,3,4]
a[1,0,:]=[9,8,7,6]
a[0,2,:]=[1,1,1,0]
a[1,2,:]=[3,6,5,1]
print a
b=np.array([2,2,1])
print np.sum(a,2)/b
