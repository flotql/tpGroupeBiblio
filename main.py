from Classes.Bibliotheque import Biblio
from Classes.Personne import Personne
from Classes.User import User
# from Classes.BD import BD
# from Classes.Livre import Livre

#
# bibliotheque = Biblio()
# while True:
#     nouveau = input("Avez vous déjà un compte? Non(1) / Oui(2)\n")
#     if nouveau != "1" and nouveau != "2":
#         print("Merci d'inscrire le chiffre 1 ou 2\n")
#     elif nouveau == "1":
#         print("Démarrage de votre inscription")
#         nom = input("Saisissez votre nom:\n")
#         prenom = input("Saisissez votre prénom:\n")
#         mdp = input("Saisissez votre mdp:\n")
#
#         nouvelInscrit = User("",nom, prenom, mdp, [], 1)
#         nouvelInscrit.DefinirID()
#         bibliotheque.ajoutUtilisateur(nouvelInscrit)
#
#         # fonction print le User nouvellement créé
#         # fonction ajouter l'utilisateur dans la bibliotheque + print "Votre inscription est validée"
#
#     elif nouveau == "2":
#         nom = input("Saisissez votre nom:\n")
#         prenom = input("Saisissez votre prénom:\n")
#         mdp = input("Saisissez votre mdp:\n")
#         #testconnection = fonction de verification de connection, return "True" si ok, "ErreurNomPrenom" si erreur dans le nom ou le prenom, "ErreurMdp" si erreur dans le motdepasse.
#         if testconnection == "ErreurNomPrenom":
#             print("Votre compte n'existe pas")
#         elif testconnection == "ErreurMdp":
#             print("Votre mot de passe est incorrect")
#         else:
#             print("Connection réussie")
