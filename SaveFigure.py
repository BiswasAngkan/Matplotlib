# Angkan Biswas
# 02.05.2020
# To save a figure.


import os
import cv2
from matplotlib import pyplot as plt

imgPath = '/home/dell/downloads/Skype/blur1.jpeg'

imgStatus = os.path.isfile(imgPath)
print(imgStatus)

if imgStatus == True:
	img = cv2.imread(imgPath, 0)

	plt.figure(figsize = (20, 20))

	plt.axis('off')
	plt.imshow(img, cmap = 'gray')
	plt.title('Snow Dog')

	figPath = '/home/dell/downloads/Skype/SnowDog.png'
	print(figPath)
	plt.savefig(figPath)

	plt.show()
	plt.close()

else:
	print('{} does not exist'.format(imgPath))

