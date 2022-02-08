from Personne import *


class User(Personne):

    def __init__(self, id,  nom, prenom, mdp, grade):
        super().__init__(id,  nom, prenom, mdp)
        self.emprunts = []
        self.grade = grade

    def ChangerGrade(self, grade):
        self.grade = grade

    def EmprunterLivre(self, livre):
        self.emprunts.append(livre)


# d = User("c.gaetan", "corin", "gaetan", "JesuisGaetan", ["Objet Le Hobbit"], 1)
# d.DefinirGrade()
# print(d.grade)




