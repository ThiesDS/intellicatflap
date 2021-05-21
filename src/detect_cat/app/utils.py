from keras.preprocessing.image import load_img, img_to_array
from typing import Tuple
import numpy as np


def load_image(filename: str, target_size: Tuple[int] = (224, 224)) -> np.array:
    """Load and convert an image to a centered numpy array

    Args:
        filename: Path to a given image
        target_size: Tuple containing image height and width as integers
    Returns:
        A numpy array with the centered image
    Raises:
        ValueError: If target_size is doesn't have length 2
    """
    if len(target_size) != 2:
        raise ValueError("target_size parameter must be a tuple with exactly 2 integers for height and width")
    # load the image
    img = load_img(filename, target_size=target_size)

    # convert to array
    img = img_to_array(img)

    # reshape into a single sample with 3 channels
    img = img.reshape(1, target_size[0], target_size[1], 3)

    # center pixel data
    img = img.astype("float32")
    img = img - [123.68, 116.779, 103.939]

    return img


def save_detections(image_path: str) -> None:
    """Save an empty file to store information on images containing cats

    Args:
        image_path: Path to image
    """

    # Path with name of file with detection information
    cat_detection_path = image_path.replace(".jpg", ".catdetected")

    # Write empty file
    with open(cat_detection_path, "w") as file:
        file.write("")
