class Livre:

    def __init__(self, Titre, auteur, langue, genre, categorie, ref, dispo, retour):
        self.Titre = Titre
        self.auteur = auteur
        self.langue = langue
        self.genre = genre
        self.categorie = categorie
        self.ref = ref
        self.dispo = dispo
        self.retour = retour

# a = Livre("Harry Potter 1", "J.K Rowling", "Français", "Fantastique", "Roman", "HJ135203", "True", "None")
# print(a.categorie)
