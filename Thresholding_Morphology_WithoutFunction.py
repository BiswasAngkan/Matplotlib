# Angkan Biswas
# 09.05.2020
# To perform thresholding & morphology transformation 


import os
import cv2
from matplotlib import pyplot as plt
import numpy as np

imgPath = '/home/dell/Downloads/frog.jpeg'

imgStatus = os.path.isfile(imgPath)
print(imgStatus)

if imgStatus == True:
	''' Load image into a matrix '''
	img = cv2.imread(imgPath)

	''' Convert image from BGR to RGB '''
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	
	''' Thresholding ''' 
	threshold = 127
	maxValue = 255
	_, binarizeImg = cv2.threshold(img, threshold, maxValue, cv2.THRESH_BINARY)
	_, binarizeRed = cv2.threshold(img[:,:,0], threshold, maxValue, cv2.THRESH_BINARY)
	_, binarizeGreen = cv2.threshold(img[:,:,1], threshold, maxValue, cv2.THRESH_BINARY)
	_, binarizeBlue = cv2.threshold(img[:,:,2], threshold, maxValue, cv2.THRESH_BINARY)
	
	'''Perform morphology transformed images'''
	kernel = np.ones((3,3))
	morphologyErode = cv2.erode(img, kernel)				# To shrinken foreground
	morphologyDilate = cv2.dilate(img, kernel)				# To increase the fourground
	morphologyOpen = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)		# Opening = Erosion followed by dilation
	morphologyClose = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)	# Dilation followed by erosion

	''' Put titles & image matrices into 2 lists, so that we can use for...loop '''
	binariTitle = ['RGB','BinarizedRGB', 'BinarizedRed', 'BinarizedGreen', 'BinarizedBlue'] 
	binariList = [img, binarizeImg, binarizeRed, binarizeGreen, binarizeBlue]
	morphologyTitle = ['MorphologyErode', 'MorphologyDilate', 'MorphologyOpen', 'MorphologyClose'] 
	morphologyList = [morphologyErode, morphologyDilate, morphologyOpen, morphologyClose]

	''' Plot binarized images '''
	plt.figure(figsize = (20, 20))	
	
	for i in range(5):
		plt.subplot(3, 3, i + 1)
		plt.imshow(binariList[i], cmap = 'gray')
		plt.title(binariTitle[i])
		plt.axis('off')
	
	''' Plot morphology transformed images '''
	j = 5 
	for i in range(4):
		plt.subplot(3, 3, i +j)
		plt.imshow(morphologyList[i])
		plt.title(morphologyTitle[i])
		plt.axis('off')
		print(i, j, i+j)
	
	''' Save figure '''
	figPath = '/home/dell/downloads/Skype/BinarizedFrog.png'
	plt.savefig(figPath)

	''' Display figure '''
	plt.show()
	
	''' Release plot resource '''
	plt.close()
	
else:
	print('{} does not exist'.format(imgPath))
