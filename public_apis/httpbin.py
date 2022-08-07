import requests
from requests.auth import HTTPBasicAuth

class httpbin:

    def __init__(self):
        # GET
        self._get_payload = {'page': 2, 'count': 25}
        self._get_url = "https://httpbin.org/get"
        
        # POST
        self._post_payload = {'username': 'vitor', 'password': 'testing'}
        self._post_url = "https://httpbin.org/post"

        # AUTH
        self._auth_user = "vitor"
        self._auth_passwd = "12345"
        self._auth_url = f"https://httpbin.org/basic-auth/{self._auth_user}/{self._auth_passwd}"

        # DYNAMIC DATA
        self._dynamic_url = "https://httpbin.org/delay/2"

        # IMAGE
        self._image_url = "https://httpbin.org/image/png"


    def get_response(self):
        print("GET")
        re = requests.get(url=self._get_url, params=self._get_payload)
        print(re.url)
        print(re.status_code)

    def post_response(self):
        print("POST")
        response = requests.post(url=self._post_url, data=self._post_payload)
        re_dict = response.json()
        print(re_dict['form'])

    def auth_response(self):
        print("AUTH")
        req = requests.get(url=self._auth_url, auth=(self._auth_user, self._auth_passwd))

        print(req.status_code)
        print(req.json())
    
    def dynamic_data(self):
        print("DYNAMIC DATA")

        # Wait 3 seconds to return output
        re = requests.get(self._dynamic_url, timeout=3)
        print(re)
    
    def image(self):
        print("DOWNLOAD IMAGE")
        req = requests.get(self._image_url)

        with open("output/httpbin_image.png", "wb") as f:
            for chunk in req.iter_content(chunk_size=128):
                f.write(chunk)


if __name__ == "__main__":
    httpbin().get_response()
    httpbin().post_response()
    httpbin().auth_response()
    httpbin().dynamic_data()
    httpbin().image()