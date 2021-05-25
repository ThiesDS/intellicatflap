import os
import argparse
import logging
import shutil

from classifier import detect_cat
from utils import save_detections
import glob

logger = logging.getLogger("intellicatflap.cat-detector")
logger.addHandler(logging.NullHandler())


def main(image_dir: str, upload_dir: str, cat_probability_threshold: float, url: str) -> None:
    """ """
    logger.info("Starting cat detector loop")
    while True:

        # Load all file paths (full paths)
        files = os.listdir(image_dir)
        images = [img for img in files if img.endswith(".jpg")]

        logger.debug("Found {image_count} images in {image_dir}".format(image_count=len(images), image_dir=image_dir))
        for image in images:

            # Image path
            image_path = os.path.normpath(os.path.join(image_dir, image))
            logger.debug("Processing {image_name} from in {image_path}".format(image_name=image, image_path=image_path))

            # Probability if cat is on image
            cat_probability = detect_cat(image_path, url)

            # Save cat detections to file
            if cat_probability > cat_probability_threshold:
                logger.debug(
                    "Cat probability for image {image_name}: {cat_probability} - Cat was detected".format(
                        image_name=image, cat_probability=cat_probability
                    )
                )
                save_detections(image_path)
            else:
                logger.debug(
                    "Cat probability for image {image_name}: {cat_probability} - No cat could be detected".format(
                        image_name=image, cat_probability=cat_probability
                    )
                )
            wildcard_path = image_path.replace("jpg", "*")
            files_to_move = glob.glob(wildcard_path)
            for file in files_to_move:
                shutil.move(file, upload_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Classify cats")
    parser.add_argument("-i", "--image-dir", type=str, help="Path to directories where images are detected")
    parser.add_argument("-u", "--upload-dir", type=str, help="Path where processed images will be moved")
    parser.add_argument(
        "-c",
        "--cat-probability-threshold",
        type=float,
        help="The probability threshold where image is seen as a cat",
        default=0.3,
    )
    parser.add_argument(
        "-t",
        "--tensorflow-url",
        type=str,
        help="URL of tensorflow serve",
        default="http://tf-serving:8501/v1/models/cat_classifier:predict",
    )
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
        upload_dir=args.upload_dir,
        cat_probability_threshold=args.cat_probability_threshold,
        url=args.tensorflow_url,
    )
