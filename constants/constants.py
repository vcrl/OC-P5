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
    'connection_problem' : "ERREUR: Impossible d'accéder à la base de donnée. Vérifiez votre connexion internet et réessayez",
    'no_products' : "ERREUR: Aucun produit ne correspond à votre recherche. Veuillez réessayer!",
    'empty': "C'EST BIEN VIDE : Quand vous aurez sélectionné des aliments à substituer, ils seront affichés ici."
}

# Dictionnaire contenant la partie graphique des menus selon leur ID
# L'ID des dictionnaire correspond à une méthode du module menus.py
MENU = {
    'main_from_start' : """
    --------------------------------------------------------
    BIENVENUE SUR L'OUTIL OPENFOODFACTS !
    Grâce à cet outil, vous pourrez remplacer des aliments
    mauvais pourr la santé, par des aliments plus sains.
    --------------------------------------------------------
    * Sélectionnez une option parmi les suivantes :
    --------------------------------------------------------

    1. Remplacer un aliment par un substitut sain.
    2. Retrouver mes aliments substitués.
    3. Réinitialiser la base de donnée.
    
    --------------------------------------------------------
    Pour quitter le programme, tapez 0.
    <Entrez votre choix>
    """,

'!main_from_start' : 
    """
    --------------------------------------------------------
    VOUS ÊTES TOUJOURS SUR L'OUTIL OPENFOODFACTS !
    Grâce à cette outil, vous pourrez remplacer des aliments
    mauvais par la santé, par des aliments plus sains.
    --------------------------------------------------------
    * Sélectionnez une option parmi les suivantes :
    --------------------------------------------------------

    1. Remplacer un aliment par un substitut sain.
    2. Retrouver mes aliments substitués.

    --------------------------------------------------------
    Pour quitter le programme, tapez 0.
    <Entrez votre choix>
    """,

'option_1' : 
    f"""
    --------------------------------------------------------
    * Sélectionnez une catégorie d'aliment. Le programme vous
    proposera des produits en fonction de celle-ci !
    --------------------------------------------------------

    1. {CATEGORIES[1]}
    2. {CATEGORIES[2]}
    3. {CATEGORIES[3]}
    4. {CATEGORIES[4]}
    5. {CATEGORIES[5]}

    --------------------------------------------------------
    Pour revenir au menu principal, tapez 0.
    <Entrez votre choix>
    """,

'option_1_2' : 
    f"""
    --------------------------------------------------------

    * Indiquez désormais l'ID du produit que vous voulez
    substituter. Le programme vous proposera des substituts
    en fonction de celui-ci !

    --------------------------------------------------------
    Pour revenir au menu principal, tapez 0.
    <Entrez votre choix>
    """,

'option_1_2_1' : 
    f"""
    --------------------------------------------------------

    * Voici des substituts plus sains de votre produit initial !
    Pour enregistrer cette combinaison produit-substitut, tapez
    l'ID du substitut que vous désirez associer avec votre produit.

    * Ensuite, rendez-vous sur le menu principal, onglet 2 pour
    revoir vos produits enregistrés.

    --------------------------------------------------------
    Pour revenir au menu principal, tapez 0.
    <Entrez votre choix>
    """,

'option_2_1': 
    """
    --------------------------------------------------------

    * Voici la liste de vos aliments préférés et de leur
    substitut plus sain !

    --------------------------------------------------------
    """,

'option_2_2' : 
    """
    --------------------------------------------------------
    Pour revenir au menu principal, tapez 0.
    <Entrez votre choix> 
    """,
}

# Variables contenant les informations de connexion à la base de donnée
# Ces informations sont modifiables librement par l'utilisateur sauf DB_DB
# Seul le module db.exec.py a accès à ces informations
#
# Pour modifier ces informations, suivez ces instructions :
#
# 1. Modifiez la variable DB_HOST avec l'hôte de votre base de donnée
# entre guillements.
# 2. Modifiez la variable DB_USER avec le nom d'utilisateur de votre
# base de donnée entre guillemets.
# 3. Modifiez la variable DB_PSWD avec le mot de passe de l'utilisateur
# de votre base de donnée entre guillemets.
# 4. ! Ne modifiez pas DB_DB !
DB_HOST = "localhost"
DB_USER = "root"
DB_PSWD = "root"
# ! Ne pas modifier la variable DB_DB !
DB_DB = "mydb"