from Personne import *


class User(Personne):

    def __init__(self, id,  nom, prenom, mdp, grade):
        super().__init__(id,  nom, prenom, mdp)
        self.emprunts = []
        self.grade = grade

    def __repr__(self):
        return str(f"{self.id} ; {self.nom} ; {self.prenom} ; {self.mdp} ; {self.emprunts} ; {self.grade}")

    def ChangerGrade(self, grade):
        self.grade = grade # on écrase le grade du constructeur

    def emprunterLivre(self, livre):
        self.emprunts.append(livre)


# d = User("c.gaetan", "corin", "gaetan", "JesuisGaetan", 1)
#
# print(d)




