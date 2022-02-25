import re


def verifMDP(motDePasse, mdpActuel):
    if mdpActuel == motDePasse:
        return True
    else:
        return False


def creationMDP(mdp):
    if not re.fullmatch(r'^[A-Za-z0-9@#$%^&+-:!=]{5,10}$', mdp):
        return False
    else:
        return True
