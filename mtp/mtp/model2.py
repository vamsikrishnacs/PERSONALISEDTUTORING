import numpy as np

#from sklearn import *
from sklearn import datasets, linear_model

class linear_regressor:

	def __init__(self,n_features,n_points):
		print " "
		self.numpyarray(n_points,n_features)
		self.example()

	def numpyarray(self,n_points,n_features):


		data=np.zeros((n_points,n_features))
		#for i in datapoints:
		print data
		
		
	def fitfromfile(self):
		fd=open(datafile,"r")
		for i in fd.read():
			print i
			

	def example(self):
		
		

# Load the diabetes dataset
		diabetes = datasets.load_diabetes()

                #print diabetes.data[7,:]
# Use only one feature
		diabetes_X = diabetes.data[:, np.newaxis]
		diabetes_X_temp = diabetes_X[:, :, 2]

# Split the data into training/testing sets
		diabetes_X_train = diabetes_X_temp[:-20]
		diabetes_X_test = diabetes_X_temp[-20:]

# Split the targets into training/testing sets
		diabetes_y_train = diabetes.target[:-20]
		diabetes_y_test = diabetes.target[-20:]

# Create linear regression object
		regr = linear_model.LinearRegression()

		x_train=np.zeros((10,4))
		
		x_train[1,:]=[12,3,4,5]
		x_train[:,2]=5
		x_train[1,:]=[12,3,4,5]
		x_train[3,:]=[1,13,24,15]
		x_train[:,2]=11
		x_train[4,:]=[12,3,14,15]
		x_train[4,:]=[12,3,14,15]

		x_train[6,:]=[2,13,11,5]
		x_train[7,:]=[1,31,14,1]
		x_train[9,:]=[12,8,4,15]
		x_train[0,:]=[5,13,19,15]

		x_train[:,0]=2
		y_train=np.zeros((10,1))
		print x_train
		y_train[:,0]=[0.5,0.2,0.3,0.4,0.5,0.2,0.3,0.4,0.1,0.9]
		print y_train

# Train the model using the training sets
		#regr.fit(diabetes_X_train, diabetes_y_train)
		regr.fit(x_train, y_train)

		print regr.coef_


    

linear_regressor(2,3)
