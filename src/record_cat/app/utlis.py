import numpy as np

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
    
    # Switch for next one
    frame_before = frame

    return motion, frame_before