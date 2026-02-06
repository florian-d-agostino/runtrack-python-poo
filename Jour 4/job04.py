class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        super().__init__()
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        aire = self.largeur * self.hauteur
        print(f"L'aire est de : {aire}")

class Cercle(Forme):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    def aire(self):
        aire = 3.14 * (self.radius * self.radius)
        print(f"L'aire est de {aire}.")

# Objet
rectangle1 = Rectangle(10, 5)
cercle1 = Cercle(10)

# Action
rectangle1.aire()
cercle1.aire()
