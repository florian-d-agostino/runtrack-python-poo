class Tache:
    def __init__(self, titre, description):
        self.titre = titre
        self.description = description
        self.status = "En cours"
    
    def terminer(self):
        self.status = "Terminée"


    

class ListeDeTaches:
    def __init__(self):
        self.listes = []

    def ajouter_tache(self, tache):
        self.listes.append(tache)

    def supprimer_tache(self, tache):
        self.listes.remove(tache)

    def afficher(self):
        for tache in self.listes:
            print(f"{tache.titre} - {tache.description} - {tache.status}")

    def filtreliste(self, status):
        liste_trier = []
        for tache in self.listes:
            if tache.status == status:
                liste_trier.append(status)
                print(liste_trier)
        

        

liste = ListeDeTaches()

tache1 = Tache("Nettoyer", "Ordinateur portable avec du produit")
tache2 = Tache("Ranger", "Bureau papier")
tache3 = Tache("Sortir poubelle", "Vider verre")

liste.ajouter_tache(tache1)
liste.ajouter_tache(tache2)
liste.ajouter_tache(tache3)

liste.afficher()
liste.filtreliste(tache1)


tache1.terminer()



