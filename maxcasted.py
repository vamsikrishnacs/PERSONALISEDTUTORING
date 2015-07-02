import numpy
import csv

fp=open("maxseektimecasted.csv",'r')
csvf=csv.reader(fp,delimiter='\t')
#for i in fp:
stri=fp.readline()
f=open("modified.csv",'w')
stri=stri.strip()
print stri[2]
a=[]
i=0
'''
for row in csvf:
	if row[3]!='NULL' and row[2]!='NULL':
		f.write(row[0]) 
		f.write('\t')
		f.write(row[1])
   		f.write('\t')
		f.write(str(max(float(row[2]),float(row[3]))))
		f.write('\n')
	elif row[3]=='NULL':
		f.write(row[0]) 
                f.write('\t')
		f.write(row[1])
  		f.write('\t')
		f.write(row[2])
		f.write('\n')
 
	else:
		f.write(row[0])                
                f.write(row[1])
                f.write(row[2])
                f.write('\n')
'''




for row in csvf:
	if row[3]!='NULL':
		if row[2]!='NULL':
			f.write(row[0]+'\t'+row[1]+'\t'+str(max(float(row[2]),float(row[3])))+'\n')
			i=i+1
		else:
			f.write(row[0]+'\t'+row[1]+'\t'+row[3]+'\n')
			i=i+1

print i 

