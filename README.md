# Dash App
The first dash app for movie & tv series analytics

## Prerequisistes
- Install python 3.8
- Install pip
- Install ElasticSearch[link](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html)
## Configure Virtual Env
Run the following commands in the root directory: 
- `virtualenv env`
- `source venv/bin/activate`
- `pip install -r requirements.txt`

# Run
- `pip install -r requirements.txt`
- `gunicorn app:server`
