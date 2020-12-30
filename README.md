# Python API OpenFoodFacts
Cet outil permet aux utilisateurs de sélectionner un produit parmi une liste générée grâce à l'API REST de OpenFoodFacts, et de retrouver des substituts plus sains à celui-ci.
L'utilisateur peut alors enregistrer les substituts qu'il trouve pertinent dans la base de donnée locale. (SQL)

## Pré-requis

Pour utiliser ce programme, vous devez posséder Python 3+ sur votre machine, et installer les dépendances grâce au fichier requirements.txt.

## Installation

1. Clônez le dépôt distant en local sur votre machine. (git clone <lien>)
2. Configurez un environnement virtuel, et installez les modules présents dans le fichier requirements.txt (pip install -r requirements.txt)
3. Lancez le script en exécutant le fichier main.py (python3 main.py)

## Utilisation
En lancez le programme, vous tomberez sur le menu principal qui vous proposera trois options :
  1. Remplacer un aliment par un substitut sain.
  2. Retrouver mes aliments substitués.
  3. Réinitialiser la base de donnée.

L'option 1 vous permettra de sélectionner un aliment parmi une liste, et d'enregistrer un substitut à celui-ci.
L'option 2 vous permettra de retrouver les substituts que vous avez enregistré.
L'option 3 - qui n'est que disponible au lancement du programme pour des raisons de stabilité - vous permet de réinitialiser la base de donnée. (attention, ça supprime tous vos substituts !)

## Utiliser une base de donnée personnalisée
Pour utiliser une base de donnée personnalisée, rien de plus simple. 
  1. Naviguez dans le fichier constants.py
  
      /contsants/constants.py
  
  2. Suivez les instructions énumérées à partir de la ligne 129.
  
  3. Tout fonctionne correctement.

## Merci d'utiliser cet outil !
