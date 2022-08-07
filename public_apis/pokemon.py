import requests

class pokemon:

    def __init__(self) -> None:
        self._url = "https://pokeapi.co/api/v2/pokemon/"

    def get_pokemon(self, pokemon:str = str):
        url_final = f"{self._url}{pokemon}"
        req = requests.get(url_final).json()
        print(req["species"])

if __name__ == "__main__":
    pokemon().get_pokemon(pokemon="charizard")