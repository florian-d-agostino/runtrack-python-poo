class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix
    def informationVehicule(self):
        print(f"Marque : {self.marque}")
        print(f"Modèle : {self.modele}")
        print(f"Année : {self.annee}")
        print(f"Prix : {self.prix}€")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=2):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes

    def informationVehicule(self):
        super().informationVehicule()
        print(f"Portes : {self.portes}")

# Objet
voiture1 = Voiture("Mazda","MX5", 2014, 19000)

# Action
voiture1.informationVehicule()