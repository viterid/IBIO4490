#
from PIL import Image
import cv2
import numpy as np
import sklearn
from sklearn import mixture
from sklearn.cluster import KMeans

def segmentByClustering (rgbImage, colorSpace, clusteringMethod, numberOfClusters ):
    
    import numpy as np
    #determine if xy is required
    space=colorSpace.split("+")
    leng=len(space)
    w ,h = rgbImage.shape[:2]
	#generate XY matrix
    if leng == 2:
        import numpy as np
        x=range(w)
        xmat= np.repeat(x,h)
        xmat=xmat.reshape(w,h)
        xmat=np.uint8(xmat)
        y=range(h)
        ymat= np.repeat(y,w)
        ymat=ymat.reshape(w,h)
        ymat=np.uint8(ymat)
        colorSpace=space[0]
	#change image to the specified color space
    def RGB(rgbImage):
        newImage = rgbImage
        return newImage
    def HSV (rgbImage):
        import cv2
        newImage = cv2.cvtColor(rgbImage, cv2.COLOR_BGR2HSV)
        return newImage
    def LAB (rgbImage):
        import skimage
        newImage = cv2.cvtColor(rgbImage, cv2.COLOR_BGR2LAB)
        return newImage
	#Switch for color space
    S_color = {
        "rgb" : RGB,
        "lab" : LAB,
		"hsv" : HSV
	}
    func = S_color.get(colorSpace)
    
    newImage=func(rgbImage)
    
	#aply XY matrix if needed
    if leng == 2:
        
        temp=np.ndarray(shape=(w,h,5))
        temp[:,:,0]=newImage[:,:,0]
        temp[:,:,1]=newImage[:,:,1]
        temp[:,:,2]=newImage[:,:,2]
        temp[:,:,3]=xmat
        temp[:,:,4]=ymat
        newImage=temp
        
    indx= 0
    size=newImage.shape
    
    if leng ==2: 
        
        repMat=np.zeros((size[0]*size[1],5))
    else:
        repMat=np.zeros((size[0]*size[1],3))
    
    for i in range(size[0]):
        for j in range(size[1]):
        

            if leng ==2:
            
                i1= (newImage[i,j,3]/(255-0))
                j1= (newImage[i,j,4]/(255-0))
                repMat[indx]= [newImage[i,j,0],newImage[i,j,1],newImage[i,j,2], i1,j1]
                indx=indx+1
        
            else:
        
                repMat[indx]= [newImage[i,j,0],newImage[i,j,1],newImage[i,j,2]]
        
    k= numberOfClusters
        
    if  clusteringMethod == 'kmeans':
            
        kmeans = KMeans(n_clusters=k).fit(repMat)
        labels=kmeans.labels_
        labels= np.reshape(labels,(size[0],size[1]))
        seg= labels
            
    elif clusteringMethod == 'gmm': 
            
        gmm = mixture.GaussianMixture(n_components=k).fit(repMat,y='None')
        labels = gmm.predict(repMat)
        labels= np.reshape(labels,(size[0],size[1]))
        seg= labels
        
    elif clusteringMethod == 'hierarchical':
        
        import sklearn.cluster
        from sklearn.cluster import AgglomerativeClustering 

        cluster = AgglomerativeClustering(n_clusters=k, affinity='euclidean', linkage='ward').fit(repMat)  
        labels=cluster.labels_
        labels= np.reshape(labels,(size[0],size[1]))
        seg=labels
        
    elif clusteringMethod == 'watershed':
        
        a=2
            
            
            
        
    
    return seg
