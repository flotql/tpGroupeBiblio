from Livre import Livre

class BD(Livre):

    def __init__(self, Titre, auteur, langue, genre, categorie, ref, dispo, retour, couleur, dessinateur):
        super().__init__(Titre, auteur, langue, genre, categorie, ref, dispo, retour)
        self.couleur = couleur
        self.dessinateur = dessinateur

a = Livre("Harry Potter 1", "J.K Rowling", "Français", "Fantastique", "Roman", "HJ135203", "True", "None")
print(a.categorie)

b = BD("Injustice 1", "DC", "Français", "Fantastique", "BD", "ID104382", "True", "None", "True", "J Raapack")
print(b.categorie, b.dessinateur)