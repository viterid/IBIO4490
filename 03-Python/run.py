#!/bin/python

import time
start = time.time()

import os
download= [file for file in os.listdir() if file.endswith('LAGdataset_100')]

if not download:

	import wget
	url = 'http://www.ivl.disco.unimib.it/wp-content/uploads/2016/09/LAGdataset_100.zip'
	filename = wget.download(url)

	import zipfile
	zip_ref = zipfile.ZipFile('LAGdataset_100.zip', 'r')
	zip_ref.extractall('LAGdataset_100')
	zip_ref.close()

import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import PIL
import numpy as np

os.mkdir('Copia')

mainDir= os.listdir('LAGdataset_100')
db='LAGdataset_100' 

for i in range (0,9):

	randNum= random.randint(0,1010)
	dir11= os.path.join(db, mainDir[randNum])
	dir12= os.path.join(db, mainDir[randNum],'y')

	oldPath= [file for file in os.listdir(dir11) if file.endswith('.png')]
	youngPath=[file for file in os.listdir(dir12) if file.endswith('.png')]

	dir11= os.path.join(dir11, oldPath[0])
	dir12= os.path.join(dir12,youngPath[0])

	oldIm=Image.open(dir11,mode='r')
	oldImC=oldIm.resize((256,256))
	oldImC.save(os.path.join('Copia',oldPath[0]))

	youngIm=Image.open(dir12,mode='r')
	youngImC=youngIm.resize((256,256))
	youngImC.save(os.path.join('Copia',youngPath[0]))

copyDir= os.listdir('Copia')


#https://stackoverflow.com/questions/41793931/plotting-images-side-by-side-using-matplotlib 

f, axarr = plt.subplots(2,9)
axarr[0,0].imshow(mpimg.imread(os.path.join('Copia',copyDir[0])))
axarr[1,0].imshow(mpimg.imread(os.path.join('Copia',copyDir[1])))
axarr[0,1].imshow(mpimg.imread(os.path.join('Copia',copyDir[2])))
axarr[1,1].imshow(mpimg.imread(os.path.join('Copia',copyDir[3])))
axarr[0,2].imshow(mpimg.imread(os.path.join('Copia',copyDir[4])))
axarr[1,2].imshow(mpimg.imread(os.path.join('Copia',copyDir[5])))
axarr[0,3].imshow(mpimg.imread(os.path.join('Copia',copyDir[6])))
axarr[1,3].imshow(mpimg.imread(os.path.join('Copia',copyDir[7])))
axarr[0,4].imshow(mpimg.imread(os.path.join('Copia',copyDir[8])))
axarr[1,4].imshow(mpimg.imread(os.path.join('Copia',copyDir[9])))
axarr[0,5].imshow(mpimg.imread(os.path.join('Copia',copyDir[10])))
axarr[1,5].imshow(mpimg.imread(os.path.join('Copia',copyDir[11])))
axarr[0,6].imshow(mpimg.imread(os.path.join('Copia',copyDir[12])))
axarr[1,6].imshow(mpimg.imread(os.path.join('Copia',copyDir[13])))
axarr[0,7].imshow(mpimg.imread(os.path.join('Copia',copyDir[14])))
axarr[1,7].imshow(mpimg.imread(os.path.join('Copia',copyDir[15])))
axarr[0,8].imshow(mpimg.imread(os.path.join('Copia',copyDir[16])))
axarr[1,8].imshow(mpimg.imread(os.path.join('Copia',copyDir[17])))
print ('Hasta antes de visualizar las imágenes')
end = time.time()
print(end - start)

plt.show()

import shutil
shutil.rmtree('Copia')

