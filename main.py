import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = "84"
HEIGHT_CM = "174"
AGE = "49"

APP_ID = os.environ.get("API_ID")
API_KEY = os.environ.get("API_KEY")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/58298ae4a7485b0180431fd0c48a8e5d/myWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # No Auth
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)
