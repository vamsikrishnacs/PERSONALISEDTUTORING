import csv
import sys
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

f8=open("grades-user",'r')
csv8=csv.reader(f8,delimiter='\t')


f9=open("perproblemuser",'r')
csv9=csv.reader(f9,delimiter=',')

f10=open("usercountp",'r')
csv10=csv.reader(f10,delimiter=' ')

f11=open("perweekuser",'r')
csv11=csv.reader(f11,delimiter=',')

f12=open("usercount",'r')
csv12=csv.reader(f12,delimiter=' ')





        
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
	

for line8 in csv8:
	testdict[line8[0]].append([line8[1],line8[2],line8[3],line8[4],line8[5],line8[6],line8[7],line8[8],line8[9],line8[10]])


for line9 in csv9:
	if(len(line9)>1):
		
		testdict[line9[0]].append(line9[1])

for line10 in csv10:
	

	testdict[line10[0]].append(line10[1])

for line11 in csv11:
	if(len(line11)>1):
		testdict[line11[0]].append(line11[1])


for line12 in csv12:
	
	testdict[line12[0]].append(line12[1])



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


















	

