

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
            print("id ",i[0],i[1],i[2])

    def __repr__(self):
        choix = input("1: Liste Utilisateurs \n2: Liste Livres\n")
        affiche = ""
        if choix == "1":
            for i in self.utilisateurs:
                affiche += i+"\n"
        elif choix == "2":
            for i in self.livres:
                affiche += i+"\n"
        return affiche

    def rechercheLivre(self,cat,choix):
        if choix == "1":
            if cat == "1":
                for i in self.livres:
                    
            elif cat == "2":

            elif cat == "3":

            elif cat == "4":

        elif choix == "2":
            if cat == "1":

            elif cat == "2":

            elif cat == "3":

            elif cat == "4":


test = Biblio()
test.importUtilisateurs()
test.afficherUtilisateurs()
print (test)

    # repr -faire choix si 1 afficher utilisateurs 2 afficher livres ? DONE
    # faire une recherche liste rayon, livres utilisateurs ? EN COURS           (dispo bool, type: str)
    # faire l'ajout d'utilisateurs ou livres ici?
    # les emprunts ici?
    # faire un emprunt /prolonger emprunt
