import numpy as np
import cv2


def click(event, x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        blue = frame[x,y,0]
        green = frame[x,y,1]
        red = frame[x,y,2]
        cv2.circle(frame, (x,y), 3 , (0,0,255), -1)
        myimage = np.zeros((512,512,3), np.uint8)
        myimage[:] = [blue, green, red]
        
        cv2.imshow('image', myimage)
        
    
        


frame = cv2.imread('image1.jpg')
cv2.imshow('image', frame)
points = []

cv2.setMouseCallback('image', click)
cv2.waitKey(0)
cv2.destroyAllWindows()
