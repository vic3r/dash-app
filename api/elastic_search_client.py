from datetime import datetime
from elasticsearch import Elasticsearch

# local modules
from dotenv import load_dotenv
import os

load_dotenv()

ELASTICSEARCH_HOST = os.getenv("ELASTICSEARCH_HOST")
ELASTICSEARCH_PORT = os.getenv("ELASTICSEARCH_PORT")

def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host': ELASTICSEARCH_HOST, 'port': ELASTICSEARCH_PORT}])
    if _es.ping():
        print('connection stablished')
    else:
        print('could not connect to storage')
    return _es

def create_index(es_object, index_name='movie'):
    created = False
    settings = {
        "settings": {
            "number_of_shards": 5,
            "number_of_replicas": 1
        },
        "mappings": {
            "members": {
                "dynamic": "strict",
                "properties": {
                    "id": {
                        "type": "text"
                    },
                    "title": {
                        "type": "text"
                    },
                    "year": {
                        "type": "text"
                    },
                    "rating": {
                        "type": "text"
                    },
                    "poster": {
                        "type": "text"
                    }
                }
            }
        }
    }
    try:
        if not es_object.indices.exists(index_name):
            # Change 400 when in production, otherwise the db will be overwritten
            es_object.indices.create(index=index_name, ignore=400, body=settings)
            print('index created')
        created = True
    except Exception as ex:
        print(str(ex))
    finally:
        return created
