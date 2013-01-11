from sklearn import svm
from Tools import *
from Domains import *
from Representations import *

logger = Logger()
D  = SystemAdministrator(logger=logger)
R  = IndependentDiscretizationCompactBinary(D,logger)

state = array([0]*D.state_space_dims)
D.printAll()
R.printAll()
print R.activeInitialFeatures(state)
print R.activeInitialFeaturesCompactBinary(state)
state2 = array([0]*D.state_space_dims)
state2[R.binary_dims] = 1
print R.activeInitialFeatures(state2)
print R.activeInitialFeaturesCompactBinary(state2)
