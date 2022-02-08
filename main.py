from ast import Pass
import sys
from xml.dom.expatbuilder import parseString
sys.path.insert(1, './Classes')

from Classes.Bibliotheque import Biblio
from Classes.User import User


bibliotheque = Biblio()
bibliotheque.importUtilisateurs("./References/Utilisateurs.txt")

print(bibliotheque.utilisateurs)
while True:
    nouveau = input("Avez vous déjà un compte? Oui(1) / Non(2)\n")
    if nouveau != "1" and nouveau != "2":
        print("Merci d'inscrire le chiffre 1 ou 2\n")
    elif nouveau == "2": # l'utilisateur n'a pas de compte
        print("Démarrage de votre inscription")
        nom = input("Saisissez votre nom:\n")
        prenom = input("Saisissez votre prénom:\n")
        mdp = input("Saisissez votre mdp:\n")
        grade = input("Combien de livres souhaitez vous emprunter?\n\t"
                      "(1) 1-2 : gratuit\n\t"
                      "(2) 3-4 : 5.00 euros par mois\n\t"
                      "(3) 5-7 : 7.00 euros par mois\n\t"
                      "(4) 7-10 : 9.00 euros par mois\n\t")

        nouvelInscrit = User("",nom, prenom, mdp, [], grade)
        nouvelInscrit.DefinirID()
        bibliotheque.ajoutUtilisateur(nouvelInscrit)

        # fonction print le User nouvellement créé
        #  print "Votre inscription est validée"

    elif nouveau == "1": # l'utilisateur a déjà un compte
        nom = input("Saisissez votre nom:\n")
        prenom = input("Saisissez votre prénom:\n")
        mdp = input("Saisissez votre mdp:\n")

        for i in bibliotheque.utilisateurs:

            if i.nom == nom and i.prenom == prenom and i.mdp == mdp:
                print("Connection réussie")
                continuer = True
                while continuer:
                    choix = input("Vous désirez :\n\t"
                                  "(1) Changer de mot de passe\n\t"
                                  "(2) Afficher les livres disponibles\n\t"
                                  "(3) Recherche ciblée\n\t"
                                  "(4) Emprunter un livre\n\t"
                                  "(5) Rendre un livre\n\t"
                                  "(6) Prolonger un emprunt\n\t"
                                  "(7) Changer de grade\n\t"
                                  "(8) Se déconnecter\n\t")
                    if choix == "1": # Changer de Mot de Passe
                        i.ChangerMotDePasse(input("Indiquez votre nouveau mot de passe\n"))

                    # elif choix == "2":
                    # elif choix == "3":
                    # elif choix == "4":

                    # elif choix == "5":
                    elif choix == "6": # Prolonger un Emprunt
                        prolonger = input("Voulez-vous prolonger l'emprunt ? (oui/non)\n")
                        if prolonger != "non" and prolonger != "oui":
                            print("Merci d'écire oui ou non")
                        elif prolonger == "non":
                            Pass
                        else: 
                            print(i.emprunts)
                            livre = input("Quel livre souhaitez-vous prolonger ?\n")
                            durée = input("Combien de temps souhaitez-vous prolonger ? :\n\t"
                                  "(1) 1 semaine\n\t"
                                  "(2) 2 semaines\n\t"
                                  "(3) 3 semaines\n\t"
                                  "(4) 1 mois\n\t")
                            print("Votre demande a bien été prise en compte")            

                    elif choix == "7": # Changer de Grade
                        grade = input("Combien de livres souhaitez vous emprunter?\n\t"
                                      "(1) 1-2 : gratuit\n\t"
                                      "(2) 3-4 : 5.00 euros par mois\n\t"
                                      "(3) 5-7 : 7.00 euros par mois\n\t"
                                      "(4) 7-10 : 9.00 euros par mois\n\t")
                        i.ChangerGrade(grade)

                    elif choix == "8": # Se Déconnecter
                        continuer = False
                        print("Déconnexion réussie")
                    else:
                        print("Inscrire un chiffre entre 1 et 8")


            elif (i.nom != nom and i.prenom == prenom and i.mdp == mdp) or (i.nom == nom and i.prenom != prenom and i.mdp == mdp) or (i.nom == nom and i.prenom == prenom and i.mdp != mdp):
                print("Erreur d'indentification")

            else:
                pass

