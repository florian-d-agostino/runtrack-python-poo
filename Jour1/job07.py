class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1
    
    def haut(self):
        self.y += 1
    
    def bas(self):
        self.y -= 1

    def position(self):
        position = (self.x, self.y)
        print(f"Votre position X / Y est : {position}")

personnage = Personnage(0, 0)
personnage.position()
personnage.gauche()
personnage.position()
personnage.gauche()
personnage.position()
personnage.haut()
personnage.position()
personnage.haut()
personnage.position()