#!/bin/bash

data_dir='/home/pi/intellicatflap/data'

if [ $2 = 'it' ]; then
    docker run -v $data_dir:/app/data -it --device=/dev/video0:/dev/video0 catdetector:$1 /bin/bash
elif [ $2 = 'app' ]; then
    docker run -v $data_dir:/app/data --device=/dev/video0:/dev/video0 catdetector:$1
fi
