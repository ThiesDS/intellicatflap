import os
import time

from utils import upload_images_to_gcs

# Current working directory
cwd = os.getcwd()

detection_log_file = cwd + '/data/cat_detection.log'
operation_log_file = cwd + '/logs/operation.log'

# Infinite loop
while True:
    
    # Wait while camera will take photos
    time.sleep(1)
    
    # Upload images and detections files to gcs
    upload_images_to_gcs(local_dir=cwd + '/data/',gcs_dir='classified/')