import os
from google.cloud import storage

# Get current working directory
cwd = os.getcwd()

# Paths
local_dir = cwd + '/data/'
gcs_dir = 'raw/'

# Set credentials using the downloaded JSON file and get bucket object
client = storage.Client.from_service_account_json(json_credentials_path='gcs_serviceaccount.json')
bucket = client.get_bucket('intellicatflap')

# Get all images in data folder
files = os.listdir(img_path)

# Upload and delete file from local storage
for file in files:
    # Upload only jpg images
    if file.endswith(".jpg"):
        # Create file paths
        local_file_path = local_dir + file
        gcs_file_path = gcs_dir + file
        # Upload from local to gcs
        blob = bucket.blob(gcs_file_path)
        blob.upload_from_filename(local_file_path)
        # DEBUG
        print('Uploaded file: ' + file)
