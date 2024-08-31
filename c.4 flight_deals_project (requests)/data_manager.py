import requests
from pprint import pprint


class DataManager:

    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co/0d376b61ae0b2ad40aaa9025a71a8db9/flightDeals/flight"
        self.basic_headers = {
            "Authorization": "Bearer dnakdgaa"
        }
        self.data = requests.get(url=self.sheety_endpoint, headers=self.basic_headers).json()

        pprint(self.data)

    def edit_row(self, param, c):
        response = requests.put(url=f"{self.sheety_endpoint}/{c}", json=param, headers=self.basic_headers)
        print(response.text)




