#proba get - pobieranie api strony
#pip3 install requests - instalowanie requests
import requests

response = requests.get('https://www.google.com')
print(response.status_code) #czy dziala api
print(response.text)
