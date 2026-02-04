class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, reservoir=50, en_marche=False):
        self.marque = marque
        self.modele = modele
        self.anne = annee
        self.kilometrage = kilometrage
        self.__reservoir = reservoir
        self.__en_marche = en_marche

    def demarrer(self):
        if self.__en_marche == False and self.__reservoir >= 5:
            self.__en_marche = True
            print("Votre voiture démarre.")
            print(f"Le reservoir à acutellement {self.__reservoir} litres")
    def arreter(self):
        if self.__en_marche == True:
            self.__en_marche = False
            print("Voitre voiture s'éteind.")

    def verifier_plein(self):
        return self.__reservoir
    
voiture_1 = Voiture("Mazda", "MX5", 2014, 124560)
voiture_1.demarrer()
voiture_1.arreter()