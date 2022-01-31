from Personne import Personne


class User(Personne):

    def __init__(self, Id,  nom, prenom, mdp, emprunts, grade):
        super().__init__(Id,  nom, prenom, mdp)
        self.emprunts = emprunts
        self.grade = grade


# d = User("c.gaetan", "corin", "gaetan", "JesuisGaetan", ["Objet Le Hobbit"], 3)
# print(d.emprunts)

def DefinirGrade():




