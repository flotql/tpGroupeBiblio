from Livre import Livre


class BD(Livre):

    def __init__(self, titre, auteur, langue, genre, categorie, ref, dispo, retour, couleur, dessinateur):
        super().__init__(titre, auteur, langue, genre, categorie, ref, dispo, retour)
        self.couleur = couleur
        self.dessinateur = dessinateur

    def __repr__(self):
        return str("Voici les éléments de la BD:\n\t"
                   "Titre: "+self.titre+"      Auteur: "+self.auteur+"\n\t"
                   "Langue: "+self.langue+"      Genre: "+self.genre+"\n\t"
                   "Categorie: "+self.categorie + "      Référence: "+self.ref+"\n\t"
                   "Disponibilité: "+self.dispo + "      Date de retour: "+self.retour+"\n\t"
                    "En couleur: "+self.couleur + "      Dessinateur: "+self.dessinateur+"\n\t")


# b = BD("Injustice 1", "DC", "Français", "Fantastique", "BD", "ID104382", "True", "None", "True", "J Raapack")
# print(b)
