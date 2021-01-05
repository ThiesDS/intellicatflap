from google.cloud import storage
import pandas as pd

def download_imgs_w_detected_cats():
    # Initialize client and bucket
    client = storage.Client.from_service_account_json(json_credentials_path='./src/gcs_sync/gcs_serviceaccount.json')
    bucket = client.get_bucket('intellicatflap')

    # Get file with detected cats
    gcs_file = 'raw/cat_detection.log'
    destination_file_name = './data/cat_detection.log'

    # Download cat detection file
    blob = bucket.blob(gcs_file)
    blob.download_to_filename(destination_file_name)

    # Read file into df
    df_cat_detection = pd.read_csv(destination_file_name, sep=": ", header=None)
    df_cat_detection.columns=['img_name','detect_cat']

    # Filter all images where cat is detected
    df_cat_detection_true = df_cat_detection.query('detect_cat=="1"')

    # Specify last n images to download
    datetime_start = '2020/12/31/00/00'
    datetime_end = '2021/01/02/00/00'

    # Download
    imgs_to_download = df_cat_detection_true['img_name']
    destination_file_folder = './data/detected_cats/'
    gcs_dir = 'raw/'
    for img in imgs_to_download:
        
        # Create filename from gcs path
        img_file_name = create_folder_path_from_img_filename(img)

        # Re-format dates
        img_datetime = pd.to_datetime('/'.join(img_file_name.split('/')[0:-1]),format='%Y/%m/%d/%H/%M')
        datetime_start = pd.to_datetime(datetime_start,format='%Y/%m/%d/%H/%M')
        datetime_end = pd.to_datetime(datetime_end,format='%Y/%m/%d/%H/%M')

        # Check if image is in selected time range
        if (img_datetime>=datetime_start) & (img_datetime<=datetime_end):

            # Create gcs path
            gcs_file = gcs_dir + img_file_name

            #gcs_file = 'raw/2021/01/04/09/00/32_871322.jpg'

            # Create blob and download to file
            blob = bucket.blob(gcs_file)
            blob.download_to_filename(destination_file_folder + img)
            
            print('Processing image ' + img)

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

if __name__ == "__main__":
    
    # Download files
    download_imgs_w_detected_cats()