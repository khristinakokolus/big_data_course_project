from cassandra_client import CassandraClient
from flask import Flask, request
import variables as var

app = Flask(__name__)


@app.route("/domains_by_pages", methods=['POST'])
def domains_by_pages():
    client = CassandraClient(var.HOST, var.PORT, var.KEYSPACE)
    client.connect()

    data = client.select_existing_domains(var.DOMAINS_DATA_TABLE)
    ret_domains = []
    for row in data:
        ret_domains.append(row[0])

    response = {"domains": ret_domains}

    client.close()
    return response


@app.route("/pages_by_user", methods=['POST'])
def pages_by_user():
    query_data = request.get_json()

    client = CassandraClient(var.HOST, var.PORT, var.KEYSPACE)
    client.connect()

    data = client.select_pages_by_user(query_data['user_id'], var.PAGES_USERS_TABLE)
    ret_pages = []
    for row in data:
        ret_pages.append(row[0])

    response = {"pages": ret_pages}

    client.close()
    return response


@app.route("/pages_count_by_domain", methods=['POST'])
def pages_count_by_domain():
    query_data = request.get_json()

    client = CassandraClient(var.HOST, var.PORT, var.KEYSPACE)
    client.connect()

    data = client.select_pages_count_by_domain(query_data['domain'], var.DOMAINS_DATA_TABLE)

    response = {query_data['domain']: data[0][0]}

    client.close()
    return response


@app.route("/page_by_id", methods=['POST'])
def page_by_id():
    query_data = request.get_json()

    client = CassandraClient(var.HOST, var.PORT, var.KEYSPACE)
    client.connect()

    data = client.select_page_by_id(query_data['page_id'], var.PAGES_DATA_TABLE)

    response = {query_data['page_id']: data[0][0]}

    client.close()
    return response


@app.route("/users_data", methods=['POST'])
def users_data():
    query_data = request.get_json()

    client = CassandraClient(var.HOST, var.PORT, var.KEYSPACE)
    client.connect()

    data = client.select_users_data(query_data['start_time'], query_data['end_time'], var.PAGES_USERS_TABLE)

    response = dict()
    i = 1
    for row in data:
        response[str(i)] = row
        i += 1

    client.close()
    return response

if __name__ == "__main__":
    app.run(debug=True)