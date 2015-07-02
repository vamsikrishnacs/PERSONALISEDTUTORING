import numpy as np
import csv

fp=open("duration.csv",'r')
csv1=csv.reader(fp,delimiter='\t')
i=0
a=[]

temp=[]

for row in csv1:
	temp.append(row)
	a.append(row[1])
	i=i+1
s=set(a)

d=dict(s)
print len(temp)
for row in temp:
        print row[0]
        
        i=i+1

print len(s)


