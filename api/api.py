import requests
from ..database.db_exec import Database_Executions
from ..constants.constants import CATEGORIES, PRODUCTS_NB
from ..constants.constants import DB_HOST, DB_USER, DB_PSWD, DB_DB

class Api_Management():
    def __init__(self):
        self.api_url = "https://fr.openfoodfacts.org/cgi/search.pl?action=process"
        self.db = Database_Executions()

    def payload(self, category, products_nb):
        payload = {
                'action': 'process',
                'tagtype_0': 'categories',
                'tag_contains_0': 'contains',
                'tag_0': category,
                'tagtype_1': 'nutrition_grade',
                'tag_contains_1': 'contains',
                'page_size': products_nb,
                'json': 'true',
                }
        return payload
    
    def return_api_as_json(self, category, products_nb):
        url_base = self.api_url
        response = requests.get(url_base, params=self.payload(category, products_nb))
        response = response.json()
        return response

    def create_categories(self):
        """
        Create db categories table
        """
        for category in CATEGORIES.values():
            cat_values_list = list(CATEGORIES.values())
            cat_keys_list = list(CATEGORIES.keys())
            self.db.execute_query(f"INSERT INTO category (name) VALUES ('{category}');")
            self.load_products(cat_keys_list, cat_values_list, category)

    def load_products(self, cat_keys_list, cat_values_list, category):
        """
        Fill products table
        """
        percentage_index = 0
        response = self.return_api_as_json(category, PRODUCTS_NB)
        position = cat_values_list.index(category)
        for product in response['products']:
            total = len(product)
            percentage_index += 1
            current_percentage = int(percentage_index / total * 100)
            self.db.printProgressBar(percentage_index, total, prefix=f'Chargement de: {category}')
            try:
                self.db.execute_query("INSERT INTO product (name, brand, description, shop, link, nutriscore, category_id) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (product['generic_name_fr'], product['brands'], product['ingredients_text_debug'], product['generic_name_fr'],
                        product['image_front_url'], product['nutriscore_grade'], cat_keys_list[position]))
                self.db.execute_query(f"DELETE FROM product WHERE name = '' OR description = '';")
            except KeyError:
                pass

            except IndexError:
                pass