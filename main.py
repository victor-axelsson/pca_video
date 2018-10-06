import numpy as np
from sklearn.preprocessing import normalize
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.utils.extmath import randomized_svd
import matplotlib.pyplot as plt
import math

np.set_printoptions(suppress=True)

def get_coords():
	res = []
	with open("coordinates.txt", "r") as f:
		lines = f.readlines()
		for row in lines:
			pts = row.split(",")
			pts[3] = pts[3].replace("\n", "")
			res.append(pts)

		return np.array(res, dtype='int32')

def invert(arr):
	items = []
	for item in arr:
		items.append(1 - item)

	return np.array(items)

def rotate(x_coord, y_coord, angle):
	rad = angle * math.pi / 180

	new_x_coord = []
	new_y_coord = []
	for i in range(len(x_coord)):
		x = x_coord[i]
		y = y_coord[i]

		new_x = x * math.cos(rad) - y * math.sin(rad)
		new_y = y * math.cos(rad) + x * math.sin(rad)

		new_x_coord.append(new_x)
		new_y_coord.append(new_y)

	return np.array(new_x_coord), np.array(new_y_coord)

def minMaxVector(v):
	scaled = []
	for item in v:
		scaled.append((item - v.min()) / (v.max() - v.min()))

	return np.array(scaled)

def scale(x_coord, y_coord, x_scale, y_scale):
	new_x_coord = []
	new_y_coord = []
	for i in range(len(x_coord)):
		x = x_coord[i]
		y = y_coord[i]

		new_x = x * x_scale
		new_y = y * y_scale

		new_x_coord.append(new_x)
		new_y_coord.append(new_y)

	return new_x_coord, new_y_coord

coords = get_coords()

pca = PCA(n_components=2)
pca.fit(coords)
transformed = pca.transform(coords)

x = minMaxVector(transformed[:,0])
y = minMaxVector(transformed[:,1])

y = invert(y)
x, y = rotate(x, y, 340)
x = minMaxVector(x)
y = minMaxVector(y)
x, y = scale(x, y, 20, 9)

markers_on = [114]
plt.plot(x, y, '-gD', markevery=markers_on)
plt.show()
