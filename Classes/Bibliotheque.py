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
        openLivres = open("../References/Livres.txt", "r")
        lireLivres = openLivres.readlines
        for i in lireLivres:
            lesLivres = [i.split(" ; ")]
            if len(lesLivres) == 7:
                objLivre = Livre(lesLivres[0],lesLivres[1],lesLivres[2],lesLivres[3],lesLivres[4],lesLivres[5],lesLivres[6],lesLivres[7])
            else:
                objLivre = BD(lesLivres[0],lesLivres[1],lesLivres[2],lesLivres[3],lesLivres[4],lesLivres[5],lesLivres[6],lesLivres[7],lesLivres[8],lesLivres[9])
            if not objLivre.genre in self.rayon:
                self.rayon.append(objLivre.genre)
            if not objLivre.auteur in self.auteur:
                self.auteur.append(objLivre.auteur)
            if not objLivre.categorie in self.categorie:
                self.categorie.append(objLivre.categorie)
            if not objLivre.T

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
            if cat == "1": #categorie
                #fantastique, horreur, roman, comic
            elif cat == "2":

            elif cat == "3":

            elif cat == "4":

        elif choix == "2":
            if cat == "1":

            elif cat == "2":

            elif cat == "3":

            elif cat == "4":

    def ajoutUtilisateur(self,nouvelUtilisateur):
        self.utilisateurs.append(nouvelUtilisateur)


test = Biblio()
test.importUtilisateurs()
test.afficherUtilisateurs()
print (test)

    # repr -faire choix si 1 afficher utilisateurs 2 afficher livres ? DONE
    # faire une recherche liste rayon, livres utilisateurs ? EN COURS           (dispo bool, type: str)
    # faire l'ajout d'utilisateurs ou livres ici?
    # les emprunts ici?
    # faire un emprunt /prolonger emprunt
