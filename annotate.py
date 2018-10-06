import cv2

global frame_count
global image

frame_count = 0
NR_EXAMPLES = 173

def on_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = (x, y)
        with open("coords_cam1.txt", "a") as f:
            f.write("{},{}\n".format(x, y))
        print(refPt)
        global frame_count
        frame_count += 1
        pth = './frames/cam1/frame-'+ str(frame_count) +'.jpg'
        print(pth)
        show_image(pth)

def show_image(path):
    global image
    image = cv2.imread(path)
    clone = image.copy()
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.setMouseCallback("image", on_click)
    cv2.resizeWindow('image', 2048, 2048)

show_image('./frames/cam1/frame-'+ str(frame_count) +'.jpg')

# keep looping until the 'q' key is pressed
while frame_count < NR_EXAMPLES -1:
    # display the image and wait for a keypress
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF
 
    # if the 'r' key is pressed, reset the cropping region
    if key == ord("r"):
        image = clone.copy()
 
    # if the 'c' key is pressed, break from the loop
    elif key == ord("c"):
        break
