class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
        self.diametre = rayon*2
        self.aire = 3.14 * rayon * rayon
        self.perimetre = 2 * 3.14 * rayon

    def changerRayon(self, rayon):
        self.rayon = rayon
        print(f"Le rayon est désormais de : {rayon}")

    def afficher(self):
        print(f"Le rayon est de : {self.rayon}")
        print(f"Le diametre est de : {self.diametre}")
        print(f"L'aire est de : {self.aire}")
        print(f"Le perimètre est de : {self.perimetre}")


cercle_1 = Cercle(4)
cercle_2 = Cercle(7)

cercle_1.afficher()
cercle_1.changerRayon(31)
cercle_1.afficher()

cercle_2.afficher()