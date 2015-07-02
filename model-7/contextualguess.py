import numpy as np

plearn=0.5
guess=0.3
slip=0.2
transit=0.4

#4parameters plus action1,action2

paction12L=np.zeros((2,2))

paction12L[0,0]=guess*guess
paction12L[0,1]=guess*(1-slip)
paction12L[1,0]=guess*(1-slip)
paction12L[1,1]=(1-slip)*(1-slip)


notpaction12L=np.zeros((2,2))
notpaction12L[0,0]=transit*(slip)*(slip)+(1-transit)*transit*(1-guess)*(slip)+(1-transit)*(1-transit)*(1-guess)*(1-guess)
notpaction12L[0,1]=transit*(slip)*(1-slip)+(1-transit)*transit*(1-guess)*(1-slip)+(1-transit)*(1-transit)*(1-guess)*guess
notpaction12L[1,0]=transit*(1-slip)*slip+(1-transit)*transit*guess*(slip)+(1-transit)*(1-transit)*guess*(1-guess)
notpaction12L[1,1]=transit*(1-slip)*(1-slip)+(1-transit)*transit*guess*(1-slip)+(1-transit)*(1-transit)*guess*guess




def label(res1,res2):
	print res1,res2
	paction12=plearn*paction12L[res1,res2]+(1-plearn)*notpaction12L[res1,res2]
	print paction12
	#final p(Ln|a+1+2)
	finalprob=(paction12L[res1,res2]*plearn)/paction12
	return finalprob


print label(0,0)
#guess_prob=1-plearn1
