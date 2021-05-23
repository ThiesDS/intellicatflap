import os
import logging
from google.cloud import storage

logger = logging.getLogger("intellicatflap.gcs-sync.utils")
logger.addHandler(logging.NullHandler())


def upload_images_to_gcs(local_dir: str, gcs_dir: str, gcs_credentials_path: str, bucket_name: str) -> None:
    """
    Uploads all images in local_dir to gcs_dir in bucket

    :param: local_dir: Path where the data is located locally
    :param: gcs_dir: Path where the data shall be uploaded on gcs bucket
    """

    # Set credentials using the downloaded JSON file and get bucket object
    client = storage.Client.from_service_account_json(json_credentials_path=gcs_credentials_path)
    bucket = client.get_bucket(bucket_name)

    # Get all images in data folder - Ignore all other types
    files = [file for file in os.listdir(local_dir) if file.endswith(".jpg") or file.endswith(".catdetected")]

    number_of_files = len(files)
    logger.debug("Found {image_count} files in {image_dir}".format(image_count=number_of_files, image_dir=local_dir))
    # Upload and delete file from local storage
    for idx, file in enumerate(files):
        logger.debug(
            "Iterataion {iteration} of {number_of_files} - Processing {image_name}".format(
                image_name=file, iteration=idx, number_of_files=number_of_files
            )
        )
        # Upload only jpg images
        if file.endswith(".jpg"):

            # This file should exist if a cat was detected
            file_cat_detected = file.replace(".jpg", ".catdetected")

            if file_cat_detected in files:

                # Path to cat folder
                gcs_image_file = gcs_dir + "cat/" + create_folder_path_from_img_filename(file)

            else:

                # Path to no cat folder
                gcs_image_file = gcs_dir + "no_cat/" + create_folder_path_from_img_filename(file)

            # Upload from local to gcs
            blob_image = bucket.blob(gcs_image_file)

            local_image_file_path = os.path.normpath(os.path.join(local_dir, file))

            logger.debug(
                "Iterataion {iteration} of {number_of_files} - Uploading file {image_name} to {bucket}".format(
                    image_name=local_image_file_path,
                    iteration=idx,
                    number_of_files=number_of_files,
                    bucket=gcs_image_file,
                )
            )

            blob_image.upload_from_filename(local_image_file_path)

            # After uploading, delete it
            os.remove(local_image_file_path)

            # FIX ME: That functionality should be optimized. Remove also the helper files - That is not working!
            # if file_cat_detected in files:
            #     os.remove(file_cat_detected)

        logger.debug(
            "Iterataion {iteration} of {number_of_files} - Processing {image_name} - DONE!".format(
                image_name=file, iteration=idx, number_of_files=number_of_files
            )
        )


def create_folder_path_from_img_filename(filename: str) -> str:
    """
    Takes file name and creates a folder path for gcs: year/month/day/hour/minute/img_second_millisecond.jpg

    :param: gcs_dir path of gcs file
    """

    # if len(filename_split) != :
    #     raise Exception("")
    filename_split = filename.split("_")
    # Use blocks to build filepath for gcs
    gcs_file_path = (
        filename_split[1][0:4]
        + "/"
        + filename_split[1][4:6]
        + "/"
        + filename_split[1][-2:]
        + "/"
        + filename_split[2][:2]
        + "/"
        + filename_split[2][2:4]
        + "/"
        + filename_split[2][4:6]
        + "/"
        + "_".join(filename.split(".")[:-1])
        + "."
        + filename.split(".")[-1]
    )

    return gcs_file_path
