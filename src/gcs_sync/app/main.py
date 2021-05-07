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
    time.sleep(1)
    
    # Upload images and detections files to gcs
    gcs_sync.upload_images_to_gcs(local_dir=cwd + '/data/',gcs_dir='classified/')