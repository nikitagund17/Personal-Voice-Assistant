import cv2
import os
import numpy as np
import pyautogui

def rec():
    flag=False
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer.yml')

    # Load the face cascade classifier
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    names="shan"

    font = cv2.FONT_HERSHEY_SIMPLEX

    cam = cv2.VideoCapture(0)
    #cam.set(3, 640)
    #cam.set(4, 480)

    while True:
        ret, img = cam.read()

        # Convert the image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale image
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

        for (x, y, w, h) in faces:
            # Extract the face from the image
            face = gray[y:y+h, x:x+w]

            # Recognize the face using the trained model
            id_, accuracy = recognizer.predict(face)

            # Check if the face matches any of the known faces
            if accuracy < 100:
                name = names[id_]
                cv2.putText(img, name, (x+5, y-5), font, 1, (0, 255, 0), 2)
                # Grant access if the face matches a known face
                # print('Access granted to', names)
                flag = True  # set the flag to True if a face is detected
            else:
                name = 'unknown'
                cv2.putText(img, name, (x+5, y-5), font, 1, (0, 0, 255), 2)

            # Draw a rectangle around the face
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
        cv2.imshow('camera', img)
        
        # Check if the flag is True, and break the loop if it is
        if flag:
            break
            
        k = cv2.waitKey(10) & 0xff
        if k == 27:
            break

    cam.release()
    cv2.destroyAllWindows()

    if id_ != 'unknown':
        from Execute import acess
       
        acess()
    elif id_ =='unknown':
        print("You Don't have access")
