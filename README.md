# Wikipedia data stream processing project


# Description

The purpose of this project is to process Wikipedia data stream. Here are used such technologies as Kafka,  
NoSQL database Cassandra and Docker.


# Design


Located in ```Documentation.pdf```


## Usage

Clone the repository:

```
https://github.com/khristinakokolus/big_data_course_project.git
```

Launch Kafka and Zookeeper servers:
```
bash scripts/run-kafka-cluster.sh
```

Launch Cassandra node:
```
bash scripts/run-cassandra-cluster.sh
```

Launch producer to read stream data:
```
cd kafka_part
bash ../scripts/run-kafka-producer.sh
```

Launch consumer to read Kafka messages and write data to Cassandra:
```
cd ..
cd cassandra_part
bash ../scripts/run-cassandra-consumer.sh
```

Launch API for usage:
```
cd ..
cd api
bash ../scripts/run-api.sh
```

To shutdown Kafka, Zookeeper and Cassandra servers:
```
bash scripts/shutdown-cluster.sh
```

# Results

Example of the queries is located in ```requests.http``` and examples of responses in ```Documentation.pdf```.
