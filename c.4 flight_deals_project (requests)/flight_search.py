import requests
from datetime import datetime, timedelta
from pprint import pprint

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
apikey = "4XhsaVG-laFGMPt_9ipCrJ3UasnuPekJ"
headers = {"apikey": apikey}


class FlightSearch:

    def __init__(self):
        self.today = datetime.now().date()
        self.tomorrow = (self.today + timedelta(days=1)).strftime("%d/%m/%Y")
        self.six_month_later = (self.today + timedelta(days=180)).strftime("%d/%m/%Y")

    def search(self, city):
        parameters = {
            "fly_from": "IST",
            "fly_to": city,
            "date_from": self.tomorrow,
            "date_to": self.six_month_later,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=parameters, headers=headers)
        try:
            data = response.json()["data"][0]
            return data
        except:
            print(f"No flights found for {city}")

