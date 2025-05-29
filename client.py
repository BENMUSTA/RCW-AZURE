import requests

url='http://localhost:8000/'

reponse = requests.get(url)
reponse = reponse.json()

print(reponse['message'])