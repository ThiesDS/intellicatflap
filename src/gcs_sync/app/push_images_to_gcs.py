import os
from google.cloud import storage

# Get current working directory
cwd = os.getcwd()

# Path of local images
img_path = cwd + '/data/'

# Path of gcs images (raw)
gcs_path = 'raw/'

# Set credentials using the downloaded JSON file and get bucket object
client = storage.Client.from_service_account_json(json_credentials_path='gcs_serviceaccount.json')
#bucket = client.get_bucket('intellicatflap')

# Get all images in data folder
files = os.listdir(img_path)
print(files)

# Upload and delete file from local storage
for file in files:
    # Create object and upload
    object_name = gcs_path + 'img_' + timestamp + '.jpg'
    print('In Loop:')
    print(object_name)
    #blob = bucket.blob(object_name)
    #blob.upload_from_filename(file)
