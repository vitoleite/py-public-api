import requests

class random_advices:

    def __init__(self) -> None:
        self._url = "https://api.adviceslip.com/advice"
    
    def get_random_advice(self):
        req = requests.get(self._url).json()
        print(req)

    def get_advice_id(self):
        url_final = f"{self._url}/{91}"
        req = requests.get(url_final).json()
        print(req)

if __name__ == "__main__":
    random_advices().get_random_advice()
    random_advices().get_advice_id()
    