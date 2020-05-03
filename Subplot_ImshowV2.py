#	Angkan Biswas
#	03.05.2020
#	To display diffrent color channels side by side


import os
import cv2
from matplotlib import pyplot as plt
import numpy as np


imgPath = '/home/dell/downloads/flowr/flower1.jpg'

imgStatus = os.path.isfile(imgPath)					
print(imgStatus)

if imgStatus == True:
	img = cv2.imread(imgPath)
	h, w, ch = img.shape
	print(h, w, ch)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	
	blue = img[:,:,2]
	red = img[:,:,0]
	green = img[:,:,1]

	title = ['Flower', 'Red', 'Green', 'Blue'] 
	imgList = [img, red, green, blue]
	
	for i in range(4):
		plt.subplot(2, 2, i + 1)
		plt.imshow(imgList[i])
		plt.title(title[i])
	
	plt.show()
	plt.close()
else:
	print('{} does not exist'.format(imgPath))

