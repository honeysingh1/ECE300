
from numpy import *
import linreg
import pcn_logic_eg
"""THE XNOR perceptron"""
inputs = array([[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]])
targets = array([[1],[0],[0],[1],[0],[1],[1],[0]])

p = pcn_logic_eg.pcn(inputs,targets)
p.pcntrain(inputs,targets,0.25,10)

inputs1 = concatenate((inputs,-ones((shape(inputs)[0],1))),axis=1)

p= linreg.linreg(inputs,targets)

out = dot(inputs1, p)

print out
