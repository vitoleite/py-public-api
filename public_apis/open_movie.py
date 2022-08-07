import requests
from pprint import pprint

class open_movie:

    def __init__(self) -> None:
        
        self._api_key = "30ee9376"
        self._movie = "Joker"

        self._url = f"http://www.omdbapi.com/?apikey={self._api_key}&t={self._movie}"
    
    def get_movie(self):
        req = requests.get(self._url).json()
        pprint(req)

if __name__ == "__main__":
    open_movie().get_movie()
