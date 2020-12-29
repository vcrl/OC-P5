import sys
from time import sleep
from graphics.display import Display
from api.api import Api_Management
from database.db_exec import Database_Executions
from constants.constants import CATEGORIES, ERROR, MENU
from constants.constants import DB_HOST, DB_USER, DB_PSWD, DB_DB

class Menus:
    def __init__(self):
        self.db = Database_Executions()
        self.display = Display()
        self.api = Api_Management()

    def show_main_menu(self, from_start=True):
        menu_choice = ['0', '1', '2', '3']
        if not from_start:
            menu = MENU["!main_from_start"] # Menu principal
        menu = MENU["main_from_start"]
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

            if from_start:
                if choice == '3':
                    self.db.reset()
                    self.api.create_categories()
                    print("<La base de donnée a bien été réinitialisée.>")

            if choice == '0':
                print("<Merci d'avoir utilisé ce service. A bientôt !>")
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
                self.show_main_menu(from_start=False)
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
        result = self.db.execute_query_with_return(
            f"""
            SELECT * FROM product
            WHERE category_id={category}
            AND NOT nutriscore = 'a'
            AND NOT nutriscore = 'b'
            ORDER BY nutriscore;
            """
            )
        menu_choice = []
        while True:
            choice = ""
            while choice == "":
                for x in result:
                    self.display.display_products(
                        x[0], x[1], x[2], x[6]
                    )
                    menu_choice.append(str(x[0]))
                menu_choice.append('0')
                choice = input(MENU["option_1_2"])
                if choice not in menu_choice:
                    print(ERROR['invalid_choice'])
            if choice == "0":
                self.show_main_menu(from_start=False)
            
            if choice in menu_choice:
                self.option_1_2_1(choice, x[1], category)
    
    def option_1_2_1(self, product_id, product_name, category):
        """
        Affichage des substituts du produit
        -> L'utilisateur doit saisir un ID
        -> Enregistrement dans la BDD substitut
        -> Msg de confirmation
        -> Retour au menu
        """
        product_name = product_name.split()
        result = self.db.execute_query_with_return(
            f"""
            SELECT * FROM product 
            WHERE category_id={category} 
            AND name LIKE '{product_name[0]}%'
            AND nutriscore = 'a' OR nutriscore = 'b' 
            ORDER BY nutriscore;
            """
            )
        menu_choice = []
        while True:
            choice = ""
            while choice == "":
                for x in result:
                    self.display.display_products(
                        x[0], x[1], x[2], x[6]
                    )
                    menu_choice.append(str(x[0]))
                menu_choice.append('0')
                choice = input(MENU["option_1_2_1"])
                if choice not in menu_choice:
                    print(ERROR['invalid_choice'])

            if choice == "0":
                self.show_main_menu(from_start=False)
            
            if choice in menu_choice:
                self.db.execute_query(f"INSERT INTO substitute (product_id, substitute_id) VALUES ({product_id}, {choice});")
                print("<La sélection a bien été enregistrée.>")
                self.show_main_menu(from_start=False)

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
                result = self.db.execute_query_with_return("SELECT * FROM substitute;")
                for x in result:
                    old_product = self.db.execute_query_with_return(
                        f"""
                        SELECT * FROM product WHERE product_id={x[0]};
                        """
                    )
                    substitute = self.db.execute_query_with_return(
                        f"""
                        SELECT * FROM product WHERE product_id={x[1]};
                        """
                    )
                    self.display.display_subtitutes(
                        old_product[0][1], old_product[0][2], old_product[0][6],
                        substitute[0][1], substitute[0][2], substitute[0][6]
                    )
                choice = input(menu)
                if choice not in menu_choice:
                    print(ERROR["invalid_choice"])
                
            if choice == "0":
                self.show_main_menu()