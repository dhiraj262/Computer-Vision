# -*- coding: utf-8 -*-


import urllib
import cv2
import numpy as np
url='http://192.168.1.6:8080/shot.jpg'

cap = cv2.VideoCapture(0)
while True:
    ret , frame = cap.read()
 
    # Use urllib to get the image and convert into a cv2 usable format
    imgResp=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    # put the image on screen
    cv2.imshow('IPWebcam',img)
    cv2.imshow('Webcam',frame)
 
    #To give the processor some less stress

 
    if cv2.waitKey(1) ==13:
        break
cv2.destroyAllWindows()
 