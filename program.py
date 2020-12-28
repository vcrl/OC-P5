import sys
from time import sleep
import mysql.connector as mysql
from database import Database_Executions
from constants import CATEGORIES, ERROR, MENU

class Menu:
    def __init__(self):
        self.show_main_menu()

    def show_main_menu(self):
        menu_choice = ['0', '1', '2', '3']
        menu = MENU['main'] # Menu principal
        while True:
            choice = ""
            while choice not in menu_choice:
                choice = input(menu)
                if choice not in menu_choice:
                    print(ERROR['invalid_choice'])
            
            if choice == "1":
                self.option_1()
            
            if choice == "2":
                self.option_2()
            
            if choice == "3":
                db = Database_Executions()
                db.create_from_api()

            if choice == "0":
                print("<A bientôt !>")
                sleep(1)
                sys.exit()
    
    def option_1(self):
        menu_choice = ['0', '1', '2', '3', '4', '5']
        menu = MENU['option_1']
        while True:
            choice = ""
            while choice not in menu_choice:
                choice = input(menu)
                if choice not in menu_choice:
                    print(ERROR['invalid_choice'])
            if choice == "1":
                pass # Liste de produits affichés

    def option_2(self):
        menu_choice = ['0']
        menu = MENU['option_2']
        while True:
            choice = ""
            while choice not in menu_choice:
                print(
                """
                Voici la liste de vos aliments substitués
                ##########################################
                """
                )
                db = mysql.connect(host="localhost", user="root", password="root", database="mydb") # config
                cursor = db.cursor(buffered=True)
                cursor.execute("SELECT * FROM product")
                result = cursor.fetchall()
                for x in result:
                    print(x[0])
                choice = input(menu)
                if choice not in menu_choice:
                    print(ERROR['invalid_choice'])
                
            if choice == "0":
                self.show_main_menu()
            
        
            