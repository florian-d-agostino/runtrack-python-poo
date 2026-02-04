class Personne:
    nom = "Vide"
    def __init__(self, prenom, nom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print(f"Je suis {self.prenom}, {self.nom}")


personne1 = Personne("Camredon", "Nathan") 
personne2 = Personne("Florian", "D'agostino")

personne1.SePresenter()
personne2.SePresenter()