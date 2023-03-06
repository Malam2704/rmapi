# To run files you have to do `python3 "directory/file.py`
# In this case run `python3 "rmapi/api_request.py"`
import requests


def get_character_name_by_id(id):
    baseurl = "https://rickandmortyapi.com/api/"

    endpoint = "character/" + str(id)

    r = requests.get(baseurl + endpoint)

    data = r.json()

    return data['name']


def get_character_name_by_location(id):
    baseurl = "https://rickandmortyapi.com/api/"

    endpoint = "location/" + str(id)

    r = requests.get(baseurl + endpoint)

    data = r.json()

    return data['name']


def get_character_name_by_episode(id):
    baseurl = "https://rickandmortyapi.com/api/"

    endpoint = "location/" + str(id)

    r = requests.get(baseurl + endpoint)

    data = r.json()

    return data['name']
