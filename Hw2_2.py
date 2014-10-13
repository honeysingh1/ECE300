# Code from Chapter 2 of Machine Learning: An Algorithmic Perspective
# by Stephen Marsland (http://seat.massey.ac.nz/personal/s.r.marsland/MLBook.html)

# You are free to use, change, or redistribute the code in any way you wish for
# non-commercial purposes, but please maintain the name of the original author.
# This code comes with no warranty of any kind.

# Stephen Marsland, 2008

# This is the start of a script for you to complete

#Honey Singh
#Hw 02 Question 2

from pylab import *
from numpy import *
import linreg
#import itertools

auto = np.array(loadtxt('auto_mpg.txt', comments='"',dtype=float))
# Separate the data into training and testing sets
row, col = auto.shape
print row
print col
randnumb = random.randint(0,392,392)
inputs = auto[:, 0:col-1]
target = auto[:, col-1]

b = arange(0,196)
c = arange(196,392)

indtraining = randnumb[b]
indtest = randnumb[c]

trainin = inputs[indtraining]
traintgt = target[indtraining] 

testin = inputs[indtest]
testtgt = target[indtest]


# This is the training part
beta = linreg.linreg(trainin,traintgt)
testin = concatenate((testin,-ones((shape(testin)[0],1))),axis=1)
testout = dot(testin,beta)
error = sum((testout - testtgt)**2)
print error
plt.plot(testtgt)
plt.plot(testout,'ro')
plt.ylabel('test data')
plt.show()

