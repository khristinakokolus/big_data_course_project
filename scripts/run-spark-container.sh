#!/bin/bash

declare -r NETWORK="streaming-data-project"

docker run --rm -it --network ${NETWORK} --name spark-submit -v "$(pwd)":/opt/app bitnami/spark:3 /bin/bash