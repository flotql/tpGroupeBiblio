from Classes.Bibliotheque import Biblio,BD,Livre
sys.path.insert(1, './Classes')
bibliotheque = Biblio()


def AffichageLivres(selection):
    bibliotheque.triLivres(bibliotheque.selection)
    choix = input("Choisir un auteur\n")
    print("Voici les livres disponibles de", bibliotheque.selection[int(choix) - 1], ":\t")
    bibliotheque.affichageTri(str(selection), int(choix) - 1)
    input("\nAppuyez sur \"entrer\" pour continuer\n")


def InterfaceUtilisateur():
    