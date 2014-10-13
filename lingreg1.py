from numpy import *

def linreg1(inputs,targets):

	inputs = concatenate((inputs,-ones((shape(inputs)[0],1))),axis=1)
	beta = dot(dot(linalg.inv(dot(transpose(inputs),inputs)),transpose(inputs)),targets)
        #beta = dot(linalg.pinv(inputs),transpose(targets))
	outputs = dot(inputs,beta)
	#print shape(beta)
	#print outputs
	return beta