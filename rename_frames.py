import glob
import os

files = glob.glob("./frames/cam1/*.jpg")
files.sort()

counter = 0
for file in files:
	pts = file.split("/")

	filename = "/".join(pts[:-1]) + "/frame-" + str(counter) + ".jpg"
	os.rename(file, filename)
	counter += 1

print("ok, done")