import requests

url = 'http://localhost:8000/team/?addreass= &date= &gamename='

response = requests.get(url)

if response.ok:
    reversed_string = response.json()
    print(reversed_string)
else:
    print('API error:', response.status_code)