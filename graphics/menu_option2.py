from constants.constants import MENU, ERROR
from graphics.main_menu import Main_Menu

class Menu_Option2:
    def __init__(self):
        self.main = Main_Menu()

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
                result = self.main.db.execute_query_with_return("SELECT * FROM substitute;")
                for x in result:
                    old_product = self.main.db.execute_query_with_return(
                        f"""
                        SELECT * FROM product WHERE product_id={x[0]};
                        """
                    )
                    substitute = self.main.db.execute_query_with_return(
                        f"""
                        SELECT * FROM product WHERE product_id={x[1]};
                        """
                    )
                    self.main.display.display_subtitutes(
                        old_product[0][1], old_product[0][2], old_product[0][6],
                        substitute[0][1], substitute[0][2], substitute[0][6]
                    )
                choice = input(menu)
                if choice not in menu_choice:
                    print(ERROR["invalid_choice"])
                
            if choice == "0":
                self.main.show_main_menu()