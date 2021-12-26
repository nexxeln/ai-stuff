import cv2
from random import randrange

# loaded some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# reading an image to detect faces in
img = cv2.imread("RDJandTom.jpg")

# converting the image to grayscale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detecting faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)       # coordinates of a rectangle

# drawing rectangles around all the faces
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x,y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 2)       # (0, 255, 0), 2 => green colour for the rectangle with thickness of 2

# showing the image
cv2.imshow("Face Detector", img)
cv2.waitKey()

print("Code completed")