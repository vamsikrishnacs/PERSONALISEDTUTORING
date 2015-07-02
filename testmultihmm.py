import numpy as np
from copy import copy
#import matplotlib.pyplot as plt

class HMM:
    def __init__(self):
        pass

    def simulate(self,nSteps):

        def drawFrom(probs):
            return np.where(np.random.multinomial(1,probs) == 1)[0][0]

        observations = np.zeros(nSteps)
        states = np.zeros(nSteps)
        states[0] = drawFrom(self.pi)
        observations[0] = drawFrom(self.B[states[0],:])
        for t in range(1,nSteps):
            states[t] = drawFrom(self.A[states[t-1],:])
            observations[t] = drawFrom(self.B[states[t],:])
	#print observations,states.shape
	#obs=np.zeros(nSteps)
	#obs[:]=[0,1,1,0,1,1,1,0,1,0]
	#print obs.shape
        return observations,states


    def evaluate(self,observations):

	print self.pi
	print self.A
	print self.B
	nStates = self.A.shape[0]
        nSamples = len(observations)
    	alpha = np.zeros((nStates,nSamples))
	pi = copy(self.pi)
	    #print observations[2]
        c = np.zeros(nSamples) #scale factors
        alpha[:,0] = pi.T * self.B[:,observations[0]]
        #c[0] = 1.0/np.sum(alpha[:,0])
        #alpha[:,0] = c[0] * alpha[:,0]
            # Update alpha for each observation step
        for t in range(1,nSamples):

        	alpha[:,t] = np.dot(alpha[:,t-1].T, self.A).T * self.B[:,observations[t]]
        	#c[t] = 1.0/np.sum(alpha[:,t])
                #alpha[:,t] = c[t] * alpha[:,t]
	print ""
	print alpha
	#c = 1.0/np.sum(alpha[:,nSamples-1])
	#alpha[:,nSamples-1] = c* alpha[:,nSamples-1]
	#res=0.0	
	#for j in range(nSamples):
	#res=1.0/np.product(c)
	#print res	
	print np.sum(alpha[:,nSamples-1])


    def train(self,observations,criterion,graphics=False):
        #if graphics:
        #    plt.ion()

	observations=np.zeros((3,11))
	#observations[:]=[0,0,1,0,1,1,1,0,1,0]
	observations[0,:]=[1,1,1,1,1,1,1,0,0,0,1]
	observations[1,:]=[1,1,1,1,1,1,1,0,1,0,1]
	observations[2,:]=[1,1,1,1,1,1,1,0,0,0,1]
	#observations[:]=[0,1,1,0,1,1,1,0,1,0]
	#observations[:]=[0,1,1,0,1,1,1,0,1,0]
	#observations[:]=[0,1,1,0,1,1,1,0,1,0]
        print observations.shape
        nStates = self.A.shape[0]
        nSamples = len(observations[0])
	#print nStates,nSamples
	print nStates,nSamples,len(observations)
        A = self.A  
        B = self.B
        pi = copy(self.pi)
	print A
	print B,pi        

	
        done = False
        while not done:

	    
            # alpha_t(i) = P(O_1 O_2 ... O_t, q_t = S_i | hmm)
            # Initialize alpha
	    xi = np.zeros((len(observations),nStates,nStates,nSamples-1));
	    tempnum=0.0
	    tempden=0.0
	    obsnum=copy(B)
	    obsden=0.0
	    obsnum[:,:]=0
	    for k in range(len(observations)):

          	
	    	print k,observations[k]
            	alpha = np.zeros((nStates,nSamples))
	    	#print observations[2]
            	c = np.zeros(nSamples) #scale factors
            	alpha[:,0] = pi.T * self.B[:,observations[k][0]]
            	c[0] = 1.0/np.sum(alpha[:,0])
            	alpha[:,0] = c[0] * alpha[:,0]
            # Update alpha for each observation step
            	for t in range(1,nSamples):

                	alpha[:,t] = np.dot(alpha[:,t-1].T, self.A).T * self.B[:,observations[k][t]]
                	c[t] = 1.0/np.sum(alpha[:,t])
                	alpha[:,t] = c[t] * alpha[:,t]

	    #print alpha
            # beta_t(i) = P(O_t+1 O_t+2 ... O_T | q_t = S_i , hmm)
            # Initialize beta
	            	beta = np.zeros((nStates,nSamples))
            		beta[:,nSamples-1] = 1
            		beta[:,nSamples-1] = c[nSamples-1] * beta[:,nSamples-1]
	    #print beta
            # Update beta backwards from end of sequence
            	for t in range(len(observations[0])-1,0,-1):
                	beta[:,t-1] = np.dot(self.A, (self.B[:,observations[k][t]] * beta[:,t]))
                	beta[:,t-1] = c[t-1] * beta[:,t-1]

	    #print beta
            	
            	for t in range(nSamples-1):
                	denom = np.dot(np.dot(alpha[:,t].T, self.A) * self.B[:,observations[k][t+1]].T,
                               beta[:,t+1])
                	for i in range(nStates):
                    		numer = alpha[i,t] * self.A[i,:] * self.B[:,observations[k][t+1]].T * \
                            beta[:,t+1].T
	                	xi[k,i,:,t] = numer / denom
  
	    	#print xi
            #raw_input("k")
            # gamma_t(i) = P(q_t = S_i | O, hmm)
		gamma=np.zeros((len(observations),2,nSamples))
		#print gamma.shape            	
		gamma1 = np.squeeze(np.sum(xi,axis=2))
 		print " "
                
            # Need final gamma element for new B
                gamma[:,:,:-1]=gamma1
		
		prod=(alpha[:,nSamples-1] * beta[:,nSamples-1]).reshape((-1,1))
		
		gamma[k]= np.hstack((gamma1[k],  prod / np.sum(prod))) #append one more to gamma!!!
	  	#print gamma

            	newpi = gamma[k][:,0]
		
		newA = np.sum(xi[k],2) / np.sum(gamma[k][:,:-1],axis=1).reshape((-1,1))
		tempnum+=np.sum(xi[k],2)
		#print np.sum(xi[k],2)	    	
		#print tempnum
		tempden+=np.sum(gamma[k][:,:-1],axis=1).reshape((-1,1))		
    		print self.A		
		print newA             	
		newB = copy(B)

	        #print gamma[k]
		#mask1 = observations[0] == 0
		#print mask1,np.sum(gamma[:,mask1],axis=1)
		
            	numLevels = self.B.shape[1]
		
            	sumgamma = np.sum(gamma[k],axis=1)
		obsden+=sumgamma
		#print "sumgamma"
		#print sumgamma,obsden            	
		for lev in range(numLevels):
                	mask = observations[k] == lev
			#print mask,np.sum(gamma[k][:,mask],axis=1).shape
                	newB[:,lev] = np.sum(gamma[k][:,mask],axis=1) / sumgamma
			obsnum[:,lev]+=np.sum(gamma[k][:,mask],axis=1)
			#print np.sum(gamma[k][:,mask],axis=1),obsnum
	
		
            	if np.max(abs(pi - newpi)) < criterion and \
                   np.max(abs(A - newA)) < criterion and \
                   np.max(abs(B - newB)) < criterion:
                	done = 1;
  
            	#A[:],B[:],pi[:] = newA,newB,newpi
	    #print gamma
	    print "gamma"
	    print "calcualtions at end"
	    #print gamma.shape
	    #print tempnum.shape
	    #print tempden.shape
	    news=tempnum/tempden
	    print news
	    #print obsnum
	    #print obsden
	    news1=obsnum/obsden.reshape(-1,1)
            if np.max(abs(pi - newpi)) < criterion and \
                   np.max(abs(A - news)) < criterion and \
                   np.max(abs(B - news1)) < criterion:
                	done = 1;
	    A[:],B[:],pi[:]=news,news1,newpi
	
	    print"update"
		

        self.A[:] = news
        self.B[:] = news1
        self.pi[:] = newpi
        self.gamma = gamma
        

