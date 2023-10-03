import requests
import sys

# COMMAND TO ACTIVATE Virtual Environment in Git Bash "source venv/Scripts/Activate"


def search_pokemon(name):
    response = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{name.lower()}/")
    try:
        result = response.json()
        pokeAbility = []
        pokeItems = []
        print("\n====================================")
        print("Name: {}".format(result['name'].capitalize()))
        print("HP: {}".format(result['stats'][0]['base_stat']))
        abilities = result['abilities']
        held_items = result['held_items']

        for ability in abilities:
            pokeAbility.append(ability['ability']['name'].capitalize())
        held_items = result['held_items']
        for item in held_items:
            pokeItems.append(item['item']['name'].capitalize())

        if (len(pokeAbility) > 1):
            print("Attacks: {}, {}".format(
                ", ".join(pokeAbility[:-1]), pokeAbility[-1]))
        else:
            print("Attack: {}".format(pokeAbility[-1]))

        if (len(pokeItems) == 1):
            print("Held Item: {}".format(pokeItems[-1]))
        elif (len(pokeItems) > 1):
            print("Held Items: {}, {}".format(
                ", ".join(pokeItems[:-1]), pokeItems[-1]))
        else:
            print("Held Items: No held items.")

        print("====================================")

    except:
        print(f"\n{name} does not exist. Please try again")


if __name__ == "__main__":
    play = 'y'
    while (play.lower() == 'y'):
        pokeName = input("Search Pokemon: ")
        search_pokemon(pokeName)
        play = input("\nDo you want to search again? Type Y if yes: ")
    else:
        print("Thank you. Bye!")
