#!/bin/bash

data_dir=$HOME/private/intellicatflap_analytics/analysis/sample_data/calibration_sample

if [ $3 = 'build_true' ]; then
	docker build -t cat_detector:$1 .
fi

if [ $2 = 'it' ]; then
    docker run -v $data_dir:/app/data -it cat_detector:$1 /bin/bash
elif [ $2 = 'app' ]; then
    docker run -v $data_dir:/app/data cat_detector:$1
else 
	echo "Error: Argument 2 must be either it or app."
fi
