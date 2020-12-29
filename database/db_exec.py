import mysql.connector as mysql
import requests
from ..constants.constants import CATEGORIES, PRODUCTS_NB
from ..constants.constants import DB_HOST, DB_USER, DB_PSWD, DB_DB

class Database_Executions:
    def __init__(self):
        self.db = mysql.connect(host=DB_HOST, user=DB_USER, password=DB_PSWD, database=DB_DB)

    def execute_query(self, query, data=None):
        cursor = self.db.cursor(buffered=True)
        cursor.execute(f"{query}", data)
        self.db.commit()
        cursor.close()
    
    def execute_query_with_return(self, query):
        cursor = self.db.cursor(buffered=True)
        cursor.execute(f"{query}")
        self.db.commit()
        return cursor.fetchall()
        cursor.close()

    def reset(self):
        cursor = self.db.cursor(buffered=True)
        with open('db.sql', 'r') as f:
            split_queries = f.read().split(';')
            for command in split_queries:
                if command.strip():
                    cursor.execute(command)
            self.db.commit()
            cursor.close()
    
    def printProgressBar(self, iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '#', printEnd = "\r"):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)