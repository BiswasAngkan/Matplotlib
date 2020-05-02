# Angkan Biswas
# 02.05.2020
# To perfrom histogram equalization and save figure.


import os
import cv2
from matplotlib import pyplot as plt

imgPath = '/home/dell/downloads/Skype/blur1.jpeg'

imgStatus = os.path.isfile(imgPath)
print(imgStatus)

if imgStatus == True:
	img = cv2.imread(imgPath, 0)
	h, w = img.shape
	print(h, w)

	equalImg = cv2.equalizeHist(img)			       # Histogram Equalization (HE)	
	clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(4,4))
	claheImg = clahe.apply(img)				       # Contrast Limited Adaptive Histogram Equalization (CLAHE)

	plt.figure(figsize = (20, 20))
		
	plt.subplot(3, 2, 1)
	plt.axis('off')
	plt.imshow(img, cmap = 'gray')
	plt.title('Snow Dog')

	plt.subplot(3, 2, 2)
	plt.axis('off')
	plt.hist(img)
	plt.title('Histogram of Snow Dog')

	plt.subplot(3, 2, 3)
	plt.axis('off')
	plt.imshow(equalImg, cmap = 'gray')
	plt.title('Snow Dog after HE')

	plt.subplot(3, 2, 4)
	plt.axis('off')
	plt.hist(equalImg)
	plt.title('Histogram of Snow Dog after HE')
	
	plt.subplot(3, 2, 5)
	plt.axis('off')
	plt.imshow(claheImg, cmap = 'gray')
	plt.title('Snow Dog after CLAHE')

	plt.subplot(3, 2, 6)
	plt.axis('off')
	plt.hist(claheImg)
	plt.title('Histogram of Snow Dog after CLAHE')

	figPath = '/home/dell/downloads/Skype/SnowDog.png'
	print(figPath)
	
	plt.savefig(figPath)

	plt.show()
	plt.close()

else:
	print('{} does not exist'.format(imgPath))

