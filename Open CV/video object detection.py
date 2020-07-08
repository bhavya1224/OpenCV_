#HSV -> Hue Saturation Value
# hue corresponds to the color components(base pigmint),
# hence just by selecting a range of Hue you can select any color.(0-360)

# Saturantion is the amount of color

#Value is basically the brightness of the color.

import cv2
import numpy as np
cap = cv2.VideoCapture(0);
def nothing(x):
    pass

cv2.namedWindow("tracking")
cv2.createTrackbar("lh", "tracking", 0, 255, nothing)
cv2.createTrackbar("ls", "tracking", 0, 255, nothing)
cv2.createTrackbar("lv", "tracking", 0, 255, nothing)
cv2.createTrackbar("uh", "tracking", 255, 255, nothing)
cv2.createTrackbar("us", "tracking", 255, 255, nothing)
cv2.createTrackbar("uv", "tracking", 255, 255, nothing)

while True:
    ret ,frame = cap.read()
    if ret== True:
        hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)
        lh = cv2.getTrackbarPos("lh", "tracking")
        ls = cv2.getTrackbarPos("ls", "tracking")
        lv = cv2.getTrackbarPos("lv", "tracking")
        uh = cv2.getTrackbarPos("uh", "tracking")
        us = cv2.getTrackbarPos("us", "tracking")
        uv = cv2.getTrackbarPos("uv", "tracking")
        
        
        l_b = np.array([lh,ls,lv]) # lower color range
        u_b = np.array([uh,us,uv]) # upper color range
        mask = cv2.inRange(hsv, l_b, u_b)
        res = cv2.bitwise_and(frame,frame,mask=mask)
        
        
        cv2.imshow("frame",frame)
        cv2.imshow("mask",mask)
        cv2.imshow("result",res)
        key = cv2.waitKey(1)
    if key == 27:
        break
    else:
        print(" ")
cap.release()
cv2.destroyAllWindows()
