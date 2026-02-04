class Comptebancaire:
    def __init__(self, numero_compte, nom, prenom, solde, agios):
        self.__numerocompte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.agios = agios

    def get_nom(self):
        return self.__nom
    def get_prenom(self):
        return self.__prenom
    def get_numerocompte(self):
        return self.__numerocompte
    def get_solde(self):
        return self.__solde
    
    def afficher(self):
        print(f"Nom : {self.__nom}")
        print(f"Prenom : {self.__prenom}")
        print(f"N° Compte : {self.__numerocompte}")
    
    def afficher_solde(self):
        print(f"Solde actuel : {self.__solde}€")

    def verserment(self):
        argent_sup = int(input("Quelle somme souhaitez vous ajouter ? : "))
        self.__solde += argent_sup
        print(f"Vous avez ajouter {argent_sup}€")
        print(f"Total de votre solde : {self.__solde}€")

    def retrait(self):
        argent_inf = int(input("Quelle somme souhaitez vous retirer ? : "))
        if argent_inf <= self.__solde or self.agios == False:
            self.__solde -= argent_inf
            print(f"Vous avez retirer {argent_inf}€")
            print(f"Total de votre solde : {self.__solde}€")
        else:
            print(f"Solde insufisant, vous avez un total de {self.__solde}€")
        if self.agios == True and argent_inf > -1:
            self.__solde -= argent_inf
            self.agios_d()

    def agios_d(self):
        if self.agios == True:
            agios = self.__solde * 0.12
            print(f"vos agios s'élévent à un montant de : {agios}€")
            self.__solde -= agios
            print(f"Solde total {self.__solde}€")

    def virement(self, compte):
        if compte == self.__numerocompte:
            virement = int(input(f"Vous avez choisis le compte N°{self.__numerocompte} - Combien souhaitez virer ? : "))
            self.__solde += virement
            print(f"Le virement sur le compte {self.__numerocompte} de {self.__nom}, {self.__prenom} d'un montant de : {virement}€")
            print("Est bien réalisé")
        else:
            compte != self.__numerocompte
            print("Virement impossible, compte inconnue")



nathan = Comptebancaire(1454, "Camredon", "Nathan", 1276, False)
nathan.afficher()
nathan.afficher_solde()
nathan.verserment()
nathan.afficher_solde()
nathan.retrait()
nathan.afficher_solde()
nathan.virement(1454)
nathan.afficher_solde()
