import os
import time
import gcs_sync

# Current working directory
cwd = os.getcwd()

# Loop every 3 hours and uplaod files to gcs
for i in range(0,9999):
    # Wait 3 hours: Camera will take photos
    time.sleep(5)
    
    # Upload images and detections files to gcs
    gcs_sync.upload_images_to_gcs(local_dir=cwd + '/data/',gcs_dir='raw/operations/')

    # Upload operation log files    
    gcs_sync.upload_file_to_gcs(local_file=cwd + '/data/cat_detection.log',gcs_file='raw/detections/detection_raw_cv2.log')

    # Upload operation log files
    gcs_sync.upload_file_to_gcs(local_file=cwd + '/logs/operation.log',gcs_file='raw/ops/operation.log')
