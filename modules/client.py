import requests

class PetShop:
    BASE_URL = "https://petstore.swagger.io/v2"

    def __init__(self):
        self.session = requests.Session()

    def get_request(self, url: str, params: dict):
        url = self.BASE_URL + '/' + url
        return self.session.get(url, params=params)

    def post_request(self, url: str, data):
        url = self.BASE_URL + '/' + url
        return self.session.post(url, json=data)

    def put_request(self, url: str, data):
        url = self.BASE_URL + '/' + url
        return self.session.put(url, json=data)

    def delete_request(self, url: str):
        url = self.BASE_URL + '/' + url
        return self.session.delete(url)

