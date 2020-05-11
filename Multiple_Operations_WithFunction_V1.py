# Angkan Biswas
# 11.05.2020
# To perform different transformations on a loded image 


import os
import cv2
from matplotlib import pyplot as plt
import numpy as np
from skimage.util import random_noise

def main():
	img = loadImg()

	plt.figure(figsize = (10, 20))
	
	thresholding(img)
	morphology(img)
	noise(img)
		
	figPath = '/home/dell/downloads/Skype/frog.png'
	print(figPath)
	plt.savefig(figPath)

	plt.show()
	plt.close()

def thresholding(img):
	threshold = 127
	maxValue = 255
	_, binarizeImg = cv2.threshold(img, threshold, maxValue, cv2.THRESH_BINARY)
	_, binarizeRed = cv2.threshold(img[:,:,0], threshold, maxValue, cv2.THRESH_BINARY)
	_, binarizeGreen = cv2.threshold(img[:,:,1], threshold, maxValue, cv2.THRESH_BINARY)
	_, binarizeBlue = cv2.threshold(img[:,:,2], threshold, maxValue, cv2.THRESH_BINARY)
	
	imgTitle = ['RGB', 'BinarizedRGB', 'BinarizedRed', 'BinarizedGreen', 'BinarizedBlue'] 
	imgList = [img, binarizeImg, binarizeRed, binarizeGreen, binarizeBlue]
	pltImg(3, 4, 5, 1, imgList, imgTitle)

def morphology(img): 
	kernel = np.ones((3,3))
	morphologyErode = cv2.erode(img, kernel)				# To shrinken foreground
	morphologyDilate = cv2.dilate(img, kernel)				# To increase the fourground
	morphologyOpen = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)		# Opening = Erosion followed by dilation
	morphologyClose = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)	# Dilation followed by erosion

	morphologyTitle = ['MorphologyErode', 'MorphologyDilate', 'MorphologyOpen', 'MorphologyClose'] 
	morphologyList = [morphologyErode, morphologyDilate, morphologyOpen, morphologyClose]
	pltImg(3, 4, 4, 6, morphologyList, morphologyTitle) 

def noise(img):
	img = img / 255							 	
	print(img.max(), img.min())									

	saltyImg = random_noise(img, mode = 'salt', amount = 0.2)
	pepperyImg = random_noise(img, mode = 'pepper', amount = 0.2)
	saltyPepperyImg = random_noise(img, mode = 's&p', amount = 0.2)

	saltyTitle = ['SaltyImg', 'PepperImg', 'SaltyPepperyImg'] 
	saltyList = [saltyImg, pepperyImg, saltyPepperyImg]
	pltImg(3, 4, 3, 10, saltyList, saltyTitle) 

def pltImg(r, c, n, j, imgList, title):			# r = row, c = column, n = number of total img, j = subplot number
	for i in range(n):
		plt.subplot(r, c, i + j)
		plt.imshow(imgList[i], cmap = 'gray')
		plt.title(title[i])
		plt.axis('off')
	
def loadImg():	
	imgPath = '/home/dell/Downloads/frog.jpeg'
	imgStatus = os.path.isfile(imgPath)
	print(imgStatus)

	if imgStatus == True:
		img = cv2.imread(imgPath)
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	
		plt.axis('off')		
		plt.imshow(img)
		plt.show()
		plt.close()

	else:
		print('{} does not exist'.format(imgPath))
	
	return img
	
main()
