#	Angkan Biswas
#	02.05.2020
#	To draw a sine wave on a loaded image. 


import os
import cv2
from matplotlib import pyplot as plt
import numpy as np


imgPath = '/home/dell/downloads/flower/1.marguerite-729510__340.jpg'

imgStatus = os.path.isfile(imgPath)
print(imgStatus)

if imgStatus == True:
	img = cv2.imread(imgPath)
	h, w, ch = img.shape
	print(h, w, ch)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

	x = list(range(w))
	y = np.sin(x) + (h/2)
		
	plt.plot(x, y, 'r')
	plt.imshow(img)
	plt.title('Flower')
	plt.show()
	plt.close()
else:
	print('{} does not exist'.format(imgPath))
