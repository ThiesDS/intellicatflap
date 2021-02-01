import cv2
import time
import os
from pathlib import Path
from datetime import datetime

# Get current working directory
cwd = os.getcwd()

# instatiate webcam video capture
videoCaptureObject = cv2.VideoCapture(0)

# Instantiate cv2-cat detector
detector_path = cwd + "/models/pretrained/"
detector_type = "haarcascade_frontalcatface_extended.xml"
#cat_detector = cv2.CascadeClassifier(detector_path + detector_type)

# Initiate additional varialbes and paramters
result = True
img_path = cwd + "/data/"

while(result):

    # Create timestamp
    time_curr = datetime.now()
    time_formatted = time_curr.strftime('%Y%m%d_%H%M%S.%f')

    # Create image name with timestamp
    img_name = "img_" + str(time_formatted) + ".jpg"
    img_destination = img_path + img_name  

    # Capture webcam video
    ret,frame = videoCaptureObject.read()
    
    # Rotate because camera is installed on its head
    frame_flipped = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

    # Write image to file
    cv2.imwrite(img_destination,frame_flipped)

    # If a cat is detected, this returns a list of rectangles
    #detected_cats = cat_detector.detectMultiScale(frame_flipped) 

    # Write to file, if cat was detected or not
    #txt = "\n" + img_name + ": "
    #file_destination = img_path + "cat_detection.log"
    #if len(detected_cats)>0:
    #    detected=1
    #    with open(file_destination, "a") as file_object:
    #        file_object.write(txt + str(detected))
    #else:
    #    detected=0
    #    with open(file_destination, "a") as file_object:
    #        file_object.write(txt + str(detected))

    # Sleep for 1 seconds
    time.sleep(.5) 

# Release
videoCaptureObject.release()
cv2.destroyAllWindows()
