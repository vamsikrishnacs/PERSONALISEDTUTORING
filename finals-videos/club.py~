import numpy
import csv

f1=open("seektimesumavgcount.csv",'r')
csv1=csv.reader(f1,delimiter='\t')
#for i in fp:

#f=open("seektimesum.csv",'r')

#csv2=csv.reader(f,delimiter='\t')

i=0
#for row in csv:
#	print row


f2=open("seeksavgcount.csv",'r')
csv2=csv.reader(f2,delimiter='\t')

f3=open("finalcount.csv",'r')
csv3=csv.reader(f3,delimiter=' ')

f4=open("finalduration.csv",'r')
csv4=csv.reader(f4,delimiter=',')

f5=open("finalloadcount.csv",'r')
csv5=csv.reader(f5,delimiter=' ')

f6=open("finalloadduration.csv",'r')
csv6=csv.reader(f6,delimiter=',')

f7=open("userspervideo1.csv",'r')
csv7=csv.reader(f7,delimiter='\t')
	
#for row in csv1:
#        print row

fw=open("clutserfinal.csv",'w')

for line1,line2,line3,line4,line5,line6,line7 in zip(csv1, csv2,csv3,csv4,csv5,csv6,csv7):
	#print line1[1],line1[2],line2[1],line3[1],line4[1],line5[1],line6[1],line7[1]
	
	fw.write(line1[1]+'\t'+line1[2]+'\t'+line2[1]+'\t'+line3[1]+'\t'+line4[1]+'\t'+line5[1]+'\t'+line6[1]+'\t'+line7[1]+'\n')
