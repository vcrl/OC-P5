class Display:
    def __init__(self):
        pass
    
    def display_products(self, id, name, brand, nutriscore):
        return print(
    f"""
    ____________________________________________________________________________________
    ID: {id} | NOM: {name} | MARQUE: {brand} | NUTRISCORE: {str(nutriscore).capitalize()}
    """
        )
    
    def display_subtitutes(self, name, brand, score, sname, sbrand, sscore):
        return print(
    f"""
    ____________________________________________________________________________________
    * Produit initial
    Nom: {name} | Marque: {brand} | Nutriscore: {str(score).capitalize()}
    -
    * Substitut sain (meilleur nutriscore)
    Nom: {sname} | Marque: {sbrand} | Nutriscore: {str(sscore).capitalize()} 

    """
        )
