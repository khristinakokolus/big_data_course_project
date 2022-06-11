#!/bin/bash
declare -r NETWORK="streaming-data-project"

docker build --tag consumer-cassandra -f Dockerfile.consumer .
docker run -d --name cassandra-consumer --network ${NETWORK} --rm consumer-cassandra