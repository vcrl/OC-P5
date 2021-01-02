"""
Module contenant la classe Product, qui gère
l'ajout des produits en base de donnée
"""
import requests
from database.db_exec import Database_Executions
from api.api import Api_Management
from constants.constants import CATEGORIES, PRODUCTS_NB

class Product():
    """
    Classe permettant l'ajout des produits
    dans la base de donnée.
    Méthodes:
    * load_product:
        - Ajoute les produits dans la base
        de donnée

    """
    def __init__(self):
        self.api = Api_Management()
        self.db = Database_Executions()

    def load_products(self, cat_keys_list, cat_values_list, category):
        """
        Méthode permettant l'ajout de produits à la base donnée
        en fonction de leur catégorie.
        Arguments:
        * cat_keys_list:
            - Variable passée par la méthode create_categories de
            la classe Category, contenant toutes les clés du 
            dictionnaire CATEGORY.
        
        * cat_values_list:
            - Variable passée par la méthode create_categories de
            la classe Category, contenant toutes les valeurs du 
            dictionnaire CATEGORY.
        
        * category:
            - Variable passée par la méthode create_categories de
            la classe Category, contenant l'index des catégories.
        """

        percentage_index = 0
        response = self.api.return_api_as_json(category, PRODUCTS_NB)
        position = cat_values_list.index(category)
        for product in response['products']:
            total = len(product)
            percentage_index += 1
            #current_percentage = int(percentage_index / total * 100)
            self.db.printProgressBar(percentage_index, total, prefix=f'Chargement...', suffix=category)
            try:
                self.db.execute_query("INSERT INTO product (name, brand, description, shop, link, nutriscore, category_id) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (product['generic_name_fr'], product['brands'], product['ingredients_text_debug'], product['stores'],
                        product['image_front_url'], product['nutriscore_grade'], cat_keys_list[position]))
                self.db.execute_query(f"DELETE FROM product WHERE name = '' OR description = '';")
            except KeyError:
                pass

            except IndexError:
                pass