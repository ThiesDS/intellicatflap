import os
import argparse
from classifier import detect_cat
from utils import save_detections


def main(image_dir: str = "/data", cat_probability_threshold: float = 0.3):
    """ """
    while True:

        # Load all file paths (full paths)
        files = os.listdir(image_dir)
        images = [img for img in files if img.endswith(".jpg")]

        for image in images:

            # Image path
            image_path = image_dir + image

            # Probability if cat is on image
            cat_probability = detect_cat(image_path)

            # Save cat detections to file
            if cat_probability > cat_probability_threshold:
                save_detections(image_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Classify cats")
    parser.add_argument("-i", "--image-dir", help="Path to directories where images are detected", default="/data")
    parser.add_argument(
        "-c", "--cat-probability-threshold", help="The probability threshold where image is seen as a cat", default=0.3
    )
    args = parser.parse_args()

    main(image_dir=args.image_dir, cat_probability_threshold=args.cat_probability_threshold)
