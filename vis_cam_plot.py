import numpy as np
from sklearn.preprocessing import normalize
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.utils.extmath import randomized_svd
import matplotlib.pyplot as plt
import math

def get_coords():
	res = []
	with open("coordinates.txt", "r") as f:
		lines = f.readlines()
		for row in lines:
			pts = row.split(",")
			pts[3] = pts[3].replace("\n", "")
			res.append(pts)

		return np.array(res, dtype='int32')


coords = get_coords()

x_1 = []  
y_1 = []
x_2 = []
y_2 = []

for row in coords:
	x_1.append(row[0])
	y_1.append(row[1])
	x_2.append(row[2])
	y_2.append(row[3])


plt.plot(x_1, y_1, '-gD')
plt.suptitle('Cam1', fontsize=20)
plt.show()

plt.plot(x_2, y_2, '-gD')
plt.suptitle('Cam2', fontsize=20)
plt.show()