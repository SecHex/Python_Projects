import cv2
import numpy as np


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

data = np.load('dataset.npy')
X, y = data[:, 1:], data[:, 0]
model = cv2.face.LBPHFaceRecognizer_create()
model.train(X, y)
cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        label, confidence = model.predict(gray[y:y+h, x:x+w])
        cv2.putText(img, str(label), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)


    cv2.imshow('img', img)


    k = cv2.waitKey(30) & 0xff
    if k==27:
        break


cap.release()
