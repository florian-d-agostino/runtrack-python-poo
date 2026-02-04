class Animal:
    def __init__(self, age=0, prenom=""):
        self.age = age
        self.prenom = prenom
        print(f"L'age de l'animal est de : {self.age}")

    def vieillir(self):
        self.age += 1
        print(f"L'age de l'animal est de : {self.age}")

    def nommer(self, prenom):
        self.prenom = prenom
        print(f"Le nouveau prenom est : {prenom}")

animal_1 = Animal()
animal_1.vieillir()
animal_1.nommer("Barbecue")


