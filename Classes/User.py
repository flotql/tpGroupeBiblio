from Personne import Personne


class User(Personne):

    def __init__(self, Id,  nom, prenom, mdp, emprunts, grade):
        super().__init__(Id,  nom, prenom, mdp)
        self.emprunts = emprunts
        self.grade = grade



    def DefinirGrade(self):
        NombreLivres = len(self.emprunts)
        if NombreLivres >= 5:
            self.grade = 3
        elif NombreLivres >= 3:
            self.grade = 2
        else:
            self.grade = 1
        # print(self.grade)


# d = User("c.gaetan", "corin", "gaetan", "JesuisGaetan", ["Objet Le Hobbit","Objet Le Hobbit","Objet Le Hobbit","Objet Le Hobbit","Objet Le Hobbit"], 1)
# d.DefinirGrade()
# print(d.grade)




