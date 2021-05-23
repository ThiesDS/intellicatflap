import os
import time
import argparse
import logging
from utils import upload_images_to_gcs

logger = logging.getLogger("intellicatflap.gcs-sync")
logger.addHandler(logging.NullHandler())


def main(image_dir: str, gcs_destination: str, gcs_credentials_path: str, bucket_name: str) -> None:
    # Infinite loop
    logger.info("Starting gcs sync loop loop")
    while True:
        # Wait while camera will take photos
        time.sleep(1)

        # Upload images and detections files to gcs
        upload_images_to_gcs(
            local_dir=image_dir,
            gcs_dir=gcs_destination,
            gcs_credentials_path=gcs_credentials_path,
            bucket_name=bucket_name,
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload to gcs")
    parser.add_argument("-i", "--image-dir", type=str, help="Path to directories where images are stores")
    parser.add_argument("-g", "--gcs-destination", type=str, help="GCS folder where detected images are stored")
    parser.add_argument("-c", "--credentials-path", type=str, help="Path to service account to access GCS")
    parser.add_argument("-b", "--bucket-name", type=str, help="Bucket name")
    parser.add_argument("-v", "--verbose", help="Show debug logs", action="store_true")
    parser.add_argument("-q", "--quiet", help="Show only warnings and errors", action="store_true")

    args = parser.parse_args()

    if args.quiet:
        log_level = logging.WARNING
    elif args.verbose:
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO

    logging.basicConfig(format="%(asctime)s - %(name)s - %(message)s", level=log_level)

    main(
        image_dir=args.image_dir,
        gcs_destination=args.gcs_destination,
        gcs_credentials_path=args.credentials_path,
        bucket_name=args.bucket_name
    )
