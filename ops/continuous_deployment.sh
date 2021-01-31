#!/bin/bash

# Write log
#USR=$(whoami)
#DAT=$(date +"%F %R ")
#echo "$DAT$USR$(pwd): Start cronjob." >> /home/pi/intellicatflap/logs/operation.log

# Go to root directory of project (from whereever you are)
cd /home/pi/intellicatflap/

# Pull from master branch of repository, of commits have been made to master
git checkout "master" && git fetch
if [ $(git diff --name-only master origin/master | wc -l) -gt 0 ]; then 
    # Pull new changes
    git pull
    
    # Quit service
    /usr/local/bin/docker-compose down -v
    
    # Rebuild service
    /usr/local/bin/docker-compose up -d --build

    # Write log
    #echo "$DAT$USR$(pwd): Pulled from origin." >> /home/pi/intellicatflap/logs/operation.log
fi

# Write log
#DAT=$(date +"%F %R ")
#echo "$DAT$USR$(pwd): Finish cronjob!" >> /home/pi/intellicatflap/logs/operation.log
