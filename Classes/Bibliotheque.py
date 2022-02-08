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

    def importUtilisateurs(self,chemin):
        with open(chemin, "r") as lireUtilisateur:
            for i in lireUtilisateur:
                lesUtilisateurs = [i.split(" ; ")]
                objUser = Personne(lesUtilisateurs)
                self.utilisateurs.append(objUser)

    def exportUtilisateurs(self,chemin):
        with open(chemin, "w") as file:
            for i in self.utilisateurs:
                file.writelines(i)

    def importLivres(self,chemin):
        openLivres = open(chemin, "r")
        lireLivres = openLivres.readlines()
        for i in lireLivres:
            lesLivres = [i.split(" ; ")]
            if len(lesLivres) == 7:
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

    def rechercheLivre(self,choix, cat, type):
        if choix == "1":
            if cat == "1":         # a l'index +1 (user not used to 0)
                for index, i in enumerate(self.categorie):
                    if type == "1":
                       for j in self.livres:
                           
            elif cat == "2":
                for index, i in enumerate(self.auteur):
                    print(i)
            elif cat == "3":
                for index, i in enumerate(self.rayon):
                    print(i)
            elif cat == "4":
                for index, i in enumerate(self.langue):
                    print(i)
        # elif choix == "2":
        #     if cat == "1":
        #
        #     elif cat == "2":
        #
        #     elif cat == "3":
        #
        #     elif cat == "4":

    def ajoutUtilisateur(self,nouvelUtilisateur):
        self.utilisateurs.append(nouvelUtilisateur)
        print("Votre inscription est validée")





test = Biblio()
# test.importUtilisateurs()
# test.afficherUtilisateurs()
# print (test)
test.importLivres()


    # repr -faire choix si 1 afficher utilisateurs 2 afficher livres ? DONE
    # faire une recherche liste rayon, livres utilisateurs ? EN COURS           (dispo bool, type: str)
    # faire l'ajout d'utilisateurs ou livres ici?
    # les emprunts ici?
    # faire un emprunt /prolonger emprunt
