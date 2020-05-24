# Angkan Biswas
# 24.05.2020
# To load an image & draw circles using buttons


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import cv2

'''	Load image	'''
imgPath = '/home/dell/Downloads/frog.jpeg'
img = cv2.imread(imgPath)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

'''	Determine the center & radius of the circle	'''
h, w, c = img.shape
centerX = int(w/2) ; centerY = int(h/1.3 ); radius = int(h/12)

'''	Draw the circle & control its color using buttons	'''
fig, ax = plt.subplots()
plt.subplots_adjust(bottom = 0.2)

class Index(object):
	def prev(self, event):
		print('previous')
		img1 = img.copy()
		circle1 = cv2.circle(img1, (centerX, centerY), radius, color = (0,0,255), thickness = -1)
		ax.imshow(circle1)
		
	def next(self, event):
		print('next')
		img2 = img.copy()
		circle2 = cv2.circle(img2, (centerX, centerY), radius, color = (255,0,0), thickness = -1)
		ax.imshow(circle2)

callback = Index()
axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
axnext = plt.axes([0.81, 0.05, 0.1, 0.075])

bnext = Button(axnext, 'Next')
bnext.on_clicked(callback.next)

bprev = Button(axprev, 'Previous')
bprev.on_clicked(callback.prev)

plt.show()
