#!/bin/bash

# Write log
USR=$(whoami)
DAT=$(date +"%F %R ")
echo "$DAT$USR$(pwd): Start cronjob." >> /home/pi/intellicatflap/logs/operation.log

# Go to root directory of project (from whereever you are)
cd /home/pi/intellicatflap/

# Pull from pi_deployment branch of repository
git fetch --all && git checkout "pi_deployment" && git pull 

# Quit service
/usr/local/bin/docker-compose down -v

# Make sure every default network is removed
#docker network rm $(docker network ls -f 'name=intellicatflap_default' -q)

# Rebuild service
/usr/local/bin/docker-compose up -d --build


echo "$DAT$USR$(pwd): Finish cronjob!" >> /home/pi/intellicatflap/logs/operation.log
