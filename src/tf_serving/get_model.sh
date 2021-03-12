#!/bin/bash

# Download model
wget http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_fpnlite_640x640_coco17_tpu-8.tar.gz

# Untar and rmove tar file
tar -xvf ssd_mobilenet_v2_fpnlite_640x640_coco17_tpu-8.tar.gz
rm ssd_mobilenet_v2_fpnlite_640x640_coco17_tpu-8.tar.gz 
