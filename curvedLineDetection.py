import cv2
import numpy as np


vid = cv2.VideoCapture(0)



# Check if the webcam is opened correctly
if not vid.isOpened():
    raise IOError("Cannot open webcam")

# Streams the video
while True:
    ret, img = vid.read()
    # ret is a Boolean value returned by the read function, and it indicates whether or not the frame was captured successfully
    # frame = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Use canny edge detection
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

#school
     x = 400
     y = 200
     w = h = 600

#home
    #x = 200
    #y = 100
    #w = h = 300



    mask = np.zeros(edges.shape[:2], np.uint8)
    mask[y:y + h, x:x + w] = 255
    res = cv2.bitwise_and(edges, edges, mask=mask)


    # Apply HoughLinesP method to
    # to directly obtain line end points
    lines_list = []
    lines = cv2.HoughLinesP(
        res,  # Input edge image
        1,  # Distance resolution in pixels
        np.pi / 180,  # Angle resolution in radians
        threshold=10,  # Min number of votes for valid line
        minLineLength=5,  # Min allowed length of line
        maxLineGap=50  # Max allowed gap between line for joining them
    )



    # this makes sure lines are being detected 
    if lines is not None:

        # Iterate over points
        for points in lines:

            # Extracted points nested in the list
            x1, y1, x2, y2 = points[0]
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            # Draw the lines joing the points
            # On the original image
            # Maintain a simples lookup list for points
            lines_list.append([(x1, y1), (x2, y2)])

        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 4)
    k = cv2.waitKey(10)
    if k == 27:
        break
    cv2.imshow("masked frame", img)


vid.release()
cv2.destroyAllWindows()

# to make my web cam work
# https://subscription.packtpub.com/book/data/9781785283932/3/ch03lvl1sec28/accessing-the-webcam#:~:text=OpenCV%20provides%20a%20video%20capture,display%20them%20in%20a%20window.

#for my line detection
#https://www.geeksforgeeks.org/line-detection-python-opencv-houghline-method/

#for my mask
#https://stackoverflow.com/questions/11492214/opencv-via-python-is-there-a-fast-way-to-zero-pixels-outside-a-set-of-rectangle
