import numpy as np
import csv
import matplotlib.pyplot as plt
from numpy.random import normal





fp=open("perproblem",'r')
csv1=csv.reader(fp,delimiter=',')
#for i in fp:
start=[]
end=[]
end1=[]
for row in csv1:
	#print row
	
	start.append(float(row[1]))
	end.append(row[0])
	
print len(start)
print len(end)


#f=open("seektimesum.csv",'r')

#csv2=csv.reader(f,delimiter='\t')
'''
start=[]
end=[]
last=[]
i=0
count=np.array(12)
for row in csv1:
	#print row[2]
	if float(row[2])>1.0 and float(row[2])<=2.0:
		i=i+1
		print row[2]
	start.append(float(row[2]))
	end.append(float(row[3]))
        last.append(abs(float(row[4])))
l=max(start),max(end)
print i


plt.hist(start, bins=15, histtype='step', color='b', label='Gaussian')
plt.hist(end, bins=15, histtype='step', color='r', alpha=1, label='Uniform')
#plt.hist(last, bins=15, histtype='step', color='y', alpha=0.7, label='Uniform')
st=[1,1,1,2,2,2,2,3,4,5,9]
n=np.array(start)
print np.bincount(start,minlength=15)
print np.histogram(start,bins=15,normed="true")	
'''
#plt.hist(start,bins=15)

#plt.hist(start, bins=10, histtype='step', color='b', label='Gaussian')
x = range(len(end))
print x
# Change of fontsize and angle of xticklabels
fig = plt.figure()
fig.clf()
ax = fig.add_subplot(111)

#ax.set_xlim(-1,100)
ax.yaxis.grid(True, linestyle='-', which='major', color='black', alpha=1)
	
plt.setp(ax.get_xticklabels(), fontsize=10, rotation='vertical')
plt.xticks(x, end)
plt.plot(x,start)
#plt.plot(x,end1)
#plt.plot(end,start)
plt.title("PROBLEM DURATION BY ID")
plt.ylabel("Total Duration(per user sum)")
plt.xlabel("prob-id")
plt.show()

