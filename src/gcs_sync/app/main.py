import os
import time
import gcs_sync

# Paths
cwd = os.getcwd()
local_dir = cwd + '/data/'
gcs_dir = 'raw/'

# Loop every 3 hours and uplaod files to gcs
for i in range(0,9999):
    # Wait 3 hours: Camera will take photos
    time.sleep(60*1)
    # Upload files to gcs and delete it locally
    gcs_sync.upload_files_to_gcs(local_dir,gcs_dir)