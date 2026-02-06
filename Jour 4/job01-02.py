# Personne
class Personne:
    def __init__(self, age=14):
        self.age = age
    def afficherAge(self):
        print(f"Age = {self.age} ans")
    def bonjour(self):
        print("Bonjour")
    def modifier_age(self, nv_age):
        self.age = nv_age

# Eleve
class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")
    def afficherAge(self):
        return super().afficherAge()

# Professeur
class Professeur(Personne):
    def __init__(self, matiereEnseigee):
        self.__matiereEnseignee = matiereEnseigee
    def enseigner(self):
        print(f"Le cours va commencer.")
    def afficherAge(self):
        return super().afficherAge()


# Objet
eleve1 = Eleve(16)
eleve2 = Personne(15)
professeur1 = Professeur("Science")


# Action
eleve1.bonjour()
eleve1.allerEnCours()
eleve2.bonjour()
professeur1.bonjour()
professeur1.enseigner()


