class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        TVA = self.prixHT * 0.20
        prix_TTC = TVA + self.prixHT
        print(f"Le prix TTC est {prix_TTC}€. La TVA est de {TVA}€")
    
    def afficher(self):
        print(f"Produit : {self.nom}")
        print(f"Prix HT : {self.prixHT}€")
        print(f"TVA {self.TVA} %")

objet_1 = Produit("Chaise", 40, 20)
objet_2 = Produit("Table", 100, 20)

objet_1.CalculerPrixTTC()
objet_1.afficher()

objet_2.CalculerPrixTTC()
objet_2.afficher()