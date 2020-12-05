#!/bin/bash

# Go to root directory of project (from whereever you are)
cd /home/doctore/intellicatflap/

# Pull from pi_deployment branch of repository
git fetch --all && git checkout "pi_deployment" && git pull 

echo "hello"