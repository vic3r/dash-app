from confluent_kafka import Producer
from api.imdb_client import search_film

p = Producer({
    'bootstrap.servers': 'localhost:9092',
})
id, code = None, None

def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.forma(err))
    else:
        print('Message deliverd to {} [{}]'.format(msg.topic(), msg.partition()))

def produce_data(film):
    global id, code
    id, code = search_film(film)
    if code < 200 or code >= 300:
        print("Something went wrong: {}".format(code))

while id is not None:
    p.poll(0)
    p.produce('first-topic', id.encode('utf-8'), callback=delivery_report)
    id, code = None, None

# Clean the actual producer
p.flush()
