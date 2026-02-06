class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    # Getter
    def get_longueur(self):
        return self.__longueur
    def get_largeur(self):
        return self.__largeur
    
    # Setter
    def set_longueur(self, longueur):
        self.__longueur = longueur
    def set_largeur(self, largeur):
        self.__largeur = largeur

    # Calculs
    def perimetre(self):
        perimetre = 2 * (self.__longueur + self.__largeur)
        print(f"Le permietre est de : {perimetre}.")
    def surface(self):
        surface = self.__longueur * self.__largeur
        print(f"La surface est de : {surface}.")

# Parallelepipede
class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur
    def volume(self):
        volume = self.get_longueur() * self.get_largeur() * self.hauteur
        print(f"Le Volume est : {volume}.")


# Objet
recantgle1 = Rectangle(10, 5)
parallelepipede1 = Parallelepipede(10, 5, 7)

# Action
recantgle1.perimetre()
recantgle1.surface()
parallelepipede1.volume()