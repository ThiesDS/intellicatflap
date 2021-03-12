#!/bin/bash

DOCKER_BUILDKIT=1

logs_dir=$HOME/intellicatflap/logs

if [ $3 = 'build_true' ]; then
	docker build  --ssh default -t interactwgcs:$1 .
fi

if [ $2 = 'it' ]; then
    docker run -v $logs_dir:/app/logs -it interactwgcs:$1 /bin/bash
elif [ $2 = 'app' ]; then
    docker run -v $logs_dir:/app/logs interactwgcs:$1
else 
	echo "Error: Argument 2 must be either it or app."
fi
