#Honey Singh
#Hw 2 question 3

from pylab import *
from numpy import *
import numpy, math, linreg,pcn_logic_eg


testset = np.array(loadtxt('prostate_data_test.txt',dtype=float))
print testset

trainset = np.array(loadtxt('prostate_data_train.txt', dtype = float))
print trainset

row,col= trainset.shape
print row, col

trainin_1 = trainset[:,0:4]
trainin_2 = trainset[:,5:col]
trainin = concatenate((trainin_1,trainin_2), axis = 1)
newrow, newcol = trainin.shape
print newrow, newcol
trainin = np.asmatrix(trainin)
traintgt = trainset[:,4]
traintgt = numpy.asmatrix(traintgt)

#testing
rowtest,coltest = testset.shape
print rowtest, coltest
testin_1 = testset[:,0:4]
testin_2 = testset[:,5:coltest]
testin = concatenate((testin_1,testin_2), axis = 1)
testin = np.asmatrix(testin)
testtgt = testset[:,4]

beta = linreg.linreg(trainin,traintgt)
testin = concatenate((testin,-ones((shape(testin)[0],1))),axis=1)
testout = dot(testin,beta)
testout = where(testout>0.5, 1,0)
print testout

error = 0
i= 0
while 1:
    error = error + (testout[i] - testtgt[i])**2
    i = i+1
    if i > 29:
        break
        
print error

#perceptron
p = pcn_logic_eg.pcn(trainin, traintgt)
weights = p.pcntrain(trainin, traintgt, 0.25, 10)
testoutput = p.pcnfwd(testin)
#testoutput = dot(testin, weights)
testoutput = where(testout>0.5, 1,0)

print testoutput


        
    
    
