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
        return self.session.execute(query)

    def close(self):
        self.session.shutdown()

    def select_existing_domains(self, table):
        query = f"SELECT DISTINCT domain FROM {table}"
        data = self.execute(query)
        return data

    def select_pages_by_user(self, user_id, table):
        query = f"SELECT page FROM {table} WHERE user_id = '{user_id}'"
        data = self.execute(query)
        return data

    def select_pages_count_by_domain(self, domain, table):
        query = f"SELECT COUNT(page) FROM {table} WHERE domain = '{domain}'"
        data = self.execute(query)
        return data

    def select_page_by_id(self, page_id, table):
        query = f"SELECT page FROM {table} WHERE page_id = '{page_id}'"
        data = self.execute(query)
        return data

    def select_users_data(self, start_time, end_time, table):
        query_initial = f"SELECT user_id, user_name FROM {table} " \
                f"WHERE creation_timestamp >= '{start_time}' AND creation_timestamp <= '{end_time}' ALLOW FILTERING"
        data = self.execute(query_initial)
        ids = []
        requested_data = []
        for row in data:
            if row[0] not in ids:
                query_count = f"SELECT COUNT(page) FROM {table} WHERE user_id = '{row[0]}'"
                page_count = self.execute(query_count)
                requested_data.append([row[0], row[1], page_count[0][0]])
                ids.append(row[0])
        return requested_data
