import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while 1:
    ret,frame =cap.read()
    into_hsv =cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    L_limit1=np.array([0,100,20])
    U_limit1=np.array([10,255,255])
    L_limit2=np.array([160,100,20])
    U_limit2=np.array([180,255,255])

    L_mask=cv2.inRange(into_hsv,L_limit1,U_limit1)
    U_mask=cv2.inRange(into_hsv,L_limit2,U_limit2)

    red=cv2.bitwise_and(frame,frame,mask=L_mask+U_mask)
    
    cv2.imshow('Original',frame)
    cv2.imshow('Red Detector',red)

    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()
