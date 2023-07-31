#! /bin/bash

# Make sure user really wants to.
read -p "Remove all stopped containers ? (y/n)" confirm ;
echo "" ;

if [ "$confirm" == "y" ]; then
    echo "Removing stopped containers..." ;
    echo "" ;
    PIDS=$(docker ps --no-trunc -aq)
    if [ $PIDS ]; then
        echo "Removing container(s) with id(s): " ;
        docker rm $(docker ps --no-trunc -aq)
    else
        echo "No containers to remove."
        exit 0
    fi
else
    echo "Did not remove containers." ;
    exit 0
fi