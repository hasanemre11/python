import requests

parameters = {"lat": 41.062631, "lng": 28.984442}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)

if response.status_code == 200:
    print(response.json())
else:
    print("Failed to fetch data. Status code:", response.status_code)
