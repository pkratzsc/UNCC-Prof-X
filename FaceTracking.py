import cv2
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

oldx = 0
oldy = 0

#Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#To caputre vidoe from webcam
cap = cv2.VideoCapture(0)

#To use a video file as input
#cap = cv2.VideoCapture('filename.mp4')

while True:
    #Read the frame
    img = cap.read()
   
    #Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   
    #Detect the faces
   
    #LED Color
    faces = face_cascade.detectMltiScale(gray, 1.1, 4)
   
    #Draw the rectangle around each face
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0) ,2)
        facewidth = y-x
        pixelsperinch = facewidth/8.5
        transy = y - oldy
        transx = x - oldx
        transy = transy / pixelsperinch
        transx = transx / pixelsperinch
        print("X Movement in Inches")
        print(transx)
        print("Y Movement in Inches")
        print(transy)
        oldx = x
        oldy = y
        GPIO.output(18, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(18, GPIO.LOW)
       
        cv2.imshow('img', img)
        k = cv2.waitKey(30) & 0xff
        if k==27:
            break
cap.release()