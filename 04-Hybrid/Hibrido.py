#!/bin/python

from PIL import Image
#Descraga las imágenes
import wget
import numpy
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

#Tango
url='https://drive.google.com/uc?export=download&id=1sdVXEhn9noiL9H5CLdFvzmGcu02d_6p1'
filename= wget.download(url)

#Haru
url='https://drive.google.com/uc?export=download&id=1_wtLaayeTRA-8hoF2vEcnX4XhkPq49eK'
filename= wget.download(url)

#Reescalar las imágenes al mismo tamaño
Tango=Image.open('Haru.png',mode='r')
Tango=Tango.resize((600,900)) 

Haru=Image.open('Tango.png',mode='r')
Haru=Haru.resize((600,900))


sigmaT=6
sigmaH=13
TangoAr = numpy.array(Tango)
HaruAr= numpy.array(Haru)

for i in [0,1,2]:

	TangoAr[:,:,i]= gaussian_filter(TangoAr[:,:,i], sigmaT, order=0, output=None, mode='reflect',cval=0.0, truncate=4.0)

	HaruAr[:,:,i]= gaussian_filter(HaruAr[:,:,i], sigmaH, order=0, output=None, mode='reflect',cval=0.0, truncate=4.0)


TangoAr= numpy.array(Tango)-TangoAr
TangoHaru= TangoAr+HaruAr

TangoFinal= Image.fromarray(TangoAr)
HaruFinal= Image.fromarray(HaruAr)

TangoHaru= Image.fromarray(TangoHaru)

TangoHaru.save('final.png')

plt.imshow(HaruFinal)
plt.show()
plt.imshow(TangoFinal)
plt.show()
plt.imshow(TangoHaru)
plt.show()




