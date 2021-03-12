#!/bin/bash

logs_dir=$HOME/intellicatflap/logs
test_data_dir=$HOME/intellicatflap/tests/test_imgs

if [ $3 = 'build_true' ]; then
	docker build -t tf-serving-test:$1 .
fi

if [ $2 = 'it' ]; then
    docker run -v $logs_dir:/app/logs -v $test_data_dir:/app/test_data -it tf-serving-test:$1 /bin/bash
elif [ $2 = 'app' ]; then
    docker run -v $logs_dir:/app/logs -v $test_data_dir:/app/test_data tf-serving-test:$1
else 
	echo "Error: Argument 2 must be either it or app."
fi
