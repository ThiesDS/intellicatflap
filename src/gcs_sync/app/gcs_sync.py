import os
from google.cloud import storage

def upload_images_to_gcs(local_dir, gcs_dir):
    """
        Uploads all images in local_dir to gcs_dir in bucket

        :param: local_dir: Path where the data is located locally
        :param: gcs_dir: Path where the data shall be uplaoded on gcs bucket
    """

    # Set credentials using the downloaded JSON file and get bucket object
    client = storage.Client.from_service_account_json(json_credentials_path='gcs_serviceaccount.json')
    bucket = client.get_bucket('intellicatflap')

    # Get all images in data folder
    files = os.listdir(local_dir)
    
    # Get first 500
    files = files[:500]

    # Upload and delete file from local storage
    for file in files:
         
        # Upload only jpg images
        if file.endswith(".catdetect"):
            
            # Create file paths
            local_image_file = local_dir + file.replace('.catdetect','.jpg')
            local_detection_file = local_dir + file
            
            gcs_image_file = gcs_dir + create_folder_path_from_img_filename(local_image_file)
            gcs_detection_file = gcs_dir + create_folder_path_from_img_filename(local_detection_file)
            
            # Upload from local to gcs
            blob_image = bucket.blob(gcs_image_file)
            blob_image.upload_from_filename(local_image_file)

            blob_detection = bucket.blob(gcs_detection_file)
            blob_detection.upload_from_filename(local_detection_file)
            
            # After uploading, delete it
            os.remove(local_image_file)
            os.remove(local_detection_file)

def upload_file_to_gcs(local_file, gcs_file):
    """
        Uploads all files in local_dir to gcs_dir in bucket

        :param: local_dir: Path where the data is located locally
        :param: gcs_dir: Path where the data shall be uplaoded on gcs bucket
    """

    # Set credentials using the downloaded JSON file and get bucket object
    client = storage.Client.from_service_account_json(json_credentials_path='gcs_serviceaccount.json')
    bucket = client.get_bucket('intellicatflap')
    
    # Upload from local to gcs
    blob = bucket.blob(gcs_file)
    blob.upload_from_filename(local_file)


def create_folder_path_from_img_filename(filename):
    """
        Takes file name and creates a folder path for gcs: year/month/day/hour/minute/img_second_millisecond.jpg

        :param: gcs_dir path of gcs file
    """
    
    # Split filename into blocks
    filename_split = filename.split('_')
    
    # Use blocks to build filepath for gcs
    gcs_file_path = filename_split[1][0:4] + '/' + filename_split[1][4:6] + '/' + filename_split[1][-2:] + '/' + filename_split[2][:2] + '/' + filename_split[2][2:4] + '/' + filename_split[2][4:6] + filename_split[2][6:13].replace('.','_') + '.' + filename.split('.')[-1]

    return gcs_file_path
