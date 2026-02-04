class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = True


    # Get 
    def get_titre(self):
        return self.__titre
    def get_auteur(self):
        return self.__auteur
    def get_nb_pages(self):
        return self.__nb_pages
    def get_disponible(self):
        return self.__disponible

    # Set
    def set_auteur(self, auteur):
        self.__auteur = auteur
    def set_titre(self, titre):
        self.__titre = titre
    def set_nb_pages(self, nb_pages):
        self.__nb_pages = nb_pages
    def set_disponible(self):
        return self.__disponible
    
    # Emprunter
    def emprunter(self):
        if self.__disponible:
            self.__disponible = False
            print("Vous empruntez le livre")
            
        else:
            print("le livre est deja pris")
    # Rendre
    def rendre(self):
        if not self.__disponible:
            self.__disponible = True
            print("Vous avez rendu le livre")

        ("Le livre n'existe pas.")

    # Verification
    def verification(self):
        if self.__disponible == True:
            print("Le livre que vous souhaitez est disponible")
        else: 
            print("Le livre que vous souhaitez est indisponnible")
        
        if self.__nb_pages >= 0:
            print(f"Nombre de pages : {self.__nb_pages}")
        else:
            print("Le nombre de page ne doit être supérieur à 0")


livre = Livre("Etoiles Sombres", "Anton Parks", 154)
livre1 = Livre("Le Seigneurs des Anneaux", "JR Tolkien", 0)
livre1.verification()
livre.verification()
livre.emprunter()
livre.verification()
livre.rendre()
livre.verification()
