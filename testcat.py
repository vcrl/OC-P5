import requests

url = "https://fr.openfoodfacts.org/categories.json"
response = requests.get(url)
response = response.json()

for category in response['tags']:
    if category['name'] == 'Snacks':
        print(category['name'])
