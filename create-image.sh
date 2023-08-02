#!/bin/bash

# start with generating static front-end assets
npm ci
npm run build --workspace=client

IMAGE_NAME=$(npm run var:image-name -s)
IMAGE_VERSION=$(npm run var:image-version -s)

# build the actual docker image
docker build . --progress=plain --no-cache -t $IMAGE_NAME:$IMAGE_VERSION
