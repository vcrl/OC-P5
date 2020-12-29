import sys
from time import sleep
from .menu_option1 import Menu_Option1
from .menu_option2 import Menu_Option2
from ..display.display import Display
from ..api.api import Api_Management
from ..database.db_exec import Database_Executions
from ..constants.constants import CATEGORIES, ERROR, MENU
from ..constants.constants import DB_HOST, DB_USER, DB_PSWD, DB_DB

class Main_Menu:
    def __init__(self):
        self.db = Database_Executions()
        self.display = Display()
        self.api = Api_Management()
        self.menu_1 = Menu_Option1()
        self.menu_2 = Menu_Option2()

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
                self.menu_1.option_1()
            
            if choice == '2':
                self.menu_2.option_2()

            if from_start:
                if choice == '3':
                    self.db.reset()
                    self.api.create_categories()
                    print("<La base de donnée a bien été réinitialisée.>")

            if choice == '0':
                print("<Merci d'avoir utilisé ce service. A bientôt !>")
                sleep(1)
                sys.exit()   