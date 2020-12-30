# Dictionnaire contenant les catégories de produit à utiliser selon leur ID
# Ce dictionnaire est récupéré par le module api.py
CATEGORIES = {
    1: "Boissons",
    2: "Snacks",
    3: "Epicerie",
    4: "Conserves",
    5: "Desserts"
}
PRODUCTS_NB = 150

# Dictionnaire contenant les messages d'erreurs à utiliser selon leur ID
# Il ne s'agit que de la partie graphique
ERROR = {
    'invalid_choice' : "ERREUR: Votre choix est incorrect. Veuillez réessayer.",
    'connection_problem' : "ERREUR: Impossible d'accéder à la base de donnée. Vérifiez votre connexion internet et réessayez"
}

# Dictionnaire contenant la partie graphique des menus selon leur ID
# L'ID des dictionnaire correspond à une méthode du module menus.py
MENU = {
    'main_from_start' : """
    ####################################################################################
    1. Quel aliment souhaitez-vous remplacer ?
    2. Retrouver mes aliments substitués.
    3. Réinitialiser la base de donnée.
    ####################################################################################
    Pour quitter le programme, tapez 0.
    <Entrez votre choix>
    """,

'!main_from_start' : 
    """
    ####################################################################################
    1. Quel aliment souhaitez-vous remplacer ?
    2. Retrouver mes aliments substitués.
    ####################################################################################
    Pour quitter le programme, tapez 0.
    Pour réinitialiser la base de donnée,
    relancez le programme.
    <Entrez votre choix>
    """,

'option_1' : 
    f"""
    Sélectionnez une catégorie d'aliment
    ####################################################################################
    1. {CATEGORIES[1]}
    2. {CATEGORIES[2]}
    3. {CATEGORIES[3]}
    4. {CATEGORIES[4]}
    5. {CATEGORIES[5]}
    ####################################################################################
    Pour revenir au menu principal, tapez 0.
    <Entrez votre choix>
    """,

'option_1_2' : 
    f"""
    ####################################################################################
    Sélectionnez un produit par son ID pour
    voir ses substituts.
    -
    Pour revenir au menu principal, tapez 0.
    <Entrez votre choix>
    """,

'option_1_2_1' : 
    f"""
    ####################################################################################
    Voici les substituts de votre produit.
    Sélectionnez un ID pour enregistrer le
    substitut dans la base de donnée.
    -
    Pour revenir au menu principal, tapez 0.
    <Entrez votre choix>
    """,

'option_2_1': 
    """
    Voici la liste de vos aliments substitués
    ####################################################################################
    """,

'option_2_2' : 
    """
    ####################################################################################
    Pour revenir au menu principal, tapez 0.
    <Entrez votre choix> 
    """,
}

# Variables contenant les informations de connexion à la base de donnée
# Ces informations sont modifiables librement par l'utilisateur sauf DB_DB
# Seul le module db.exec.py a accès à ces informations
DB_HOST = "localhost"
DB_USER = "root"
DB_PSWD = "root"
# ! Ne pas modifier la variable DB_DB !
DB_DB = "mydb"