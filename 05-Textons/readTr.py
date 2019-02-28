#!/bin/python
from cifar10 import load_cifar10
Train = load_cifar10(meta='cifar-10-batches-py', mode=1)

TrainImages= Train['data']  
Anot= Train ['labels']

import pickle
from PIL import Image
from skimage import color
from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy
import numpy as np

TrImGr=numpy.zeros((10000,32,32))


for i in range(0,10000):
    temp= TrainImages[i,:,:,:]
    temp=color.rgb2gray(temp)
    TrImGr[i]= temp
    
clase=0
indx1=0
indx2=0
count=0
TrFinal=numpy.zeros((5000,32,32))
AnotFinal= numpy.zeros((5000))

while clase < 10:
    
    tf= Anot[indx1]==clase
    
    if tf==1:
        
        TrFinal[indx2]=TrImGr[indx1]
        AnotFinal[indx2]=Anot[indx1]
        indx2=indx2+1
        count= count+1
        
        
    if count==500:
        clase=clase+1
        count=0
        indx1=0
    
    indx1=indx1+1
    
with open('TrainingSet', 'wb') as f:
    pickle.dump(TrFinal, f)
    
with open('Anotaciones', 'wb') as f:
    pickle.dump(AnotFinal, f)
    
#with open('TrainingSet', 'rb') as f:
#    TrSet= pickle.load(f)


#plt.imshow(Image.fromarray(TrFinal[4999,:,:]))
#plt.show()
    

