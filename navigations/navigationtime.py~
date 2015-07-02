i=0
#for row in csv1:
#	print row
import numpy
import csv
from datetime import timedelta
from datetime import datetime

f=open("navigations",'r')
csv2=csv.reader(f,delimiter='\t')	



fw=open("ne_time.csv",'w')
i=0
for line2 in csv2:
	c=line2[3].split()
	c1=line2[2].split()

	FMT = '%H:%M:%S'
	tdelta = datetime.strptime(c[1], FMT) - datetime.strptime(c1[1], FMT)
	if tdelta.days < 0:
    		tdelta = timedelta(days=0,seconds=tdelta.seconds, microseconds=tdelta.microseconds)

	#print tdelta,tdelta.seconds

	
	if c1[0]==c[0]:
		#print line2, 
		print c,c1,tdelta,tdelta.seconds
		fw.write(line2[0]+'\t'+line2[1]+'\t'+str(tdelta.seconds)+'\n')
	#if c1[0]!=c[0]:
	#	print tdelta
	#	print line2[0],line2[2],line2[3]
		i=i+1

print i


