import numpy as np
import cv2 as cv
from termcolor import colored

img = cv.imread('Images/Training/group.jpg')
img_grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
people=list()

haar_cascade=cv.CascadeClassifier('Classifiers/haarcascade_frontalface_default.xml')
try:
    haar_cascade.empty()
    print("Classifier loaded",colored("succesfully",'green'))
except:
    print(colored("Error",'red'),"laoding classifier")
faces_rect=haar_cascade.detectMultiScale(img_grey, scaleFactor=1.2,minNeighbors=5)

print("Number of faces found in image: {}".format(len(faces_rect)))

for x,y,w,h in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv.imshow("face_detection",img)
cv.waitKey(0)