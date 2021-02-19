import os

import numpy as np
import tensorflow as tf

from object_detection.utils import label_map_util, config_util
from object_detection.builders import model_builder

from utils import load_image_into_numpy_array, get_model_detection_function

# Set paths
cwd = os.getcwd()

pipeline_config = "../tensorflow/models/research/object_detection/configs/tf2/ssd_mobilenet_v2_fpnlite_640x640_coco17_tpu-8.config"
model_dir = "../pretrained_models/ssd_mobilenet_v2_fpnlite_640x640_coco17_tpu-8/checkpoint/"
image_dir = 'data/'

# Load pipeline config and build a detection model
configs = config_util.get_configs_from_pipeline_file(pipeline_config)
model_config = configs['model']
detection_model = model_builder.build(model_config=model_config, is_training=False)

# Restore checkpoint
ckpt = tf.compat.v2.train.Checkpoint(model=detection_model)
ckpt.restore(os.path.join(model_dir, 'ckpt-0')).expect_partial()

# Get detection function
detect_fn = get_model_detection_function(detection_model)

# Detect objects
thresh = 0.3

while True:

    files = os.listdir(image_dir)
    images = [img for img in files if img.endswith('.jpg')]
    images.sort()

    for image in images:
        
        # Load image
        image_path = image_dir + image
        image_np = load_image_into_numpy_array(image_path)
        input_tensor = tf.convert_to_tensor(np.expand_dims(image_np, 0), dtype=tf.float32)
        
        # Detections
        detections, predictions_dict, shapes = detect_fn(input_tensor)

        # Extract cat detections
        cat_detections = [[cat_class.numpy(),cat_score.numpy(),cat_box.numpy()] for cat_class,cat_score,cat_box in zip(detections['detection_classes'][0],detections['detection_scores'][0],detections['detection_boxes'][0]) if cat_class == 16 and cat_score >= thresh]
        
        # Save cat detections to file, if some are found
        detection = image.replace('.jpg','.catdetect')
        detection_path = image_dir + detection
        if cat_detections:
            with open(detection_path, "w") as file:
                file.write(f"{cat_detections[0][1]}, {cat_detections[0][2]}")
        else:
            with open(detection_path, "w") as file:
                    file.write(f"None")
