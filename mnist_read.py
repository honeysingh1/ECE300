#Honey Singh
#Hw 2 No 1

from numpy import *
from pylab import *
import cPickle, gzip, numpy, pylab
import linreg
# Load the dataset
f = gzip.open('mnist.pkl.gz', 'rb')

train_set, valid_set, test_set = np.array(cPickle.load(f))


#training
input_train = train_set[0]
trainin = input_train[0:2000,:]
target_train = train_set[1]
traintgt = target_train[0:2000]
traintgt =numpy.asmatrix(traintgt)

#testing
testinput = test_set[0]
newtestinput = testinput[0:2000,:]
testout = test_set[1]
newtesttarget = testout[0:2000,]
newtesttarget = numpy.asmatrix(newtesttarget)

beta = linreg.linreg(trainin, traintgt)
newtestinput = concatenate((newtestinput, -ones((shape(newtestinput)[0],1))), axis=1)
newtestoutput = dot(newtestinput, beta)
print newtestoutput

error = sum((newtestoutput-newtesttarget)**2)

print error

f.close()