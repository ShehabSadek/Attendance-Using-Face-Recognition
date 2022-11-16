import cv2 as cv
import os
import pickle
from termcolor import colored

BASE_DIR=os.path.dirname(os.path.abspath(__file__))
testing_folder=os.path.join(BASE_DIR,"Images/Testing")

haar_cascade=cv.CascadeClassifier('Classifiers/haarcascade_frontalface_default.xml')
recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yaml")

labels={}
with open("labels.pckl",'rb') as f:
    old_labels = pickle.load(f)
    labels = {v:k for k,v in old_labels.items()}

for root, dirs, files in os.walk(testing_folder):
    for file in files:
        path = os.path.join(root,file)
        img= cv.imread(path)
        # print(colored(file,"yellow"))
        gray_img= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        faces_rect=haar_cascade.detectMultiScale(gray_img, scaleFactor=1.2,minNeighbors=5)


        for i in faces_rect:
            x,y,w,h = i
            roi = gray_img[y:y+h,x:x+w]
            _id,conf = recognizer.predict(roi)
            # print(colored("ID {}".format(_id),'green'),colored(", Conf {}".format(conf),'red'))
            cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            cv.putText(img,labels[_id],(x+2,y),cv.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),2,cv.LINE_AA)
        cv.imshow("face_detection",img)
        cv.waitKey(0)