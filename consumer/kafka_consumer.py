import json

from confluent_kafka import Consumer, KafkaError
from api.imdb_client import get_film

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'group1',
    'client.id': 'client-1',
    'enable.auto.commit': True,
    'session.timeout.ms': 20000,
    'default.topic.config': {'auto.offset.reset': 'smallest'}
})

consumer.subscribe(['first-topic'])
films = []

while True:
    msg = consumer.poll(1.0)
    print("connected")
    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print('End of partition reached {}/{}'.format(msg.topic(), msg.partition()))
        else:
            print("Error occured: {}".format(msg.error()))
        continue

    decoded_message = json.loads(msg.value().decode('utf-8'))
    print(("Message arrived: {}").format(decoded_message))
    films.append(decoded_message)

# close consumer
consumer.close()
