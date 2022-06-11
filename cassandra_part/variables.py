# Kafka configs
CASSANDRA_TOPIC = 'wikipedia-stream-cassandra'
BOOTSTRAP_SERVERS=['kafka-server:9092']

# Cassandra configs
HOST = 'cassandra-node'
PORT = 9042
KEYSPACE = 'wikipedia'
DOMAINS_DATA_TABLE = 'domains_data'
PAGES_USERS_TABLE = 'pages_users'
PAGES_DATA_TABLE = 'pages_data'