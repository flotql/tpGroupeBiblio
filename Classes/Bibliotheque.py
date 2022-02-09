from Livre import *
from BD import *
from User import *

class Biblio:

    nomBib = "La petite lecture paisible"

    def __init__(self):
        self.rayon = []
        self.auteur = []
        self.livres = []
        self.utilisateurs = []
        self.categorie = []
        self.langue = []
        self.disponible = []

    def importUtilisateurs(self,chemin):
        with open(chemin, "r") as lireUtilisateur:
            for i in lireUtilisateur:
                lesUtilisateurs = i.split(" ; ")
                objUser = User(lesUtilisateurs[0],lesUtilisateurs[1],lesUtilisateurs[2],lesUtilisateurs[3],lesUtilisateurs[5])
                self.utilisateurs.append(objUser)
                # Ajouter chaque ref de lesutilisateurs[4] dans objUser.emprunts

    def exportUtilisateurs(self,chemin):
        with open(chemin, "w") as file:
            for i in self.utilisateurs:
                file.writelines(i)

    def importLivres(self,chemin):
        openLivres = open(chemin, "r")
        lireLivres = openLivres.readlines()
        for i in lireLivres:
            lesLivres = i.split(" ; ")
            if len(lesLivres) == 8:
                objLivre = Livre(lesLivres[0],lesLivres[1],lesLivres[2],lesLivres[3],lesLivres[4],lesLivres[5],lesLivres[6],lesLivres[7])
            else:
                objLivre = BD(lesLivres[0],lesLivres[1],lesLivres[2],lesLivres[3],lesLivres[4],lesLivres[5],lesLivres[6],lesLivres[7],lesLivres[8],lesLivres[9])
            self.livres.append(objLivre)
            if not objLivre.genre in self.rayon:
                self.rayon.append(objLivre.genre)
            if not objLivre.auteur in self.auteur:
                self.auteur.append(objLivre.auteur)
            if not objLivre.categorie in self.categorie:
                self.categorie.append(objLivre.categorie)
            if not objLivre.langue in self.langue:
                self.langue.append(objLivre.langue)
            if objLivre.dispo == "True":
                self.disponible.append(objLivre)


    # def ajoutLivre(self):


    def exportLivres(self,chemin):
        with open(chemin, "w") as file:
            for i in self.livres:
                file.writelines(i)

    def afficherUtilisateurs(self):
        for i in self.utilisateurs:
            print("id ",i[0],i[1],i[2])

    # def __repr__(self):
    #     choix = input("1: Liste Utilisateurs \n2: Liste Livres\n")
    #     affiche = ""
    #     if choix == "1":
    #         for i in self.utilisateurs:
    #             affiche += i+"\n"
    #     elif choix == "2":
    #         for i in self.livres:
    #             affiche += i+"\n"
    #     return affiche

    # def dispoLivres(self,dispo):



    def triLivres(self, tri):
        for index, i in enumerate(tri):
            print(index+1,": ",i)

    def affichageTri(self,selection,valeur):
        for i in self.disponible:
            if selection == "auteur":
                if i.auteur == self.auteur[valeur]:
                    print(i.titre)
            elif selection == "genre":
                if i.genre == self.rayon[valeur]:
                    print(i.titre)
            elif selection == "categorie":
                if i.categorie == self.categorie[valeur]:
                    print(i.titre)
            elif selection == "langue":
                if i.langue == self.langue[valeur]:
                    print(i.titre)

    def ajoutUtilisateur(self,nouvelUtilisateur):
        self.utilisateurs.append(nouvelUtilisateur)
        print("Votre inscription est validée")


 #########################            TEST                 ###########################

test = Biblio()

# test.importLivres("../References/Livres.txt")
# choix = input("si auteur press 1, genre press 2, 3 cat, 4 langue")
# if choix == "1":
#     test.triLivres(test.auteur)
#     choix = input("quel auteur")
#     test.affichageTri("auteur",int(choix)-1)
# if choix == "2":
#     test.triLivres(test.rayon)
#     choix = input("quel genre")
#     test.affichageTri("genre",int(choix)-1)
# if choix == "3":
#     test.triLivres(test.categorie)
#     choix = input("quel cat")
#     test.affichageTri("categorie",int(choix)-1)
# if choix == "4":
#     test.triLivres(test.langue)
#     choix = input("quel langue")
#     test.affichageTri("langue",int(choix)-1)
    # repr -faire choix si 1 afficher utilisateurs 2 afficher livres ? DONE
    # faire une recherche liste rayon, livres utilisateurs ? EN COURS           (dispo bool, type: str)
    # faire l'ajout d'utilisateurs ou livres ici?
    # les emprunts ici?
    # faire un emprunt /prolonger emprunt
