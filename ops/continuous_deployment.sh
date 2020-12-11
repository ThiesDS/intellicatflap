#!/bin/bash

# Go to root directory of project (from whereever you are)
cd /home/pi/intellicatflap/

# Pull from pi_deployment branch of repository
git fetch --all && git checkout "pi_deployment" && git pull 

# Rebuild and start service
docker-compose down
docker-compose rm --force
docker volume rm $(docker volume ls -q)
docker-compose up -d

# Write log
date +"%F %R: Complete cronjob." >> /home/pi/intellicatflap/logs/operation.log
