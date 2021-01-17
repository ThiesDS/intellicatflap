#!/bin/bash

git checkout "master" && git fetch --all
if [ $(git diff --name-only master origin/master | wc -l) -gt 0 ]; then 
    # Pull new changes
    git pull
    
    # Quit service
    /usr/local/bin/docker-compose down -v
    
    # Rebuild service
    /usr/local/bin/docker-compose up -d --build

    # Write log
    echo "$DAT$USR$(pwd): Pulled from origin." >> /home/pi/intellicatflap/logs/operation.log
else
    echo "Booooob"
fi