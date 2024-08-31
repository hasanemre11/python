import data_manager
import requests
from flight_search import FlightSearch

data_manage = data_manager.DataManager()
sheet_data = data_manage.data['flight']

f = FlightSearch()


cities = ["CDG", "BER", "NRT", "ICN", "CAI"]
index = -1
for city in cities:
    index += 1
    data = f.search(city)
    now_price = data["price"]
    destination = data['cityTo']
    if now_price < sheet_data[index]["lowestPrice"]:
        parameters = {
            "flight": {
                 'city': sheet_data[index]['city'],
                 'iataCode': sheet_data[index]['iataCode'],
                 'lowestPrice': now_price
            }
        }
        data_manage.edit_row(param=parameters, c=sheet_data[index]["id"])
