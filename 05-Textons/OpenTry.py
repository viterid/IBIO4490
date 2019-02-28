#!/bin/python
import pickle
import numpy

with open('PruebaTextones1', 'rb') as f:
    TrSet= pickle.load(f)
print(type(TrSet))


