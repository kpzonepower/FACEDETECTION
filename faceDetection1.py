import numpy as np
import cv2
cap = cv2.VideoCapture(0)
cap.set(3,1920) # set Width
cap.set(4,1080) # set Height
while True:
    ret, img = cap.read()
    cv2.imshow('video',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
cap.release()
cv2.destroyAllWindows()

