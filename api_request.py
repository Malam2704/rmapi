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


def main():

    intro_text = """
     1. Get Character Data\n
     2. Get Location Data\n
     3. Get Episode Data\t
    """
    user_id_input = input(intro_text)

    if (user_id_input == "1"):
        character_id_input = input("What is the Character Id? \n")
        print("Your Character is" +
              get_character_name_by_id(character_id_input))
    elif (user_id_input == "2"):
        location_id_input = input("What is the Location Id? \n")
        print("Your Character is" +
              get_character_name_by_location(location_id_input))
    elif (user_id_input == "3"):
        episode_id_input = input("What is the Episode Id? \n")
        print("Your Character is" +
              get_character_name_by_episode(episode_id_input))


main()
