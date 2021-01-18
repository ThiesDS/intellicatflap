#!/bin/bash

data_dir=$HOME/intellicatflap/data
models_dir=$HOME/intellicatflap/models

if [ $3 = 'build_true' ]; then
	docker build -t catdetector:$1 .
fi

if [ $2 = 'it' ]; then
    docker run -v $data_dir:/app/data -v $models_dir:/app/models -it --device=/dev/video0:/dev/video0 catdetector:$1 /bin/bash
elif [ $2 = 'app' ]; then
    docker run -v $data_dir:/app/data -v $models_dir:/app/models --device=/dev/video0:/dev/video0 catdetector:$1
else 
	echo "Error: Argument 2 must be either it or app."
fi
