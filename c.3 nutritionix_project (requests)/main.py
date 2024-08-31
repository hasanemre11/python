import requests
from datetime import datetime

text = input("Tell which exercise you did:")
weight = 60
height = 172
age = 21

parameters = {
    "query": text,
    "weight_kg": weight,
    "height_cm": height,
    "age": age
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

app_id = "fb515fe1"
api_key = "d41efd646b138ed9b755336c2cd17da6"
headers = {
    "x-app-id": app_id,
    "x-app-key": api_key
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

sheety_endpoint = "https://api.sheety.co/0d376b61ae0b2ad40aaa9025a71a8db9/myWorkouts/sayfa1"

date = datetime.now().strftime("%Y%m%d")
time = datetime.now().strftime("%X")

bearer_headers = {
    "Authorization": "Basic bnVsbDpudWxs"
}

for exercise in result["exercises"]:
    sheet_input = {
        "sayfa1": {
            "date": date,
            "time": time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories'],
        }
    }
    sheet_response = requests.post(url=sheety_endpoint, json=sheet_input, headers=bearer_headers)
    print(sheet_response.text)
