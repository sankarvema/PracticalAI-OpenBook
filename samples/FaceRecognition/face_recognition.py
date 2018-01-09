####################################################
# Modified by Nazmi Asri                           #
# Original code: http://thecodacus.com/            #
# All right reserved to the respective owner       #
####################################################

# Import OpenCV2 for image processing
print("Face Recognition Step");
import cv2
import base64
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError, CollectionInvalid
from bson import json_util, ObjectId
import json
import os,sys

# execute mongoDB in terminal
client = MongoClient()
db = client.mememoji
# Import numpy for matrices calculations
import numpy as np

# Create Local Binary Patterns Histograms for face recognization
recognizer = cv2.face.createLBPHFaceRecognizer()

# Load the trained mode
recognizer.load('trainer/trainer.yml')

# Load prebuilt model for Frontal Face
cascadePath = "haarcascade_frontalface_default.xml"

# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath);

# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX

# Initialize and start the video frame capture
cam = cv2.VideoCapture(0)

# Loop
while True:
    # Read the video frame
    ret, im =cam.read()

    # Convert the captured frame into grayscale
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    # Get all face from the video frame
    faces = faceCascade.detectMultiScale(gray, 1.2,5)

    # For each face in faces
    for(x,y,w,h) in faces:

        # Create rectangle around the face
        cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)

        # Recognize the face belongs to which ID
        Id = recognizer.predict(gray[y:y+h,x:x+w])

        getSamePerson = db.facedataset.find_one({"personIdentity": Id[0]})
        if(getSamePerson and Id[1]<45):
            print(Id);
            Id = getSamePerson['name'];    
        else:
            import winsound
            Freq = 2500 # Set Frequency To 2500 Hertz
            Dur = 1000 # Set Duration To 1000 ms == 1 second
            winsound.Beep(Freq,Dur)
            Id = "Unknown";   
        # # Check the ID if exist 
        # if(Id[0] == 1):
        #     Id = "Aman"

        # elif(Id[0] == 2):
        #         Id = "kranthi"
        # #If not exist, then it is Unknown
        # else:
        #     Id = "Unknown"

        # Put text describe who is in the picture
        cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
        cv2.putText(im, str(Id), (x,y-40), font, 2, (255,255,255), 3)

    # Display the video frame with the bounded rectangle
    cv2.imshow('im',im) 

    # If 'q' is pressed, close program
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Stop the camera
cam.release()

# Close all windows
cv2.destroyAllWindows()
print("Face Recognition Step Completed");
