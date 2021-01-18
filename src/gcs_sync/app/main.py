import os
import time
import gcs_sync

# Current working directory
cwd = os.getcwd()

detection_log_file = cwd + '/data/cat_detection.log'
operation_log_file = cwd + '/logs/operation.log'

# Loop every 3 hours and uplaod files to gcs
while True:
    # Wait 3 hours: Camera will take photos
    time.sleep(5)
    
    # Upload images and detections files to gcs
    gcs_sync.upload_images_to_gcs(local_dir=cwd + '/data/',gcs_dir='raw/')

    # Upload operation log files
    if os.path.exists(detection_log_file):
        gcs_sync.upload_file_to_gcs(local_file=detection_log_file,gcs_file='detections/detection_raw_cv2.log')

    # Upload operation log files
    if os.path.exists(operation_log_file):
        gcs_sync.upload_file_to_gcs(local_file=operation_log_file,gcs_file='ops/operation.log')