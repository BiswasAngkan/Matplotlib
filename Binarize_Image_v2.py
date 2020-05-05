# Angkan Biswas
# 05.05.2020
# To binarize an image & its different color channels using thresholding


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
	
	''' Chanel separation '''	
	red = img[:,:,0]
	green = img[:,:,1]
	blue = img[:,:,2]

	''' Thresholding ''' 
	threshold = 127
	maxValue = 255
	_, binarizeImg = cv2.threshold(img, threshold, maxValue, cv2.THRESH_BINARY)
	_, binarizeRed = cv2.threshold(img[:,:,0], threshold, maxValue, cv2.THRESH_BINARY)
	_, binarizeGreen = cv2.threshold(img[:,:,1], threshold, maxValue, cv2.THRESH_BINARY)
	_, binarizeBlue = cv2.threshold(img[:,:,2], threshold, maxValue, cv2.THRESH_BINARY)
	
	print(np.unique(img), np.unique(binarizeImg))
	print(binarizeImg.shape, binarizeRed.shape, binarizeGreen.shape, binarizeBlue.shape)
	print(img.shape, red.shape, green.shape, blue.shape)

	'''Put titles & image matrices into 2 lists, so that we can use for...loop '''

	title = ['RGB', 'Red', 'Green', 'Blue', 'BinarizedRGB', 'BinarizedRed', 'BinarizedGreen', 'BinarizedBlue'] 
	imgList = [img, red, green, blue, binarizeImg, binarizeRed, binarizeGreen, binarizeBlue]

	'''Display & save figure '''
	plt.figure(figsize = (20, 20))	
	
	for i in range(8):
		plt.subplot(2, 4, i + 1)
		plt.imshow(imgList[i], cmap = 'gray')
		plt.title(title[i])
		# if (i >= 4):
		if ((i % 2) == 0):
			plt.axis('off')

	figPath = '/home/dell/downloads/Skype/BinarizedFrog.png'
	print(figPath)
	plt.savefig(figPath)

	plt.show()
	plt.close()
	
else:
	print('{} does not exist'.format(imgPath))
