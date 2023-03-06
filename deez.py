from api_request import *


def main():

    menu_text = "\n\t----Menu----\n"
    intro_text = " 1. Get Character Data\n 2. Get Location Data\n 3. Get Episode Data\n\r"
    print(menu_text)
    user_id_input = input(intro_text)

    if(user_id_input == "1"):
        character_id_input = input("What is the Character Id? \n")
        print("Your Character is " +
              get_character_name_by_id(character_id_input))
    elif(user_id_input == "2"):
        location_id_input = input("What is the Location Id? \n")
        print("Your Location is " +
              get_character_name_by_location(location_id_input))
    elif(user_id_input == "3"):
        episode_id_input = input("What is the Episode Id? \n")
        print("Your Episode is " +
              get_character_name_by_episode(episode_id_input))


main()
