import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, coup):
        coup.random(3) = 1
        coup -= self.vie
        coup = 0  # toucher / rater random

    def sante(self):
        pass

    def win(self):
        pass


class Jeu:
    def choisir_niveau(difficulte):
        pass # lvl difficulté 1 2 3





vladimir = Personnage("Vladimir Putin", 10)
trump = Personnage("Donald Trump", 10)