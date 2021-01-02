"""
Module contenant la classe Display, affichant les produits
sous une belle mise en page.
"""

class Display:
    """
    Classe permettant l'affichage des produits
    de manière structurée et lisible.
    Méthodes:
    * display_products:
        - Affiche les produits de manière
        lisible. Correspond à la liste des
        produits.

    * display_substitutes:
        - Affiche le produit initial et
        ses substituts de manière lisible.
    """
    def __init__(self):
        pass
    
    def display_products(self, id, name, brand, nutriscore):
        """
        Méthode permettant l'affichage des produits
        de manière structurée.
        Arguments:
        * id:
            - Correspond à l'ID du produit.
        * name:
            - Correspond au nom d'affichage du
            produit.
        * brand:
            - Correspond à la marque du produit.
        * nutriscore:
            - Correspond au nutriscore du produit.
        """
        return print(
    f"""
    ____________________________________________________________________________________
    ID: {id} | NOM: {name} | MARQUE: {brand} | NUTRISCORE: {str(nutriscore).capitalize()}
    """
        )
    
    def display_subtitutes(self, name, brand, score, sname, sbrand, sscore, sshop, slink):
        """
        Méthode permettant l'affichage des substituts
        de manière structurée.
        Arguments:
        * name:
            - Correspond au nom d'affichage du
            produit initial.
        * brand:
            - Correspond à la marque du produit initial.
        * score:
            - Correspond au nutriscore du produit initial.
        * sname:
            - Correspond au nom d'affichage du substitut.
        * sbrand:
            - Correspond à la marque du substitut.
        * sscore:
            - Correspond au nutriscore du substitut.
        * sshop:
            - Correspond à la liste des magasins du
            substitut.
        * slink:
            - Correspond au lien OpenFoodFact du
            substitut.
        """
        return print(
    f"""
    ____________________________________________________________________________________
    * Produit initial
    Nom: {name} | Marque: {brand} | Nutriscore: {str(score).capitalize()}
    -
    * Substitut sain (meilleur nutriscore)
    Nom: {sname} | Marque: {sbrand} | Nutriscore: {str(sscore).capitalize()} | Disponible chez: {sshop}
    Lien: {slink}
    """
        )
