# Angkan Biswas
# 25.05.2020
# To understand how use button


import matplotlib.pyplot as plt
from matplotlib.widgets import Button

def main():
	global functionDict, bWidth, bHeight, bY 

	functionDict = {'1': one, '2': two, '3': three, '4': four}
	bWidth = 0.1; bHeight = 0.075; 	bY = 0.7 
	
	fig = plt.gcf()						# gcf = get current figure
	fig.canvas.set_window_title('Calculator')

	bt1 = draw_single_button(0.1, '1')
	bt2 = draw_single_button(0.21, '2')
	bt3 = draw_single_button(0.32, '3')
	bt4 = draw_single_button(0.43, '4')	

	plt.show()
	plt.close()

def one(event):		
	print('One')	

def two(event):
	print('Two')

def three(event):
	print('Three')

def four(event):
	print('Four')

def draw_single_button(bX, label):
	ax = plt.axes([bX, bY, bWidth, bHeight])
	bt = Button(ax, label)
	bt.on_clicked(functionDict[label])

	return bt

main()
