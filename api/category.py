"""
Module contenant la classe Category, qui gère
l'ajout des catégories en base de donnée
"""
import requests
from database.db_exec import Database_Executions
from api.api import Api_Management
from api.product import Product
from constants.constants import CATEGORIES, PRODUCTS_NB

class Category():
    """
    Classe permettant la création des catégories
    dans la base de donnée.
    Méthodes:
    * payload:
        - Définit les paramètres de récuparation
        des informations liées à l'API

    * return_api_as_json:
        - Renvoi la réponse de l'API au format
        JSON
    """
    def __init__(self):
        self.api = Api_Management()
        self.db = Database_Executions()
        self.product = Product()

    def create_categories(self):
        """
        Méthode permettant de créer les catégories 
        enregistrées dans le dictionnaire CATEGORIES
        dans la base de donnée.
        Renvoi ensuite les variables:
        cat_keys_list, cat_values_list, category
        à la méthode load_products de la classe
        Product.
        """

        for category in CATEGORIES.values():
            cat_values_list = list(CATEGORIES.values())
            cat_keys_list = list(CATEGORIES.keys())
            self.db.execute_query(f"INSERT INTO category (name) VALUES ('{category}');")
            self.product.load_products(cat_keys_list, cat_values_list, category)