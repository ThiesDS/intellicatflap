import numpy as np
import os
import logging
from datetime import datetime

# Configure logging
time = datetime.today()
log_file_path = os.getcwd() + '/logs/'
log_file_name = 'log_' + time.strftime('%Y%m%d%H%M%S') + '.log'
FORMATTER = logging.Formatter('%(asctime)s|%(name)s|%(levelname)s|%(funcName)s:%(lineno)d|%(message)s')

file_handler = logging.FileHandler(log_file_path + log_file_name)
file_handler.setFormatter(FORMATTER)

logger = logging.getLogger('record_cat_' + __name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)

logger.info('Start logging')


def motion_detector(frame,frame_before,thresh):

    if frame_before==None:
        # On start, no motion 
        motion = False
    else:
        # Calculate sum of squared difference
        frame_diff_sq = (frame-frame_before)**2
        img_diff_sq_sum = np.sum(frame_diff_sq)/(frame_diff_sq.shape[0]*frame_diff_sq.shape[1])
        
        # If sum of squared difference is larger then thresh, motion is detected
        if img_diff_sq_sum > thresh:
            motion = True
        else:
            motion = False
    
        # Log motion sensor infos
        #logger.info('Image Diff: ' + str(round(img_diff_sq_sum,1)) + ': Motion: ' + str(motion))

    # Switch for next one
    frame_before = frame

    return motion, frame_before