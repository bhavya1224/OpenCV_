import numpy as np
import cv2
#event = [i for i in(dir(cv2) if 'EVENT' in i]
#print(events)

def click(event, x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        text = str(x) + ', '+ str(y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,text, (x,y),font,1,(255,255,0), 2,cv2.LINE_AA)
        cv2.imshow('image',frame)
        
    if event==cv2.EVENT_RBUTTONDOWN:
        blue = frame[y, x, 0]
        green = frame[y, x, 1]
        red = frame[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(frame,text, (x,y),font,0.5,(0,255,0), 2)
        cv2.imshow('image',frame)
        

frame = np.zeros((512, 512, 3), np.uint8)
cv2.imshow('image', frame)

cv2.setMouseCallback('image', click)
cv2.waitKey(0)
cv2.destroyAllWindows()


         


