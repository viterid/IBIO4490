#!/bin/python

#Descraga las imágenes
from PIL import Image
import wget
import numpy
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
import cv2
import numpy as np,sys

#Dan
url='https://drive.google.com/uc?export=download&id=1fYmAo9yaGZARz0oK7ZTfMNAc-JkimN8l'
filename= wget.download(url)

#JF
url='https://drive.google.com/uc?export=download&id=15V849rgF5RHgELczk8l8awXHDqUC-bx_'
filename= wget.download(url)


#Reescalar las imágenes al mismo tamaño
Dan=Image.open('Dan.png',mode='r')
Dan=Dan.resize((512,512)) 
Dan.save('Dan.png')

JF=Image.open('JF.png',mode='r')
JF=JF.resize((512,512))
JF.save('JF.png') 


import numpy as np,sys
A = cv2.imread('Dan.png')
B = cv2.imread('JF.png')
# generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in range(1,6):
	G = cv2.pyrDown(G)
	gpA.append(G)

# generate Gaussian pyramid for B
G = B.copy()
gpB = [G]
for i in range(1,6):
	G = cv2.pyrDown(G)
	gpB.append(G)
# generate Laplacian Pyramid for A
lpA = [gpA[5]]
for i in range(5,0,-1):
	GE = cv2.pyrUp(gpA[i])
	L = cv2.subtract(gpA[i-1],GE)
	lpA.append(L)

# generate Laplacian Pyramid for B
lpB = [gpB[5]]
for i in range(5,0,-1):
	GE = cv2.pyrUp(gpB[i])
	L = cv2.subtract(gpB[i-1],GE)
	lpB.append(L)

# Now add left and right halves of images in each level
LS = []
for la,lb in zip(lpA,lpB):
	rows,cols,dpt = la.shape
	cols=cols/2
	cols=int(cols)
	ls = np.hstack((la[:,0:cols], lb[:,cols:]))
	LS.append(ls)

# Now reconstruct
ls_ = LS[0]
for i in range(1,6):
	ls_ = cv2.pyrUp(ls_)
	ls_ = cv2.add(ls_,LS[i])

# image with direct connecting each half
real = np.hstack((A[:,:cols],B[:,cols:]))

plt.imshow(ls_)
plt.show()

cv2.imwrite('Pyramid_blending2.jpg',ls_)
cv2.imwrite('Direct_blending.jpg',real)

f,axarr=plt.subplots(2,3)
axarr[0,0].imshow(lpB[0])
axarr[0,1].imshow(lpB[1])
axarr[0,2].imshow(lpB[2])
axarr[1,0].imshow(lpB[3])
axarr[1,1].imshow(lpB[4])
axarr[1,2].imshow(lpB[5])
plt.show()
