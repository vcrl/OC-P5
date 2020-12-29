from ..constants.constants import MENU, ERROR
from .main_menu import Main_Menu

class Menu_Option1:
    def __init__(self):
        self.main = Main_Menu()

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
        result = self.main.db.execute_query_with_return(
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
                    self.main.display.display_products(
                        x[0], x[1], x[2], x[6]
                    )
                    menu_choice.append(str(x[0]))
                menu_choice.append('0')
                choice = input(MENU["option_1_2"])
                if choice not in menu_choice:
                    print(ERROR['invalid_choice'])
            if choice == "0":
                self.main.show_main_menu(from_start=False)
            
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
        for i in range(50):
            print(product_name[0])
        result = self.main.db.execute_query_with_return(
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
                    self.main.display.display_products(
                        x[0], x[1], x[2], x[6]
                    )
                    menu_choice.append(str(x[0]))
                menu_choice.append('0')
                choice = input(MENU["option_1_2_1"])
                if choice not in menu_choice:
                    print(ERROR['invalid_choice'])

            if choice == "0":
                self.main.show_main_menu(from_start=False)
            
            if choice in menu_choice:
                self.main.db.execute_query(f"INSERT INTO substitute (product_id, substitute_id) VALUES ({product_id}, {choice});")
                print("<La sélection a bien été enregistrée.>")
                self.main.show_main_menu(from_start=False)