#!/bin/bash

# start with generating static front-end assets
npm ci
npm run build --workspace=client

# build the actual docker image
docker build . --progress=plain --no-cache -t flask-svelte-carbon-image

# For linux
# docker build - < Dockerfile

# For windows
# Get-Content Dockerfile | docker build -
