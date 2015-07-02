import numpy as np


fd=open("datafile.txt","rw+")
str=fd.readline()
print str
s=str.split()
print s


str1=fd.readline()
s1=str1.split()
arr=np.zeros((2,4))

arr[0,:]=s
arr[1,:]=s1
print arr

l=[1,0,1,0]
lev1=np.zeros(4)
lev1[:]=1



print lev1
mask=(l==lev1)
print mask


a=np.array((2,3))
a=np.zeros((2,3))

a[:,0]=1
a[1,:]=2
a[1,1]=3

print a

print np.sum(a,axis=0)




