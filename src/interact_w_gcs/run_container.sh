#!/bin/bash

data_dir='/home/pi/intellicatflap/data'

if [ $3 = 'build_true' ]; then
	docker build -t interactwgcs:$1 .
fi

if [ $2 = 'it' ]; then
    docker run -v $data_dir:/app/data -it interactwgcs:$1 /bin/bash
elif [ $2 = 'app' ]; then
    docker run -v $data_dir:/app/data interactwgcs:$1
else 
	echo "Error: Argument 2 must be either it or app."
fi
