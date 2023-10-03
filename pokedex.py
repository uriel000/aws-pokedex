import requests
import sys


def search_pokemon(name):
    response = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{name.lower()}/")
    try:
        result = response.json()
        print("Name: {}".format(result['name'].capitalize()))
        print("ID: {}".format(result['id']))
        print("Base XP: {}".format(result['base_experience']))
    except:
        print("Pokemon does not exist")


if __name__ == "__main__":
    search_pokemon(sys.argv[1])
