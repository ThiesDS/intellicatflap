#!/bin/bash

# Go to root directory of project (from whereever you are)
cd /home/pi/intellicatflap/

# Pull from pi_deployment branch of repository
git fetch --all && git checkout "pi_deployment" && git pull 

# Rebuild and start service
docker-compose up --force-recreate --build