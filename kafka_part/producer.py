import requests
import json
from kafka import KafkaProducer
import variables as var


PRODUCER = KafkaProducer(bootstrap_servers=['kafka-server:9092'],
                         value_serializer=lambda m: json.dumps(m).encode('ascii'))


def send_data(url):
    s = requests.Session()

    with s.get(url, headers=None, stream=True) as resp:
        for line in resp.iter_lines():
            if line:
                decoded_data = line.decode('utf8').replace("'", '"')
                if decoded_data.startswith("data:"):
                    try:
                        converted_data = json.loads(decoded_data[6:])
                        PRODUCER.send(var.CASSANDRA_TOPIC, converted_data)
                    except json.decoder.JSONDecodeError:
                        continue
        PRODUCER.flush()


def main():
    send_data(var.STREAM_URL)


if __name__ == '__main__':
    main()
