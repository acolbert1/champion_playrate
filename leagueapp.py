import cassiopeia as cass
import random
import requests
from cassiopeia import Summoner

cass.set_riot_api_key("")
cass.set_default_region("NA")

response = requests.get("http://ddragon.leagueoflegends.com/cdn/10.10.3216176/data/en_US/champion.json")
data = response.json()["data"]


def character_input():
    character_name = input("Please enter a character name: ")
    key_lookup = data[character_name]["key"]
    print(key_lookup)

    response = requests.get("https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/Q6r3ae6WA5YTcKWOAx2MSiG-emz1oNAcouhLdkGOBifk3Q?champion="+ key_lookup +"&api_key=RGAPI-5f17ca8e-6831-4c95-b884-de4265c13223")
    games_played = response.json()["totalGames"]
    print("You have played " + character_name + " " + str(games_played) + " times")
        


character_input()
    



#user puts in an input and it will display that characters information.


# user can type in a character name i.e. annie
# program will look up character id via the champion api call
# program will pass that id into the match-list api call and return total games played
# for every id in data > id:
#     print ['data']['id']
