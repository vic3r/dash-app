import http
import json
from requests import request

# local modules
from dotenv import load_dotenv
import os

load_dotenv()

API_URL = os.getenv("API_URL")
API_TOKEN = os.getenv("API_TOKEN")


api_url = API_URL
api_token = API_TOKEN

# Get url from settings
url = "https://" + api_url

# Extract key from settings
headers = {
    'x-rapidapi-host': api_url,
    'x-rapidapi-key': api_token
}

def search_film(filmName: str) -> (str, int):
    search_query = url + "/search/" + filmName
    search_response = request("GET", search_query, headers=headers)
    if search_response.status_code < 200 or search_response.status_code >= 300:
        return "Error has happen", search_response.status_code
    if search_response.text is None:
        return "Undefined property text", http.HTTPStatus.NOT_FOUND
    
    film = json.loads(search_response.text)
    if film["titles"] is None or len(film["titles"]) == 0:
        return "Undefined property titles", http.HTTPStatus.NOT_FOUND
    if (film["titles"][0]["id"] is None) or (film["titles"][0]["id"] == ""):
        return "Undefined property title id", http.HTTPStatus.NOT_FOUND
    
    id = film["titles"][0]["id"]
    return id, search_response.status_code

def get_film(id: str) -> str:
    getQuery = url + "/film/" + id
    get_response = request("GET", getQuery, headers=headers)
    if get_response.status_code < 200 or get_response.status_code >= 300:
        return "Error has happen", get_response.status_code
    if get_response.text is None:
        return "Undefined property text", http.HTTPStatus.NOT_FOUND

    return get_response.text
