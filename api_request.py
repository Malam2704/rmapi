import requests


def get_character_name_by_id(id):
    baseurl = "https://rickandmortyapi.com/api/"

    endpoint = "character/" + str(id)

    r = requests.get(baseurl + endpoint)

    data = r.json()

    return data['name']


def main():
    user_id_input = input("Enter a characted Id: ")
    print(get_character_name_by_id(user_id_input))


main()
