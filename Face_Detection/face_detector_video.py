import cv2
from random import randrange

# loading some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# capturing the video from a webcam
webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)      # 0 => default webcam, put in the video name("video.mp4"), for it to work with a recorded video

# looping through the frames
while True:
    # reading the current frame 
    successful_frame_read, frame = webcam.read()

    # converting the image to grayscale
    grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detecting faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_frame)       # coordinates of a rectangle

    # drawing rectangles around all the faces
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 2)       # (0, 256, 0), 2 => green colour for the rectangle with thickness of 2

    # showing the webcam
    cv2.imshow("Face Detector", frame)
    key = cv2.waitKey(1)     # 1 => presses a key for every 1 millisecond, which enables live video

    # terminating the program if 'Q' is pressed
    if (key == 81) or (key == 113):     # 81 = 'Q' and 113 = 'q' 
        break
    
# releasing the VideoCapture object
webcam.release()

print("Code completed")