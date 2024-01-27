import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 60
HEIGHT_CM = 180
AGE = 24

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

USERNAME = "parth"
PASSWORD = os.environ["PASSWORD"]

endpoint = os.environ["endpoint"]
sheet_endpoint = os.environ["sheet_endpoint"]

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

response = requests.post(endpoint, json=parameters, headers=headers)
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

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)

#Basic Authentication
sheet_response = requests.post(
  sheet_endpoint,
  json = sheet_inputs,
  auth=(
      PASSWORD,
      USERNAME,
  )
)

