import csv

f1=open("timelines",'r')
csv1=csv.reader(f1,delimiter='\t')

data=[]
for row in csv1:
	data.append(row)

for i,j in zip(data,range(len(data))):
	#print j
	if i[3]=='problem_check': #or i[3]=='load_video':
		if i[9]=='/event':
			print i[3],i[9],i[12][38:70],i[10]
			print i
			ans=i[12][38:70]
		else:			
			print i[3],i[9][82:114],i[10]
			print i
			ans=i[9][82:114]			
		print " "
				
		c=data[j-15][10]
		d=data[j-10][10]
		e=data[j-5][10]
		f=data[j][10]
		#print ans,c,d,e,f
#		print data[j-10][3],data[j-10][10],data[j-9][3],data[j-8][3],data[j-7][3],data[j-6][3],data[j-5][3],data[j-4][3],data[j-3][3],data[j-2][3],data[j-1][3],data[j][3],data[j][10]
		

#for i in data:
	#print i[3],i[10]
	#if i[3]=='problem_check' or i[3]=='load_video':
	#print i[3],i[10]

print data[10]

