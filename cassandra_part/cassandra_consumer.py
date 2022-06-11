import json
from kafka import KafkaConsumer
import variables as var
from cassandra_client import CassandraClient


CONSUMER = KafkaConsumer(var.CASSANDRA_TOPIC, bootstrap_servers=var.BOOTSTRAP_SERVERS,
                         value_deserializer=lambda m: json.loads(m.decode('ascii')),
                         auto_offset_reset='earliest', group_id=None)


def main():

    client = CassandraClient(var.HOST, var.PORT, var.KEYSPACE)
    client.connect()

    for message in CONSUMER:

        try:
            message_data = message.value

            domains_data = (message_data['meta']['id'], message_data['meta']['domain'], message_data['page_title'])
            client.insert_domain_data(domains_data, var.DOMAINS_DATA_TABLE)

            print(message_data)
            pages_users_data = (message_data['meta']['id'], message_data['performer']['user_id'],
                                message_data['performer']['user_text'], message_data['page_title'],
                                message_data['meta']['dt'])
            client.insert_pages_users(pages_users_data, var.PAGES_USERS_TABLE)

            pages_data = (message_data['page_id'], message_data['page_title'])
            client.insert_pages_data(pages_data, var.PAGES_DATA_TABLE)
        except KeyError:
            continue

    client.close()


if __name__ == '__main__':
    main()