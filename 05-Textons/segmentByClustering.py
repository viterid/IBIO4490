from PIL import Image

def segmentByClustering (rgbImage, colorSpace, clusteringMethod, numberOfClusters ):

	#determine if xy is required
	space=colorSpace.split("+")
	leng=space.leng
	w ,h = rgbImage.size
	#generate XY matrix
	if leng == 2:
		import numpy as np
		x=range(x)
		xmat= np.repeat(x,h)
		y=range(y)
		ymat= np.repeat(y,w)
	#change image to the specified color space
	def RGB(rgbImage):
		newImage = rgbImage
		return newImage
	def HSV (rgbImage):
		import skimage
		newImage = skimage.color.rgb2hsv(rgbImage)
		return newImage
	def LAB (rgbImage):
		import skimage
		newImage = skimage.color.rgb2lab(rgbImage)
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
		newImage.append(xmat,ymat)




imPath='BSDS_small/train/12003.jpg'
import cv2

rgbImage=cv2.imread(imPath)


seg=segmentByClustering (rgbImage, 'rgb', 'kmeans',4  )
