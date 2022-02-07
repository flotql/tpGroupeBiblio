class Personne:

    def __init__(self, id,  nom, prenom, mdp):
        self.Id = id
        self.nom = nom
        self.prenom = prenom
        self.mdp = mdp

    def DefinirID(self):
        self.id = str(self.nom[0]+"."+self.prenom)





# c = Personne("p.maxime", "przybylo", "maxime", "Azerty77")
# print(c.nom)
# print(c.Id)
# c.DefinirID()
# print(c.Id)
