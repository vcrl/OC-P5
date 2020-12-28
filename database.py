import mysql.connector as mysql
import requests
from constants import CATEGORIES, PRODUCTS_NB

class Database_Executions:
    """
        Database management class.

        *Methods:
            - create_from_api:
                Create the database from an SQL file.
                Add categories & products into the...
                ...database from the API.
        """
    def __init__(self):
        self.db = mysql.connect(host="localhost", user="root", password="root", database="mydb") # config
        self.cursor = self.db.cursor(buffered=True)

    def create_from_api(self):
        # Create from sql file
        with open('db.sql', 'r') as f:
            split_queries = f.read().split(';')
            for command in split_queries:
                if command.strip():
                    self.cursor.execute(command)
            self.db.commit()
            self.cursor.close()

        #Categories
        for category in CATEGORIES.values():
            cat_values_list = list(CATEGORIES.values())
            cat_keys_list = list(CATEGORIES.keys())
            cursor = self.db.cursor(buffered=True)
            cursor.execute(f"INSERT INTO category (name) VALUES ('{category}');")
            self.db.commit()
            payload = {
                'action': 'process',
                'tagtype_0': 'categories',
                'tag_contains_0': 'contains',
                'tag_0': category,
                'tagtype_1': 'nutrition_grade',
                'tag_contains_1': 'contains',
                'page_size': PRODUCTS_NB,
                'json': 'true',
                }

            url_base = "https://fr.openfoodfacts.org/cgi/search.pl?action=process"
            response = requests.get(url_base, params=payload)
            response = response.json()
            position = cat_values_list.index(category)
            percentage_index = 0
            for product in response['products']:
                total = len(product)
                percentage_index += 1
                current_percentage = int(percentage_index / total * 100)
                self.printProgressBar(percentage_index, total, prefix=f'Chargement de: {category}', suffix='\n')
                if product: #Check si l'élement est vide
                    try:
                        cursor.execute(f"INSERT INTO product (name, brand, description, shop, link, nutriscore, category_id) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                        (product['generic_name_fr'], product['brands'], product['ingredients_text_debug'], product['generic_name_fr'],
                        product['image_front_url'], product['nutriscore_grade'], cat_keys_list[position]))
                        self.db.commit()
                    except KeyError:
                        pass

                    except IndexError:
                        pass
            cursor.close()

        print("<La base de donnée a bien été réinitialisée.>")

    def printProgressBar (self, iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '#', printEnd = "\r"):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
        if iteration == total: 
            print('\n')