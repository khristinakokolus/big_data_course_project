class CassandraClient:
    def __init__(self, host, port, keyspace):
        self.host = host
        self.port = port
        self.keyspace = keyspace
        self.session = None

    def connect(self):
        from cassandra.cluster import Cluster
        cluster = Cluster([self.host], port=self.port)
        self.session = cluster.connect(self.keyspace)

    def execute(self, query):
        self.session.execute(query)

    def close(self):
        self.session.shutdown()

    def insert_domain_data(self, data_to_insert, table_name):
        query = f"INSERT INTO {table_name} (id, domain, page) " \
                f"VALUES ('{data_to_insert[0]}', '{data_to_insert[1]}', '{data_to_insert[2]}');"
        self.execute(query)

    def insert_pages_users(self, data_to_insert, table_name):
        query = f"INSERT INTO {table_name} (id, user_id, user_name, page, creation_timestamp) " \
                f"VALUES ('{data_to_insert[0]}', '{data_to_insert[1]}', '{data_to_insert[2]}', " \
                f"'{data_to_insert[3]}', '{data_to_insert[4]}');"
        self.execute(query)

    def insert_pages_data(self, data_to_insert, table_name):
        query = f"INSERT INTO {table_name} (page_id, page) " \
                f"VALUES ('{data_to_insert[0]}', '{data_to_insert[1]}');"
        self.execute(query)