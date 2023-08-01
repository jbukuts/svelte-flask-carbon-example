#! /bin/bash

# formatting helpers
BOLD=$(tput bold)
UNDL=$(tput smul)
NORM=$(tput sgr0)

# null device to throw away stderr and stdout output
LOG_FILE="/dev/null"

echo $npm_package_name

# Make sure user really wants to.
DOCKER_IMAGE_NAME="flask-svelte-carbon-image"
read -p "Remove all containers and images for ${BOLD}${UNDL}$DOCKER_IMAGE_NAME${NORM}? (y/n)" confirm ;
echo "" ;

if [ "$confirm" == "y" ]; then

    # find containers using image and stop and remove them
    CONTAINER_PIDS=$(docker ps -aq --filter ancestor="$DOCKER_IMAGE_NAME")
    if [ "$CONTAINER_PIDS" ]; then
        echo "Removing container(s) with id(s): ";
        docker ps -a --filter ancestor="$DOCKER_IMAGE_NAME"
        echo ""

        echo "Stopping container(s)";
        docker stop $CONTAINER_PIDS &> $LOG_FILE
        echo "Stopped container(s)";

        docker rm $CONTAINER_PIDS &> $LOG_FILE
        echo "Removed container(s)";
    else
        echo "No containers to remove."
    fi
    echo ""

    # find image and dangling images and remove them
    IMAGE_PIDS=$(docker image ls -aq --filter reference="$DOCKER_IMAGE_NAME")
    if [ "$IMAGE_PIDS" ]; then
        echo "Removing image(s) with id(s): "
        docker image ls -a --filter reference="$DOCKER_IMAGE_NAME"
        echo ""
        
        docker rmi $IMAGE_PIDS &> $LOG_FILE
        echo "Removed image(s)"

        docker image prune --force &> $LOG_FILE
        echo "Pruned dangling image(s)"
    else
        echo "No images to remove."
    fi
    echo ""
else
    echo "Did not remove containers." ;
    exit 0
fi

