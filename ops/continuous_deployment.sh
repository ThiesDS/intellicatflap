#!/bin/bash

# Go to root directory of project (from whereever you are)
cd /home/pi/intellicatflap/

# Pull from pi_deployment branch of repository
git fetch --all && git checkout "pi_deployment" && git pull 

# Rebuild and start service
docker-compose down -v
docker-compose build
docker-compose up

# Write log
USR=$(whoami)
DAT=$(date +"%F %R "
"$DAT$USR: Complete cronjob." >> /home/pi/intellicatflap/logs/operation.log
