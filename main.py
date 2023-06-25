import requests

question = input("Tell me which exersice you did: ")

headers = {
    "x-app-id": "a41d7881",
    "x-app-key": "0293ec30da232b1567f437a2a618f009",
    "x-remote-user-id": "0",
    "Content-Type": "application/json",
}

params = {
    "query": question,
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}

url = "https://trackapi.nutritionix.com/v2"
NLP_endpoint = "/natural/exercise"

response = requests.post(url=f"{url}{NLP_endpoint}",
                         json=params, headers=headers)

with open("data.json", mode="w") as file:
    file.write(response.text)

print(response.text)
