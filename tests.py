import mysql.connector as mysql
import requests
from requests.api import request
import json
#db = mysql.connect(host="localhost", user="root", password="root", database="test")
#cursor = db.cursor(buffered=True)
#cursor.execute(f"INSERT INTO Subtitute (product_id, substitute_id) VALUES (1 #id du premier produit select, 2 #id du deuxième produit select)
#db.commit()

"nutriscore_grade"
"nutriscore_score"
"generic_name_fr"
"ingredients_text_debug"
"image_front_url"
"stores_tags"


payload = {
    'action': 'process',
    'tagtype_0': 'categories',
    'tag_contains_0': 'contains',
    'tag_0': category,
    'tagtype_1': 'nutrition_grade',
    'tag_contains_1': 'contains',
    'page_size': nb,
    'json': 'true',
    }

url_base = "https://fr.openfoodfacts.org/cgi/search.pl?action=process"
response = requests.get(url_base, params=payload)
response = response.json()


for product in response['products']:
    print("Produit:" + str(product["generic_name_fr"]))
    print("Nutriscore :" + str(product["nutriscore_grade"]))
    print(product["stores_tags"])