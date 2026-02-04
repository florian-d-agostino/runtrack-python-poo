class Joueur:
    def __init__(self, nom, numero, position, nb_but, passe_decisive, carton_jaune, carton_rouge):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.nb_but = nb_but
        self.passe_decisive = passe_decisive
        self.carton_jaune = carton_jaune
        self.carton_rouge = carton_rouge

    def marqueUnBut(self):
        self.nb_but += 1
    def effectuerUnePasseDecisive(self):
        self.passe_decisive += 1
    def recevoirUnCartonJaune(self):
        self.carton_jaune += 1
    def recevoirUnCartonRouge(self):
        self.carton_rouge += 1

    def afficher(self):
        print(f"Nom : {self.nom} ")
        print(f"Numéro : {self.numero} ")
        print(f"Posisiont : {self.position}")
        print(f"Nombre de but : {self.nb_but} ")
        print(f"Passe décisive : {self.passe_decisive}")
        print(f"Carton jaune : {self.carton_jaune}")
        print(f"Carton rouge : {self.carton_rouge}")


class equipe_foot:
    def __init__(self, nom):
        self.nom = nom
        self.liste_joueurs = []

    def ajouter_joueur(self, joueur):
        self.liste_joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        for joueurs in self.liste_joueurs:
            print(joueurs.nom, 
                joueurs.numero, 
                joueurs.position, 
                joueurs.nb_but, 
                joueurs.passe_decisive,
                joueurs.carton_jaune,
                joueurs.carton_rouge)
            
    def mettreAJourStatistiquesjoueur(self,joueur, type):
        if joueur in self.liste_joueurs:
            if type == "but":
                joueur.marqueUnBut()
            elif type == "passe_decisive":
                joueur.effectuerUnePasseDecisive()
            elif type == "jaune":
                joueur.recevoirUnCartonJaune()
            elif type == "rouge":
                joueur.recevoirUnCartonRouge()



joueur1 = Joueur("John", 9, "avant-centre", 2, 7, 1, 0)
joueur2 = Joueur("Petter", 12, "deffenseur", 0, 2, 1, 1)
joueur3 = Joueur("Walter", 7, "butteur", 12, 2, 1, 2)


joueur1.marqueUnBut()

om = equipe_foot("Olympique de Marseille")
om.ajouter_joueur(joueur1)
om.ajouter_joueur(joueur2)

joueur1.marqueUnBut()

om.afficherStatistiquesJoueurs()
om.mettreAJourStatistiquesjoueur(joueur1, "rouge")
om.afficherStatistiquesJoueurs()