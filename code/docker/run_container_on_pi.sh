#!/bin/bash

data_dir='/home/pi/intellicatflap/data'

docker run -v $data_dir:/intellicatflap/data -it --device /dev/video0 catdetector:latest /bin/bash
