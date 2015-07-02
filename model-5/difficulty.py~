import csv
from collections import defaultdict

f1=open("grades-problem",'r')
csv1=csv.reader(f1,delimiter='\t')


mx=0
mx1=0
temp=[]

for line in csv1:
	temp.append(line)
	count=float(line[1])
	mx=max(count,mx)
	at=float(line[6])
	mx1=max(at,mx1)
#print mx,mx1

#print len(temp)
#print temp[39]
	
for line in temp:
	dif=0.0
	count=(float(line[1])/mx)
		
	grade=float(line[4])
	totalgrade=float(line[5])
	
	percent=grade/totalgrade

	attemptfactor=float(line[6])
	normfactor=attemptfactor/mx1
	dif=count*percent*normfactor
		
	print line[0],dif

