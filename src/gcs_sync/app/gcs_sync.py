import os
from google.cloud import storage

def upload_files_to_gcs(local_dir, gcs_dir):
    """
        Uploads all files in local_dir to gcs_dir in bucket

        :param: local_dir: Path where the data is located locally
        :param: gcs_dir: Path where the data shall be uplaoded on gcs bucket
    """

    # Set credentials using the downloaded JSON file and get bucket object
    client = storage.Client.from_service_account_json(json_credentials_path='gcs_serviceaccount.json')
    bucket = client.get_bucket('intellicatflap')

    # Get all images in data folder
    files = os.listdir(local_dir)

    # Upload and delete file from local storage
    for file in files:
        
        # Upload only jpg images
        if file.endswith(".jpg"):
            
            # Create file paths
            local_file = local_dir + file
            gcs_file = gcs_dir + file
            
            # Upload from local to gcs
            blob = bucket.blob(gcs_file)
            blob.upload_from_filename(local_file)
            
            # After uploading, delete it
            os.remove(local_file) 
