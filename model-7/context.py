import csv
import sys
from collections import defaultdict
temp=[]
f1=open("difficult",'r')
csv1=csv.reader(f1,delimiter=' ')

f2=open("finalcountusers",'r')
csv2=csv.reader(f2,delimiter=' ')


f3=open("grade-attempts-time-user-id",'r')
csv3=csv.reader(f3,delimiter='\t')

f4=open("usernamesp",'r')
csv4=csv.reader(f4,delimiter='\t')


f5=open("grades1111",'r')
csv5=csv.reader(f5,delimiter='\t')


f6=open("grades-problem",'r')
csv6=csv.reader(f6,delimiter='\t')

f7=open("perproblem",'r')
csv7=csv.reader(f7,delimiter=',')

f8=open("problemcount",'r')
csv8=csv.reader(f8,delimiter=' ')


f9=open("time.csv",'r')
csv9=csv.reader(f9,delimiter='\t')


for line1 in csv4:
	temp.append(line1[0])
#print temp

temp2=[]
temp3=[]
for line7 in csv7:
	
	temp2.append(line7[0])
	temp3.append(line7)
print len(temp)
print len(temp2)       
testdict=defaultdict(dict)


for line1 in csv1:
	#print line1[0]
	#if(testdict[line2[0]]=='null'):
	#	print "error"
	for i in temp:
		#print i
		testdict[i][line1[0]]=[line1[1]]


for line1 in csv6:
	res=float(line1[4])/float(line1[5])
	#if(testdict[line2[0]]=='null'):
	#	print "error"
	for i in temp:
		#print i
		testdict[i][line1[0]].append(res)

for line1 in temp3:
	#print line1,":"
	for i in temp:
		try:
			testdict[i][line1[0]].append(line1[1])

		except:
			pass
	

for line1 in csv8:
	for i in temp:
		#print i
		try:		
			testdict[i][line1[0]].append(line1[1])
		except:
			pass

for line1 in csv9:
	try:
		testdict[line1[0]][line1[1]].append(line1[2])
	except:
		pass


for line1 in csv3:
	l1=float(line1[6])
	l2=float(line1[7])
	res=l1/l2
	try:
		if(res>=0.6):
			testdict[line1[0]][line1[1]].append('1')
			testdict[line1[0]][line1[1]].append(line1[2])
		else:
			testdict[line1[0]][line1[1]].append('0')
			testdict[line1[0]][line1[1]].append(line1[2])
	except:
		pass


for line1 in csv2:
	for i in temp2:
		#print i
		try:		
			testdict[line1[0]][i].append(line1[1])
		except:
			pass


for line1 in csv5:
	for i in temp2:
		#print i

		res=float(line1[1])/float(line1[2])
		try:		
			testdict[line1[0]][i].append(res)
		except:
			pass


for i in testdict.keys():
	print i	
	for j in testdict[i].keys():
		
		if(len(testdict[i][j])>6):
			print j,testdict[i][j]
		



'''    
for line2 in csv2:
	#print line2
	#if(testdict[line2[0]]=='null'):
	#	print "error"
	

	testdict[line2[0]].append([line2[1],line2[2],line2[3]])

'''



print testdict['ShubhamYewalekar']['21650f8821bc46dc94c2ff65d8965649']

print len(testdict)

'''





for line5 in csv5:
	
	testdict[line5[0]].append(line5[1])











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
	if(t==12):
		j=j+1
		print testdict[i],i
		#print testdict[i][0][1]+'\t'+testdict[i][1][1]+'\t'+testdict[i][2]+'\t'+testdict[i][3]+'\t'+testdict[i][4]+'\t'+testdict[i][5]+'\t'+testdict[i][7][0]+'\t'+str(float(testdict[i][7][3])/float(testdict[i][7][4]))+'\t'+testdict[i][7][6]+'\t'+testdict[i][8]+'\t'+testdict[i][9]+'\t'+testdict[i][10]+'\t'+testdict[i][11]

print j

#for i in testdict.keys():

	#print testdict[i]
#print len(testdict)
'''

















	

