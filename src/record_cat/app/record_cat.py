import cv2
import time
import os
from pathlib import Path
from datetime import datetime

# Get current working directory
cwd = os.getcwd()

# instatiate webcam video capture
videoCaptureObject = cv2.VideoCapture(0)

# Initiate additional varialbes and paramters
result = True
img_path = cwd + "/data/"

while(result):

    # Create timestamp
    time_curr = datetime.now()
    time_formatted = time_curr.strftime('%Y%m%d%M:%S.%f')

    # Create image name with timestamp
    img_name = "img_" + str(time_formatted) + ".jpg"
    img_destination = img_path + img_name  

    # Capture webcam video
    ret,frame = videoCaptureObject.read()

    # Write to file
    cv2.imwrite(img_destination,frame)

    # Sleep for 1 seconds
    time.sleep(1) 

# Release
videoCaptureObject.release()
cv2.destroyAllWindows()
