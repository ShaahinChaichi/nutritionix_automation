import requests

url = "nutritionix.com"

headers = {
    "x-app-id": "a41d7881",
    "x-app-key": "0293ec30da232b1567f437a2a618f009",
    "x-remote-user-id": "0",
    "Content-Type": "application/json",
}

params = {
    "query": "ran 3 miles",
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}

NLP_endpoint = "/v2/search/instant"

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise",
                         json=params, headers=headers)

print(response.text)
