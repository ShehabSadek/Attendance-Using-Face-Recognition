import cv2 as cv
import numpy as np
import os
import pickle
from PIL import Image

BASE_DIR=os.path.dirname(os.path.abspath(__file__))
training_folder=os.path.join(BASE_DIR,"Images/Training")

haar_cascade=cv.CascadeClassifier('Classifiers/haarcascade_frontalface_default.xml')
recognizer = cv.face.LBPHFaceRecognizer_create()


c_id=0
label_id={}
y_labels=[]
x_train=[]

for root, dirs, files in os.walk(training_folder):
    for file in files:
        if file.endswith("jpg"):
            path = os.path.join(root,file)
            label = os.path.basename(root).replace(" ","-").lower()
            #print(label,path)
            if not label in label_id:
                label_id[label] = c_id
                c_id += 1 
            _id = label_id[label]
            #print(label_id)
            pil_image= Image.open(path).convert("L")
            image_array = np.array(pil_image,"uint8")
            faces_rect=haar_cascade.detectMultiScale(image_array, scaleFactor=1.2,minNeighbors=5)
            
            for x,y,w,h in faces_rect:
                roi = image_array[y:y+h,x:x+w]
                x_train.append(roi)
                y_labels.append(_id)


# print(y_labels)
# print(x_train)

with open("labels.pckl",'wb') as f:
    pickle.dump(label_id,f)

recognizer.train(x_train,np.array(y_labels))
recognizer.save("trainer.yaml")

# import numpy as np
# import cv2 as cv
# from termcolor import colored

# img = cv.imread('Images/Testing/group.jpg')
# img_grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# people=list()

# haar_cascade=cv.CascadeClassifier('Classifiers/haarcascade_frontalface_default.xml')
# try:
#     haar_cascade.empty()
#     print("Classifier loaded",colored("succesfully",'green'))
# except:
#     print(colored("Error",'red'),"laoding classifier")
# faces_rect=haar_cascade.detectMultiScale(img_grey, scaleFactor=1.2,minNeighbors=5)

# print("Number of faces found in image: {}".format(len(faces_rect)))

# for x,y,w,h in faces_rect:
#     cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
# cv.imshow("face_detection",img)
# cv.waitKey(0)