import numpy as np

q=np.array((2,3,5))
q=np.zeros((2,3,5))
q[:,:,(1,4)]=1
c=q.sum(axis=1)
print q.shape

a=np.array((2,3))
b=np.array((2,2))
a=np.zeros((2,3))
b=np.zeros((2,2))


a[1,:]=1
b[:,1]=1
a[0,0]=1
b[1,0]=2
print a
print b
print np.sum(a,axis=0)

print c
print "start"
def hello():
	print "hello"
	for i in range(2,10):
		print i
	print "hi"

l=["s1","s2","asi",3]
hello()
print l[1:10]
l.append(4)
print l
for i in l:
	print i
p=[]
p=["12345","212"]
def dictionary():
	print "i'm dictionary"
	d={1:2,2:"asa"}
	p[0]="1234"
	print p
	print d[1]

dictionary()
