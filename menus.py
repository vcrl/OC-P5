import sys
from time import sleep
import mysql.connector as mysql
from database import Database_Executions
from constants import CATEGORIES, ERROR, MENU
from constants import DB_HOST, DB_USER, DB_PSWD, DB_DB

class Menu:
    def __init__(self):
        self.show_main_menu()

    def show_main_menu(self):
        menu_choice = ['0', '1', '2', '3']
        menu = MENU["main"] # Menu principal
        while True:
            choice = ""
            while choice not in menu_choice:
                choice = input(menu)
                if choice not in menu_choice:
                    print(ERROR["invalid_choice"])
            
            if choice == '1':
                self.option_1()
            
            if choice == '2':
                self.option_2()
            
            if choice == '3':
                db = Database_Executions()
                db.create_from_api()

            if choice == '0':
                print("<A bientôt !>")
                sleep(1)
                sys.exit()
    
    def option_1(self):
        """
        L'utilisateur choisit une catégorie
        -> ça passe a option 1_2 une fois choisie
        """
        menu_choice = ['0', '1', '2', '3', '4', '5']
        menu = MENU['option_1']
        while True:
            choice = ""
            while choice not in menu_choice:
                choice = input(menu)
                if choice not in menu_choice:
                    print(ERROR["invalid_choice"])
            if choice == '0':
                self.show_main_menu()
            for option in menu_choice:
                if choice == option:
                    self.option_1_2(option)
                    break

    def option_1_2(self, category):
        """
        Affichage des produits de la catégorie
        -> L'utilisateur doit saisir un ID
        -> option_1_2_1
        """
        db = mysql.connect(host=DB_HOST, user=DB_USER, password=DB_PSWD, database=DB_DB) # config
        cursor = db.cursor(buffered=True)
        cursor.execute(f"SELECT * FROM product WHERE category_id={category}")
        result = cursor.fetchall()

        menu_choice = []
        while True:
            choice = ""
            while choice == "":
                print("####################################################################################")
                for x in result:
                    print("____________________________________________________________________________________")
                    print(f"ID: {x[0]} | NOM: {x[1]} | MARQUE: {x[2]} | NUTRISCORE: {str(x[6]).capitalize()}")
                    menu_choice.append(str(x[0]))
                choice = input(MENU["option_1_2"])
                if choice not in menu_choice:
                    print(ERROR['invalid_choice'])
            if choice == "0":
                self.show_main_menu()
            
            if choice in menu_choice:
                self.option_1_2_1(choice, category)
    
    def option_1_2_1(self, product_id, category):
        """
        Affichage des substituts du produit
        -> L'utilisateur doit saisir un ID
        -> Enregistrement dans la BDD substitut
        -> Msg de confirmation
        -> Retour au menu
        """
        db = mysql.connect(host=DB_HOST, user=DB_USER, password=DB_PSWD, database=DB_DB) # config
        cursor = db.cursor(buffered=True)
        cursor.execute(f"SELECT * FROM product WHERE category_id={category} AND nutriscore = 'a'")
        result = cursor.fetchall()
        cursor.close()

        menu_choice = []
        while True:
            choice = ""
            while choice == "":
                print("####################################################################################")
                for x in result:
                    print("____________________________________________________________________________________")
                    print(f"ID: {x[0]} | NOM: {x[1]} | MARQUE: {x[2]} | NUTRISCORE: {str(x[6]).capitalize()}")
                    menu_choice.append(str(x[0]))
                choice = input(MENU["option_1_2_1"])
                if choice not in menu_choice:
                    print(ERROR['invalid_choice'])

            if choice == "0":
                self.show_main_menu()
            
            if choice in menu_choice:
                cursor = db.cursor(buffered=True)
                cursor.execute(f"INSERT INTO substitute (product_id, substitute_id) VALUES (%s, %s)", (product_id, choice))
                db.commit()
                cursor.close()
                self.show_main_menu()


    def option_2(self):
        """
        Affichage des substituts enregistrés
        -> Retour au menu
        """
        menu_choice = ['0']
        menu = MENU["option_2_2"]
        while True:
            choice = ""
            while choice not in menu_choice:
                print(MENU["option_2_1"])
                db = mysql.connect(host=DB_HOST, user=DB_USER, password=DB_PSWD, database=DB_DB) # config
                cursor = db.cursor(buffered=True)
                cursor.execute("SELECT * FROM substitute")
                result = cursor.fetchall()
                for x in result:
                    print("____________________________________________________________________________________")
                    print(f"Produit ID: {x[0]} | Subtitut ID: {x[1]}")
                choice = input(menu)
                if choice not in menu_choice:
                    print(ERROR["invalid_choice"])
                
            if choice == "0":
                self.show_main_menu()
            
        
            