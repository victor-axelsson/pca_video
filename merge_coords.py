

coords_cam1 = None
with open("coords_cam1.txt", "r") as f:
    coords_cam1 = f.readlines()

coords_cam2 = None
with open("coords_cam2.txt", "r") as f:
    coords_cam2 = f.readlines()

cam1 = []
for line in coords_cam1:
	pts = line.split(",")
	pts[1] = pts[1].replace("\n", "")
	cam1.append(pts)

cam2 = []
for line in coords_cam2:
	pts = line.split(",")
	pts[1] = pts[1].replace("\n", "")
	cam2.append(pts)

with open("coordinates.txt", "w") as f:
	for i in range(len(cam1)):
		f.write("{},{},{},{}\n".format(cam1[i][0], cam1[i][1], cam2[i][0], cam2[i][1]))
	
