import cv2
vidcap = cv2.VideoCapture('cam1.mov')
success, image = vidcap.read()
count = 0
success = True
while success:
  cv2.imwrite("frames/tmp/frame-%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  count += 1



print("All Done")