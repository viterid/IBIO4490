#!/usr/bin/env python3

def evaluation (pred,path):
    
	import scipy.io
	import cv2
	from matplotlib import pyplot as plt
	import numpy as np
    
	
	mat = scipy.io.loadmat(path)
    
	for i in range(1):
		gtruthtemp=mat['groundTruth'][0,i][0][0]['Segmentation']
		laplacian = cv2.Laplacian(gtruthtemp,cv2.CV_64F)  
		if i==0:
			gtruth=laplacian
		else: 
			gtruth = gtruth + laplacian
    
	laplacian = cv2.Laplacian(gtruth,cv2.CV_64F)  
	laplacian = laplacian!= 0
    
	gtruth =  laplacian*1
    
	
	pred = cv2.Laplacian(gtruthtemp,cv2.CV_64F)  
    
    
    
    #Presición 
	inte = (pred<gtruth)
	inte = inte*1
	inte=np.sum(inte)
	tot = gtruth+pred
	tot = tot*1
	tot=np.sum(tot)
    
	pres = inte/tot
    
    #Cobertura
	inte = (gtruth<pred)
	inte = inte*1
	inte=np.sum(inte)
	tot = gtruth+pred
	tot = tot*1
	tot=np.sum(tot)
    
	cob = inte/tot
    
	return pres, cob

