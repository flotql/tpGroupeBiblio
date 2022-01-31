

class Biblio:

    nomBib = "La petite lecture paisible"

    def __init__(self):
        self.rayon = []
        self.auteur = []
        self.livres = []
        self.utilisateurs = []

    def importUtilisateurs(self):
        with open("../References/Utilisateurs.txt", "r") as lireUtilisateur:
            for i in lireUtilisateur:
                self.utilisateurs.append(i)
        return self.utilisateurs

    def exportUtilisateurs(self):
        with open("../References/Utilisateurs.txt", "w") as file:
            for i in enumerate (self.utilisateurs):
                file.writelines(i)

    def importLivres(self):
        openLivres = open("../References/Livres.txt.txt", "r")
        lireLivres = openLivres.readlines
        for i in lireLivres:
            self.livres.append(i)
        return self.livres

    def exportLivres(self):
        with open("../References/Livres.txt", "w") as file:
            for i in enumerate(self.livres):
                file.writelines(i)

    def afficherUtilisateurs(self):
        for i in self.utilisateurs:
            print("id",i.[])

test = Biblio()
test.importUtilisateurs()
print(

    # repr -faire choix si 1 afficher utilisateurs 2 afficher livres ?
    # faire une recherche liste rayon, livres utilisateurs ?
    # faire l'ajout d'utilisateurs ou livres ici?
    # les emprunts ici?
    # faire un emprunt /prolonger emprunt
