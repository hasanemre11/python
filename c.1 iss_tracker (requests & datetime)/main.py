import requests
from datetime import datetime


parameters = {"lat": 41.062631, "lng": 28.984442}

data = requests.get("https://api.sunrise-sunset.org/json", params=parameters).json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise, sunset)


time_now = datetime.now()
print(time_now)