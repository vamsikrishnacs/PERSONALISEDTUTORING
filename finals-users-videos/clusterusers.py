import csv
from collections import defaultdict

f1=open("seeksavgcountusers1",'r')
csv1=csv.reader(f1,delimiter='\t')

f2=open("seektimesumavgcountusers",'r')
csv2=csv.reader(f2,delimiter='\t')


f3=open("finaldurationusers",'r')
csv3=csv.reader(f3,delimiter=',')

f4=open("finalcountusers",'r')
csv4=csv.reader(f4,delimiter=' ')



f5=open("finalloadcountusers",'r')
csv5=csv.reader(f5,delimiter=' ')


f6=open("finalloaddurationusers",'r')
csv6=csv.reader(f6,delimiter=',')

f7=open("videosperusercount",'r')
csv7=csv.reader(f7,delimiter='\t')
'''
f3=open("finalloadcountusers",'r')
csv3=csv.reader(f3,delimiter=' ')

'''

testdict=defaultdict(list)


for line1 in csv1:
	#print line2
	#if(testdict[line2[0]]=='null'):
	#	print "error"
	

	testdict[line1[0]].append([line1[1],line1[2],line1[3]])

       
for line2 in csv2:
	#print line2
	#if(testdict[line2[0]]=='null'):
	#	print "error"
	

	testdict[line2[0]].append([line2[1],line2[2],line2[3]])

for line in csv3:
	
	testdict[line[0]].append(line[1])

for line4 in csv4:
	
	testdict[line4[0]].append(line4[1])


for line5 in csv5:
	
	testdict[line5[0]].append(line5[1])


for line6 in csv6:
	
	testdict[line6[0]].append(line6[1])


for line7 in csv7:
	testdict[line7[0]].append(line7[1])
	

#for line3 in csv3:
	#testdict.setdefault(key, [])

	#testdict[line3[0]].append(line3[1])
	#testdict[line3[0]].append(line3[1])



#	print lines
	
#print testdict['VeveritaIon']
#print testdict['zsarah001']
#print testdict
#print len(testdict)
#print testdict.keys()

j=0
for i in testdict.keys():

	t=len(testdict[i])
	if(t==3):
		j=j+1
		print testdict[i],i

print j
'''
for i in testdict.keys():

	print testdict[i]
'''
print len(testdict)



















	

