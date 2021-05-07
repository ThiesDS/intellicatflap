import os

from classifier import detect_cat
from utils import load_image, save_detections


# Set paths
image_dir = 'data/'

# Threshold
cat_thresh = 0.3

while True:

    # Load all file paths (full paths)
    files = os.listdir(image_dir)
    images = [img for img in files if img.endswith('.jpg')]

    for image in images:
        
        # Image path
        image_path = image_dir + image

        # Probability if cat is on image
        cat_probabilitiy = detect_cat(image_path)

        # Save cat detections to file
        if cat_probabilitiy > cat_thresh:
            save_detections(image_path)