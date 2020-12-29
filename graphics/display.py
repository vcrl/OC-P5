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
            *PRODUIT INITIAL
            Nom: {name} | Marque: {brand} | Nutriscore: {str(score).capitalize()}
            *SUBSTITUT
            Nom: {sname} | Marque: {sbrand} | Nutriscore: {str(sscore).capitalize()} 
            """
        )
