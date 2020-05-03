#	Angkan Biswas
#	02.05.2020
#	To draw sine wave on diffrent color channels of a loaded image and display side by side


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
	
	x = list(range(w))
	y = np.sin(x) + (h/2)
		
	blue = img[:,:,2]
	red = img[:,:,0]
	green = img[:,:,1]

	plt.subplot(2, 2, 1)
	plt.plot(x, y, 'r')	
	plt.imshow(img)
	plt.title('Flower')

	plt.subplot(2, 2, 2)
	plt.plot(x, y, 'r')	
	plt.imshow(red)

	plt.title('Red')

	plt.subplot(2, 2, 3)
	plt.plot(x, y, 'r')	
	plt.imshow(green)
	plt.title('Green')

	plt.subplot(2, 2, 4)
	plt.plot(x, y, 'r')	
	plt.imshow(blue)
	plt.title('Blue')
	
	plt.show()
	plt.close()
else:
	print('{} does not exist'.format(imgPath))


