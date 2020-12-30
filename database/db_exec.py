import mysql.connector as mysql
import requests
from constants.constants import CATEGORIES, PRODUCTS_NB
from constants.constants import DB_HOST, DB_USER, DB_PSWD, DB_DB

class Database_Executions:
    """
    Classe permettant la gestion des requêtes à/sur la
    base de donnée.
    Méthodes:
    * execute_query:
        - Exécute une query SQL, sans retourner les
        valeurs retournées

    * execute_query_with_return:
        - Exécute une query SQL, en retournant les
        valeurs retournées pour un accès aux données
    
    * reset:
        - Permet de réinitialiser la base de donnée,
        en exécutant le fichier db.sql
    
    * printProgressBar:
        - Permet l'affichage d'une bar de chargement
        lors de la réinitialisation de la base de donnée
    """
    def __init__(self):
        self.db = mysql.connect(host=DB_HOST, user=DB_USER, password=DB_PSWD, database=DB_DB)

    def execute_query(self, query, data=None):
        """
        Méthode permettant d'exécuter une requête
        SQL simple.

        Arguments:
        * query:
            - Permet de récupérer la requête afin de
            l'exécuter.
        
        * data=None:
            - Permet de récupérer ou non des données
            suplémentaires pour la requête. (passage
            de variables, etc.)
        """

        cursor = self.db.cursor(buffered=True)
        cursor.execute(f"{query}", data)
        self.db.commit()
        cursor.close()
    
    def execute_query_with_return(self, query, data=None):
        """
        Méthode permettant d'exécuter une requête
        SQL simple et de retourner les informations.

        Arguments:
        * query:
            - Permet de récupérer la requête afin de
            l'exécuter.
        
        * data=None:
            - Permet de récupérer ou non des données
            suplémentaires pour la requête. (passage
            de variables, etc.)
        """

        cursor = self.db.cursor(buffered=True)
        cursor.execute(f"{query}")
        self.db.commit()
        return cursor.fetchall()
        cursor.close()

    def reset(self):
        """
        Méthode permettant de réinitialiser la
        base de donnée.
        """

        cursor = self.db.cursor(buffered=True)
        with open('.\database\db.sql', 'r') as f:
            split_queries = f.read().split(';')
            for command in split_queries:
                if command.strip():
                    cursor.execute(command)
            self.db.commit()
            cursor.close()
    
    def printProgressBar(self, iteration, total, prefix = '', suffix = '', length = 20, fill = '#', printEnd = "\r"):
        """
        Méthode permettant d'afficher une barre
        de chargement à la réinitialisation de
        la base de donnée.

        Arguments:
        * iteration:
            - Récupère le nombre d'itération d'une
            même variable.
        
        * total:
            - Récupère le nombre total de données à
            traiter
        
        * prefix = '':
            - Ajoute une prefix avant la bar de chargement.
        
        * suffix = '':
            - Ajoute une suffix après la bar de chargement.
        
        * length = 100:
            - Nombre de caractère que contient la barre.
        
        * fill = '#':
            - Caractère à utiliser pour le remplissage de
            la barre
        
        * printEnd = "\r":
            - Caractère à ajouter à la fin de la barre
        """

        current = (f"{suffix}")
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '.' * (length - filledLength)
        print(f'\r{prefix} [{bar}] {current}', end = printEnd)