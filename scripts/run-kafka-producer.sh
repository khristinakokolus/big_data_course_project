#!/bin/bash
declare -r NETWORK="streaming-data-project"

docker build --tag producer-kafka -f Dockerfile.producer .
docker run -d --name kafka-producer --network ${NETWORK} --rm producer-kafka