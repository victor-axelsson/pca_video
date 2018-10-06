import cv2
import time

NR_EXAMPLES = 173
frame_count = 0

def get_image(path, name):
    image = cv2.imread(path)
    clone = image.copy()
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(name, 512, 512)
    return image



# keep looping until the 'q' key is pressed
while frame_count < NR_EXAMPLES -1:
    # display the image and wait for a keypress
    pth = './frames/cam1/frame-'+ str(frame_count) +'.jpg'
    print(pth)
    img_cam1 = get_image('./frames/cam1/frame-'+ str(frame_count) +'.jpg', "cam1")
    img_cam2 = get_image('./frames/cam2/frame-'+ str(frame_count) +'.jpg', "cam2")

    cv2.imshow("cam1", img_cam1)
    cv2.imshow("cam2", img_cam2)

    key = cv2.waitKey(1) & 0xFF

    # if the 'c' key is pressed, break from the loop
    if key == ord("c"):
        break
    #cv2.imshow("cam2", img_cam2)
    frame_count += 1

    time.sleep(1)
