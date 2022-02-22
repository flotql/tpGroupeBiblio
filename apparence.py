import os
# récupérer le chemin du répertoire courant
path = os.getcwd()
print("Le répertoire courant est : " + path)
# récupérer le nom du répertoire courant
repn = os.path.basename(path)
print("Le nom du répertoire est : " + repn)
# récupérer le chemin du script
path = os.path.realpath(__file__)
print("Le chemin du script est : " + path)

## le code ci-dessous à mettre dans la console :
# python -m ensurepip
# python -m pip install art

from art import *
# art.aprint("random")
tprint("Bonjour",font="block-medium")
tprint("Bienvenue dans la Bibliotheque",font="block-medium")

# Explication :
# https://pypi.org/project/art/
# Liste des polices :
# https://github.com/sepandhaghighi/art/blob/master/FontList.ipynb
