
import numpy as np
los={}
nstudents=10
seed=0.1
los[0]=0.1
for i in range(1,nstudents):
	los[i]=los[i-1]+0.1

#los={1:"0.05"};
b = np.array([[0.4, 0.6],
	      [0.5, 0.5]])
a=np.array([[0.3,0.7],
	    [0.1,0.9]])
pi=np.array([0.85,0.15])

datapoints=[
		[3,[0,1,1,0],[3,1,2,1]],
		#[4,[1,0,1],[3,1,2]]
	   ]
print "hello"
print b[0][0]
print a[0][1]
print los[9]

print los.items()

class HMMmodel:
	
	criterion=0.0001	
	nstudents=0
	nresources=0
	dict={}	
	loIs={}
	tIr={}
	forwardlat=[]
	backwardlat=[]
	gammalat=[]
	epsilonlat=[]
	def __init__(self,nstudents,nresources,a,b,pi):
		self.nstudents=nstudents
		self.nresources=nresources
		self.a=a
		self.b=b
		self.pi=pi
		for i in range(self.nstudents):
			self.loIs[i]=0.2
		self.tIr[1]=0.7	
		for i in range(2,self.nresources):		
			self.tIr[i]=self.tIr[i-1]-0.1
				
		print self.tIr.items()
		print "class"

	def hello(self):
		print "class-hello"
		
		print self.nstudents


	def exp(self):
		print self.a
		print self.b
		print self.pi

	def initarrays(self):
		for i in range(self.nstudents):
			print i			
			self.dict[i]=a
			

	def hmmtrain(self,datapoints):
		for i in datapoints:
			ts=len(i[1])
			print ts
			print i[1]
			alphalat=np.zeros((2,ts))
			print alphalat
			print self.tIr.items()

                        #alpha calculation
			#alpha = np.zeros((nStates,nSamples))
           	        c = np.zeros(ts) #scale factors
            		alphalat[:,0] = pi.T * self.b[:,i[1][0]]
            		c[0] = 1.0/np.sum(alphalat[:,0])
            		#alphalat[:,0] = c[0] * alphalat[:,0]
           		 # Update alpha for each observation step
			#for r in range(self.nresources)            		:
			for t in range(1,ts):
				temp=self.tIr[i[2][t-1]]
				#print temp					
				self.a[0,0]=1-temp
			        self.a[0,1]=temp
				
                		alphalat[:,t] = np.dot(alphalat[:,t-1].T, self.a).T * self.b[:,i[1][t]]
                			#c[t] = 1.0/np.sum(alphalat[:,t])
                		#alphalat[:,t] = c[t] * alphalat[:,t]
				#print alphalat[:,0]
			print alphalat
      


			#beta calcuation
                        betalat = np.zeros((2,ts))
            		betalat[:,ts-1] = 1
            		#betalat[:,ts-1] = c[ts-1] * betalat[:,ts-1]
            		# Update beta backwards from end of sequence
            		for t in range(len(i[1])-1,0,-1):
				temp=self.tIr[i[2][t-1]]
				#print temp			
				#self.a=[[1-temp,temp],
				#	[0.1,0.9]]
				self.a[0,0]=1-temp
			        self.a[0,1]=temp
                		betalat[:,t-1] = np.dot(self.a, (self.b[:,i[1][t]] * betalat[:,t]))
                		#betalat[:,t-1] = c[t-1] * betalat[:,t-1]
			print betalat
						
                  
			res=self.nresources
           		xi = np.zeros((2,2,ts-1));
			#for r in range(res):            		
			for t in range(ts-1):
                		denom = np.dot(np.dot(alphalat[:,t].T, self.a) * self.b[:,i[1][t+1]].T,betalat[:,t+1])
                		for j in range(2):
					temp=self.tIr[i[2][t]]
					print temp,t,i[2][t]
				#self.a=[[1-temp,temp],
				#	[0.1,0.9]]
					#if(r==i[2][t-1]):						
					self.a[0,0]=1-temp
					self.a[0,1]=temp
					print a	
				
                   			numer = alphalat[j,t] * self.a[j,:]* self.b[:,i[1][t+1]].T * betalat[:,t+1].T
					print numer
					print denom			
					#else:
					#	numer=0                    				
					xi[j,:,t] = numer / denom
			print xi

			#gammacomps

			gammalat = np.squeeze(np.sum(xi,axis=1))
            		# Need final gamma element for new B
            		prod =  (alphalat[:,ts-1] * betalat[:,ts-1]).reshape((-1,1))
			#print gammalat

            		gammalat = np.hstack((gammalat,  prod / np.sum(prod))) #append one more to gamma!!!
			#print xi
			print gammalat

            		newpi = gammalat[:,0]

            		#newA = np.sum(xi,2) / np.sum(gammalat[:,:-1],axis=1).reshape((-1,1))

			temp=np.sum(xi,2)
			print temp

			newA=np.sum(gammalat[:,:-1],axis=1).reshape((-1,1))
			#print newA
			newB =np.copy(self.b)

            		numLevels = self.b.shape[1]
            		sumgamma = np.sum(gammalat,axis=1)

			#print sumgamma
            		for lev in range(numLevels):
                		mask = i[1]== lev
                		#newB[:,lev] = np.sum(gammalat[:,mask],axis=0) / sumgamma

			print newB


			

            		if np.max(abs(pi - newpi)) < 0.0001 and np.max(abs(a - newA)) < 0.0001 and np.max(abs(b - newB)) < 0.0001:
                		done = 1;


			


ar=np.array([1,2,3,4])


p=HMMmodel(5,5,a,b,pi)
p.hello()
p.exp()
p.initarrays()
print p.dict[1][0]
print p.loIs.items()
print p.tIr.items()
p.hmmtrain(datapoints)







