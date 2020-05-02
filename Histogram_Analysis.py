# Angkan Biswas
# 02.05.2020
# To display histogram of diffrent color of loded image side by side


import os
import cv2
from matplotlib import pyplot as plt

imgPath = '/home/dell/downloads/forest/4.1*0drOXMZVz0cx8jlXW2SxTg.jpeg'

imgStatus = os.path.isfile(imgPath)
print(imgStatus)

if imgStatus == True:
	img = cv2.imread(imgPath)
	h, w, ch = img.shape
	print(h, w, ch)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

	red = img[:,:,0]
	green = img[:,:,1]
	blue = img[:,:,2]

	plt.figure(figsize = (20, 20))	
	plt.subplot(3, 3, 1)
	plt.axis('off')
	plt.imshow(img)
	plt.title('Forest')

	plt.subplot(3, 3, 2)
	plt.axis('off')
	plt.imshow(red, cmap = 'gray')
	plt.title('Red')

	plt.subplot(3, 3, 3)
	plt.axis('off')
	plt.hist(red)
	
	plt.subplot(3, 3, 4)
	plt.axis('off')
	plt.imshow(green, cmap = 'gray')
	plt.title('Green')

	plt.subplot(3, 3, 5)
	plt.axis('off')
	plt.hist(green)

	plt.subplot(3, 3, 6)
	plt.axis('off')
	plt.imshow(blue, cmap = 'gray')
	plt.title('Blue')

	plt.subplot(3, 3, 7)
	plt.axis('off')
	plt.hist(blue)
	

	plt.show()
	plt.close()
	
	
