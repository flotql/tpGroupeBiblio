from Livre import Livre


class BD(Livre):

    def __init__(self, Titre, auteur, langue, genre, categorie, ref, dispo, retour, couleur, dessinateur):
        super().__init__(Titre, auteur, langue, genre, categorie, ref, dispo, retour)
        self.couleur = couleur
        self.dessinateur = dessinateur



# b = BD("Injustice 1", "DC", "Français", "Fantastique", "BD", "ID104382", "True", "None", "True", "J Raapack")
# print(b.categorie, b.dessinateur)
