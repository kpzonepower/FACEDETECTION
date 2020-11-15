#01_face_dataset.py
import cv2
import os

 
cam = cv2.VideoCapture(0)
cam.set(3,640) # set Width
cam.set(4,480) # set Height

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

face_id = input('\n enter user id end press <return> ==>')

print("\n [INFO] Initializing face capture.Look the camera and wait ...")

count = 0
while(True):

    ret, img = cam.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        count += 1

        
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        cv2.imshow('video', img)

    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break

print("\n [INFO] Exiting Program and cleanup stuff")

cam.release()
cv2.destroyAllWindows()
