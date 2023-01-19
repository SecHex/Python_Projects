import cv2
import numpy as np

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load the dataset
data = np.load('dataset.npy')
X, y = data[:, 1:], data[:, 0]

# Initialize the recognizer
model = cv2.face.LBPHFaceRecognizer_create()
model.train(X, y)

# Define the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read the frame
    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Recognize the face
        label, confidence = model.predict(gray[y:y+h, x:x+w])

        # Draw the label
        cv2.putText(img, str(label), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    # Show the frame
    cv2.imshow('img', img)

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

# Release the VideoCapture
cap.release()
