class Ville:
    def __init__(self, name, citizens):
        self.__name = name
        self.__citizens = citizens

    def get_name(self, name):
        return self.__name
    
    def get_citizens(self):
        return self.__citizens
    
    def add_citizen(self):
        self.__citizens += 1

    def show(self):
        print(f"Population de la ville de {self.__name} : {self.__citizens} habitants")

    def show_a(self):
        print(f"Mise à jour de la population de {self.__name} : {self.__citizens} Habitants")



class People:
    def __init__(self, name, age, ville):
        self.__name = name
        self.__age = age
        self.__ville = ville
        self.__ville.add_citizen()


paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

paris.show()
marseille.show()


john = People("John", 45, paris)
myrtille = People("Myrtille", 4, paris)
chloe = People("Chloé", 18, marseille )

paris.show_a()
marseille.show_a()


