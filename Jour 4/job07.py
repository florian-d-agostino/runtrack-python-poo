
class Carte:
    def __init__(self, valeurs, couleurs):
        self.valeurs = valeurs
        self.couleurs = couleurs
        


        self.valeurs = [2, 3, 4, 5, 6, 7, 8, 9, "Valet", "Dame", "Roi","As"]
        self.couleurs = ["Coeur", "Trèfle", "Carerau", "Pique"]

    



class Jeu:
    def __init__(self, paquet, joueur, croupier):
        self.paquet = paquet
        self.joueur = joueur
        self.croupier = croupier

    def paquet(self):
        for couleur in self.couleurs:
            for valeur in self.valeurs:
                self.paquet.append(couleur, valeur)






# distribution de Carte
# tour joueur choix joueur prendre carte(s) ou passe
# tour croupier ajout carte jusqua 17 mini Stop
# Si main joueur > 21 perdu
# Si main joueur < 21 et > score croupier joueur gagne
# Sinon main joueur < 21 et < score croupier joueur perd



