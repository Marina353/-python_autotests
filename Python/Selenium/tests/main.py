import requests

URL = 'https://api.pokemonbattle.ru/v2' 
TOKEN = '3cee5fbb67f73217e74cb5616729fb28'
HEADER = {'Content-Type' :'application/json','trainer_token' : TOKEN
}
body_registration = {
    "trainer_token": TOKEN,
    "email": "kolosok88@yandex.ru",
    "password": "Iloveqa1",
    "password_re": "Iloveqa1"
}
bodi_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 12
}

'''response = requests.post(url = f'{URL}/trainers/reg, headers = HEADER, json = bodi_registration
print(response.text)'''                         

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = bodi_confirmation)
print(response_confirmation.text)'''

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create )
print(response_create.text)

message = response_create.json()["message"] 
print(message)