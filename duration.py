import numpy
import csv

fp=open("modified.csv",'r')
csv1=csv.reader(fp,delimiter='\t')
#for i in fp:

#f=open("seektimesum.csv",'r')

#csv2=csv.reader(f,delimiter='\t')

i=0
#for row in csv1:
#	print row


f=open("seektimesum.csv",'r')
csv2=csv.reader(f,delimiter='\t')	
#for row in csvf:
#        print row

fw=open("duration.csv",'w')

for line1,line2 in zip(csv1, csv2):
	
	s=float(line1[2])-float(line2[2])
	fw.write(line1[0]+'\t'+line1[1]+'\t'+str(s)+'\n')
