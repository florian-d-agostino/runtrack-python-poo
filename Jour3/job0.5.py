import random
import time 

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, ennemi):
        coup = random.randint(0, 3)
        ennemi.sante(coup)
        print(f"{self.nom} attaque {ennemi.nom} et inflige {coup} dégats.")

    def sante(self, coup):
        self.vie -= coup
        if self.vie < 0:
            self.vie = 0
        print(f"{self.nom} a maintenant {self.vie} point de vie.")


    def vivant(self):
        return self.vie > 0


class Jeu:
    def __init__(self, joueur, ennemi):
        self.joueur = joueur
        self.ennemi = ennemi
        self.niveau_input = None

    def choisir_niveau(self):
        while True:
            niveau_input = int(input("~~~~~~~ FIGHT PYTH ~~~~~~~ \n Niveau difficulté Facile - 1 \n Niveau de difficulté Moyen - 2 \n Niveau de difficulté Difficile - 3 \n Quel difficulté voulez vous choisir ? (1/2/3) : "))
            self.niveau_input = niveau_input
            break

    def appliquer_niveau(self):
        if self.niveau_input == 1:
            vie_joueur = 20
            vie_ennemi = 20
        elif self.niveau_input == 2:
            vie_joueur = 15
            vie_ennemi = 20
        elif self.niveau_input == 3:
            vie_joueur = 10
            vie_ennemi = 20

    def victoire(self):
        if self.joueur.vivant():
            print(f"{self.joueur.nom} a gagné !")
        else:
            print(f"{self.ennemi.nom} à gagné !")
    

    def lancer_jeu(self):
        self.choisir_niveau()
        self.appliquer_niveau()



        print(" Round One ! - - Fight - -  !")

        while self.joueur.vivant() and self.ennemi.vivant():
            time.sleep(2)
            self.joueur.attaquer(self.ennemi)

        self.victoire()
    







vladimir = Personnage("Vladimir Putin", 10)
trump = Personnage("Donald Trump", 10)
jeu = Jeu(vladimir, trump)
jeu.lancer_jeu()