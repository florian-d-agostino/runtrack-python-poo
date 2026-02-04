class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def get_longueur(self):
        return self.__longueur
    def set_longueur(self, longueur):
        self.__longueur = longueur
        

    def get_largeur(self):
        return self.__largeur
    def set_largeur(self, largeur):
        self.__largeur = largeur
        


    def afficher(self):
        long = self.get_longueur()
        larg = self.get_largeur()
        print(f"Longueur : {long}")
        print(f"largeur : {larg}")

    def modifier(self, longueur, largeur):
        self.set_largeur(largeur)
        self.set_longueur(longueur)
        print(f"Nouvelle largeur {largeur}")
        print(f"Nouvelle longueur {longueur}")

rectangle = Rectangle(10, 5)
rectangle.afficher()
rectangle.set_largeur(10)
rectangle.set_longueur(20)
rectangle.modifier(24, 45)


