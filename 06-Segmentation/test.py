#!/usr/bin/env python3
import seg
from seg import segmentByClustering
import os
from os import listdir
import cv2
import numpy as np
from evaluacion import evaluation
import matplotlib.pyplot as plt

main='./BSDS_small/train/'
dir= os.listdir(main)

count=1
count1=2
presMat= np.zeros((20,14))
cobMat= np.zeros ((20,14)) 

for im in range(1,21):
    indx=0
    for k in range(2,16):
        
        path= main+ dir[count1] 
        pathim= main+ dir[count]
        rgbImage= cv2.imread(pathim)
        pred= segmentByClustering (rgbImage, "rgb+xy", "kmeans" , k )
        pres, cob = evaluation (pred,path)
        presMat[im-1,indx]=pres
        cobMat[im-1,indx]= cob
        indx=indx+1
        
    count= count+2
    count1= count1+2



    
    
