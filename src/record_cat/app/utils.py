import numpy as np
import os
from datetime import datetime


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