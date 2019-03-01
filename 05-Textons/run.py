import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validaton
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
#Read images

with open('TrImGr','rb') as f:
	images=pickle.load(f)

#load Anotations
with open('Anotaciones') as f:
	anot=pickle.load(f)
#Variable for different textons dictionaries
files=['PruebaTextones1','PruebaTextones1k16','PruebaTextones1k32','PruebaTextones1k48','PruebaTextones1k64','PruebaTextones1k80','PruebaTextones1k96','PruebaTextones1k112']
K=[128,16,32,48,64,80,96,112]
#maximum depth of the random Forest
depths = [5,10]
#Maximum number of trees
Trees = [10,15]

def histc(X,bins):
	import numpy as no
	map_to_bins=np.digitize(X,bins)
	r=np.zeros(bins.shape)
	for i in map_to_bins:
		r[i-1] += 1
	return np.array(r)

from assingTextons import assingTextons
from fbRun import fbRun

#Temporal variable for the better textons maps
maps=np.array([])
# Maximun cossvalidation Average untin the current point
maxValue=0



for i in range(8):
	#Load Textons Diccionary
	with open(files[i],'rb') as f:
		trSet=pickle.load(f)
	#Assing the textons to the training group
	for image in images:
		tempmap=assingTextons(fbRun(fb,image),textons.traspose())
		#Indexing the map of every image created
		hist=np.linalg.norm(histc(tempmap.flaten(), np.arange(K[i]))/tempmap.size)
		np.append(maps,hist)
	for depth in depths:
		for tree in trees:
			#Create the random fores Clasifier with depth and tree parameters
			RFcls=RandomForestClasifier(n_estimators=tree,max_depth=depth)
			#cross validaton of the moder
			CVrf= cross_validation.cross_val_score(RFcls,maps,anot,cv=3)
			value = CVrf.mean()
			print ('Cross Validation Avereage {} for: depth = {} trees = {} file = {} ', format(value, depth, tree, file))
			#Determine the best model until the current iteration
			if maxValue<value:
				maxValue=value
				clasifier=RFcls
				usedMaps=maps
				Textons=files[i]
				kidx=K[i]
#fit the training data into the best classifier
classifier.fit(usedMaps,anot)

with open('RfClsF','wb') as f:
	pikle.dump(clasifier,f)

#open the textons with the best result for the test
with open(Textons, 'rb') as f:
    textons= pickle.load(f)

#Cargar imagenes Test

# Varible for test images map
testMap=np.array([])

#asignar textones a las imagenes de Test
for image in test:
	tempmap=assigTextons(fbRun(fb,image),textons.traspose())

	testHist=np.linag.norm(histc(testmap.flatten(),np.arrange(kidx))/testmap.size)

	np.append(testMap,testHist)
#predict the categories for the current test dataSet
predictions=classifier.predict(testMap)

matrix=confusión_matrix(anot,pred)
with open ('matriz','wb') as f:
	pickle.dump(matrix,f)
