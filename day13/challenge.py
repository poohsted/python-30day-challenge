"""This script fetches a random Pokémon's details from the PokeAPI.
Challenge: Pokémon API Fetcher

You’ll create a Python script that:

Picks a random Pokémon ID (1–151)

Sends a request to PokeAPI

Parses and prints the Pokémon’s name, height, and type(s)
"""
import requests
import random

def fetch_random_pokemon():
    # Generate a random Pokémon ID between 1 and 151
    pokemon_id = random.randint(1, 151)
    print(f"Fetching details for Pokémon ID: {pokemon_id}")

    # Send a request to the PokeAPI
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        name = data['name'].capitalize()
        height = data['height']
        types = [t['type']['name'] for t in data['types']]

        print(f"Pokémon Name: {name}")
        print(f"Height: {height}")
        print(f"Types: {', '.join(types)}")
    else:
        print("Failed to retrieve Pokémon details.")
        if __name__ == "__main__":
            fetch_random_pokemon()