if __name__ == '__main__':
    np.set_printoptions(precision=3,suppress=True)
    if True:
        #'Two states, three possible observations in a state'

        hmm = HMM()
        hmm.pi = np.array([0.85, 0.15])
        hmm.A = np.array([[0.85, 0.15],
                          [0.3, 0.7]])
       # hmm.B = np.array([[0.8, 0.1, 0.1],
        #                  [0.0, 0.0, 1]])

	hmm.B=np.array([[0.8, 0.2],
                        [0.0, 0.1]])


	#hmm.B = np.array([[0.8, 0.1, 0.1],


        hmmguess = HMM()
        hmmguess.pi = np.array([0.8, 0.2])
        hmmguess.A = np.array([[0.5, 0.5],
                               [0.7, 0.3]])

	hmmguess.B=np.array([[0.65, 0.35],
         	              [0.5, 0.5]])
        #hmmguess.B = np.array([[0.3, 0.3, 0.4],
        #                       [0.2, 0.5, 0.3]])
    else:
        #three states
        print "Error....this example with three states is not working correctly."
        hmm = HMM()
        hmm.pi = np.array([0.1, 0.4, 0.5])
        hmm.A = np.array([[0.7, 0.2, 0.1],
                          [0.1, 0.6, 0.3],
                          [0.4, 0.2, 0.4]])
        hmm.B = np.array([[0.5, 0.3, 0.2],
                          [0.1, 0.6, 0.3],
                          [0.0, 0.3, 0.7]])
        hmmguess = HMM()
        hmmguess.pi = np.array([0.333, 0.333, 0.333])
        hmmguess.A = np.array([[0.3333, 0.3333, 0.3333],
                               [0.3333, 0.3333, 0.3333],
                               [0.3333, 0.3333, 0.3333]])
        hmmguess.B = np.array([[0.3, 0.3, 0.4],
                               [0.2, 0.5, 0.3],
                               [0.3, 0.3, 0.4]])

    o,s = hmm.simulate(11)
    print o
    hmmguess.train(o,0.0001,graphics=True)
    print "evaluate"
    hmmguess.evaluate(np.array([0,0,1,0]))
    print 'Actual probabilities\n',hmm.pi
    print 'Estimated initial probabilities\n',hmmguess.pi

    print 'Actual state transition probabililities\n',hmm.A
    print 'Estimated state transition probabililities\n',hmmguess.A

    print 'Actual observation probabililities\n',hmm.B
    print 'Estimated observation probabililities\n',hmmguess.B
'''
    plt.subplot(2,1,2)
    plt.cla()
    plt.plot(np.vstack((s*0.9+0.05,hmmguess.gamma[1,:])).T,'-o',alpha=0.7)
    plt.legend(('True State','Guessed Probability of State=1'))
    plt.ylim(-0.1,1.1)
    plt.xlabel('Time')
    plt.draw()
'''



