class Commande:
    def __init__(self, numero_cde):
        self.__numero_cde = numero_cde
        self.__liste_plats = {}
        self.__status_cde = "en cours"

    def ajouter_plat(self, nom_plat, prix):
        self.__liste_plats[nom_plat] = prix

    def annuler_plat(self):
        self.__status_cde = "annulée"
        print("Commande annulée")

    def afficher_cde(self):
        print(self.__liste_plats)

    def total(self):
        total = 0
        for prix in self.__liste_plats.values():
            total += prix
        print(f"Le total est de : {total}€")


commande = Commande(1)
commande.ajouter_plat("Salade césar", 8.90)
commande.ajouter_plat("Pizza", 11)
commande.ajouter_plat("Tarte champsaur", 12.3)
commande.annuler_plat()
commande.afficher_cde()
commande.total()