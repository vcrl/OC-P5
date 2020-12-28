# API information
CATEGORIES = {
    1: "Boissons",
    2: "Snacks",
    3: "Epicerie",
    4: "Conserves",
    5: "Desserts"
}
PRODUCTS_NB = 1;

# Errors
ERROR = {
    'invalid_choice' : "ERREUR: Votre choix est incorrect. Veuillez réessayer.",
    'connection_problem' : "ERREUR: Impossible d'accéder à la base de donnée. Vérifiez votre connexion internet et réessayez"
}

# Menus
MENU = {
    'main' : """
    ##########################################
    1. Quel aliment souhaitez-vous remplacer ?
    2. Retrouver mes aliments substitués.
    3. Réinitialiser la base de donnée.
    ##########################################
    Pour quitter le programme, tapez 0.
    <Entrez votre choix>
    """,

    'option_1' : f"""
    Sélectionnez une catégorie d'aliment
    ##########################################
    1. {CATEGORIES[1]}
    2. {CATEGORIES[2]}
    3. {CATEGORIES[3]}
    4. {CATEGORIES[4]}
    5. {CATEGORIES[5]}
    ##########################################
    Pour revenir au menu principal, tapez 0.
    <Entrez votre choix>
    """,

    'option_2' : f"""
    ##########################################
    Pour revenir au menu principal, tapez 0.
    <Entrez votre choix> 
    """,
}

# Database information
DB_HOST = "localhost"
DB_USER = "root"
DB_PSWD = "root"
DB_DB = "mydb"