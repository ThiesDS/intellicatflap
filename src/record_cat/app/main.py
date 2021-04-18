import cv2
import time
import os
import logging
from pathlib import Path
from datetime import datetime

from utils import motion_detector


# Configure logging
log_time = datetime.today()
log_file_path = os.getcwd() + '/logs/'
log_file_name = 'log_' + log_time.strftime('%Y%m%d%H%M%S') + '.log'
FORMATTER = logging.Formatter('%(asctime)s|%(name)s|%(levelname)s|%(funcName)s:%(lineno)d|%(message)s')

file_handler = logging.FileHandler(log_file_path + log_file_name)
file_handler.setFormatter(FORMATTER)

logger = logging.getLogger('record_cat_' + __name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)

logger.info('Start service')

# Get current working directory
cwd = os.getcwd()

# instatiate webcam video capture
videoCaptureObject = cv2.VideoCapture(0)

# Initiate additional varialbes and paramters
img_path = cwd + "/data/"

# Paramter for motion filter (later to be replaced by docker env var)
motion_filter = True
frame_before = None
thresh = 20

while True:

    logger.info('Enter loop.')

    # Capture webcam video
    ret,frame = videoCaptureObject.read()

    # Optional motion filter
    if motion_filter:
        motion,frame_before = motion_detector(frame,frame_before,thresh)
    else:
        # if motion filter is off, always save image
        motion = True

    # If motion is detected, save image
    if motion:
        
        # Create timestamp
        time_curr = datetime.now()
        time_formatted = time_curr.strftime('%Y%m%d_%H%M%S.%f')

        # Create image name with timestamp
        img_name = "img_" + str(time_formatted) + ".jpg"
        img_destination = img_path + img_name  

        # Rotate and write
        frame_flipped = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

        # Write image to file
        cv2.imwrite(img_destination,frame_flipped)

    # Sleep for 1 seconds
    time.sleep(.5) 

# Release
videoCaptureObject.release()
cv2.destroyAllWindows()
