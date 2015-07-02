import numpy as np
import csv
from sklearn.cluster import KMeans



f=open("grades-problem",'r')

csv2=csv.reader(f,delimiter='\t')
temp=[]

for row in csv2:
	print row			
	#temp.append(row)

print len(temp)

def makecluster():

	n_points=6
	n_dim=2
	n_clusters=6
	model=KMeans(init='k-means++',n_clusters=4,n_init=10)
   
	data=np.zeros((16,2))
 	#print data
        #data1=np.array(temp)   
	data[0:4,:]=2
	data[4:8,:]=1
	data[8:12:,:]=-1
	data[12:16,:]=-2
	data[(0,4,8,12),1]=2
	data[(1,5,9,13),1]=1
	data[(2,6,10,14),1]=-1
	data[(3,7,11,15),1]=-2
	
	#data[3,1]=2
        #data[4,1]=3
	#data[5,1]=2
        #data[0,1]=3

	
	#model.fit(data1)
	print data1
	print model.labels_


makecluster()
