"""
Module contenant la classe Api_Management, qui gère
les requêtes à l'API d'OpenFoodFact
"""
import requests
from database.db_exec import Database_Executions
from constants.constants import CATEGORIES, PRODUCTS_NB

class Api_Management():
    """
    Classe permettant la gestion des requêtes API.
    Méthodes:
    * payload:
        - Définit les paramètres de récuparation
        des informations liées à l'API

    * return_api_as_json:
        - Renvoi la réponse de l'API au format
        JSON
    """
    def __init__(self):
        self.api_url = "https://fr.openfoodfacts.org/cgi/search.pl?action=process"
        self.db = Database_Executions()

    def payload(self, category, products_nb):
        """
        Méthode définissant les paramètres à passer à l'API
        pour la récupération des données.
        Arguments:
        * category:
            - Permet de passer une variable category contenant
            les différentes catégories à utiliser
        
        * products_nb:
            - Permet de passer une variable products_nb contenant
            le nombre de produits à requêter à l'API
        
        Return:
        Le dictionnaire payload, contenant tous les paramètres
        à passer à l'API.
        """

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
        """
        Méthode retournant les données de l'API au format
        JSON.
        Arguments:
        * category:
            - Permet de passer une variable category contenant
            les différentes catégories à utiliser
        
        * products_nb:
            - Permet de passer une variable products_nb contenant
            le nombre de produits à requêter à l'API
        
        Return:
        La variable reponse contenant la réponse API au format
        JSON.
        """

        url_base = self.api_url
        response = requests.get(url_base, params=self.payload(category, products_nb))
        response = response.json()
        return response