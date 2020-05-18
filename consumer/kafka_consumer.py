import json

from confluent_kafka import Consumer, KafkaError
from api.imdb_client import search_film

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'broker1',
    'auto.offset.reset' : 'earliest',
})

consumer.subscribe(['topic1'])
films = []

while True:
    msg = consumer.poll(1.0)

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
