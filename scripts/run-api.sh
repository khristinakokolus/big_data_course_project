#!/bin/bash

declare -r NETWORK="streaming-data-project"

docker build -f Dockerfile.api . -t wikipedia_api_rest
docker run -d -p 8080:8080 --network ${NETWORK}  --name wikipedia_api --rm wikipedia_api_rest