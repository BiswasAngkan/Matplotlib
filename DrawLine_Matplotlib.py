#	Angkan Biswas
#	30.04.2020
#	To draw line using Matplotlib


from matplotlib import pyplot as plt
import numpy as np

x = list(range(100))
y = list(range(50))
z = list(range(50))

u = 30 * np.sin(x)
v = x * np.sin(x)
w = [a+10 for a in x]
t = y + z

plt.plot(x, v, 'k')
plt.plot(x, w, 'x--')
plt.plot(x, u, 'r')
plt.plot(x, t, 'g')


plt.show()
plt.close()
