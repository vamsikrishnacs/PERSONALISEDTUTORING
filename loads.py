import numpy
import csv
from datetime import timedelta
from datetime import datetime
fp=open("videomaxload.csv",'r')
csv1=csv.reader(fp,delimiter='\t')
#for i in fp:

#f=open("seektimesum.csv",'r')

#csv2=csv.reader(f,delimiter='\t')

i=0
#for row in csv1:
#	print row


f=open("usernamevideominmax.csv",'r')
csv2=csv.reader(f,delimiter='\t')	
#for row in csvf:
#        print row


fw=open("durationtest1.csv",'w')
i=0
for line2 in csv2:
	#w.write(line2[0]+'\t'+line1[0]+'\t'+line2[3]+'\t'+line2[2]+'\n')
	#print line2[0],line2[3],line2[2]
	c=line2[3].split()
	c1=line2[2].split()
	FMT = '%H:%M:%S'
	tdelta = datetime.strptime(c[1], FMT) - datetime.strptime(c1[1], FMT)
	#hen = datetime.fromtimestamp(line2[2])
	#print then
	if tdelta.days < 0:
    		tdelta = timedelta(days=0,seconds=tdelta.seconds, microseconds=tdelta.microseconds)
	#rint tdelta
	
	if c1[0]==c[0]:
		print line2,tdelta.seconds
		fw.write(line2[0]+'\t'+line2[1]+'\t'+str(tdelta.seconds)+'\n')
	#if c1[0]!=c[0]:
	#	print tdelta
	#	print line2[0],line2[2],line2[3]
		i=i+1

print i
