import cv2
import os

def highlight_faces(frame, faces):
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
        cv2.rectangle(frame, ((0,frame.shape[0] -25)),(270, frame.shape[0]), (255,255,255), -1)

# Paths
local_dir = '../data/detected_cats/'

# Alternative, faster face detector
detector = cv2.CascadeClassifier('../config/haarcascade_frontalcatface_extended.xml')

# images with detected cats
files = os.listdir(local_dir)

for file in files:

    # Read image
    img = cv2.imread(local_dir + file) 

    # Detect cat
    faces = detector.detectMultiScale(img)#, scaleFactor=1.2, minNeighbors=3)

    if len(faces)>0:
        # Highlight faces
        highlight_faces(img, faces)

        # Save to file again
        new_file = file.split('.')[0] + '_face.jpg'
        cv2.imwrite(local_dir + new_file, img)
