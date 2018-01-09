####################################################
# Modified by Nazmi Asri                           #
# Original code: http://thecodacus.com/            #
# All right reserved to the respective owner       #
####################################################

# Import OpenCV2 for image processing
print("Starting Registration Step");
import cv2
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError, CollectionInvalid
from bson import json_util, ObjectId
import json
import os,sys

fName = input("Enter your first name: ")
lName = input("Enter your last name:")
org = input("Enter your organization name:")
des = input("Enter your designation name:")
city = input("Enter your city:")
age = input("Enter your age:")
print (fName,lName,org,des,city,age)
# execute mongoDB in terminal
client = MongoClient()
db = client.mememoji

# Start capturing video 
vid_cam = cv2.VideoCapture(0)

# Detect object in video stream using Haarcascade Frontal Face
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For each person, one face id
face_id = db.facedataset.count() + 1;

# Initialize sample face image
count = 0

# Start looping
while(True):

    # Capture video frame
    _, image_frame = vid_cam.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

    # Detect frames of different sizes, list of faces rectangles
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    facedataset = {}

    # Loops for each faces
    for (x,y,w,h) in faces:

        # Crop the image frame into rectangle
        cv2.rectangle(image_frame, (x,y), (x+w,y+h), (255,0,0), 2)
        
        # Increment sample face image
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        # Display the video frame, with bounded rectangle on the person's face
        cv2.imshow('frame', image_frame)

    # To stop taking video, press 'q' for at least 100ms
    if cv2.waitKey(100) & 0xFF == ord('q'):    
        facedataset['personIdentity'] = face_id;    
        facedataset['name'] = fName + ' ' + lName;
        facedataset['org'] = org;
        facedataset['des'] = des;    
        facedataset['city'] = city;    
        facedataset['age'] = age;
        print (facedataset)
        pobj = json.loads(json_util.dumps(facedataset))
        result = db.facedataset.insert_one(pobj)   
        break

    # If image taken reach 100, stop taking video
    elif count>10:
        facedataset['personIdentity'] = face_id;    
        facedataset['name'] = fName + ' ' + lName;
        facedataset['org'] = org;
        facedataset['des'] = des;
        facedataset['city'] = city;    
        facedataset['age'] = age;        
        print (facedataset)
        pobj = json.loads(json_util.dumps(facedataset))
        result = db.facedataset.insert_one(pobj)   
        break

# Stop video
vid_cam.release()

# Close all started windows
cv2.destroyAllWindows()
print("Registration Step Completed Successfully");