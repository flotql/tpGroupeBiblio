class Personne:

    def __init__(self, id,  nom, prenom, mdp):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.mdp = mdp

    def __repr__(self):
        return str(f"{self.nom},{self.prenom},{self.mdp}")

    def definirID(self):
        self.id = str(self.nom[0]+"."+self.prenom)

    def verifMDP(self, motDePasse, mdpActuel):
        if mdpActuel == motDePasse:
            return True
        else:
            return False


        # tstMDP = True
        # while tstMDP:
        #     if mdpActuel == motDePasse:
        #         tstMDP = False
        #     else:
        #         print("Les deux mdp ne correspondent pas, veuillez réessayer")

    def changerMotDePasse(self, motdepasse):
        self.mdp = motdepasse
        print("le mot de passe a bien été mis a jour")





# c = Personne("p.maxime", "przybylo", "maxime", "Azerty77")
# print(c.nom)
# print(c.Id)
# c.DefinirID()
# print(c.Id)
