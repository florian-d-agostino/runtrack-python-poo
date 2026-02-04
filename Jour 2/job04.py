class Student:
    def __init__(self, name, surname, id_student, credit=0):
        self.__name = name
        self.__surname = surname
        self.__id_student = id_student
        self.__credit = credit

    def get_name(self):
        return self.__name
    def get_surname(self):
        return self.__surname
    def get_id_student(self):
        return self.__id_student
    def get_credit(self):
        return self.__credit

    def set_credit(self, credit):
        self.__credit = credit

    def add_credit(self, credit):
        if credit > 0:
            self.__credit += credit
            print(f"Le nombre de credits de {self.__surname}, {self.__name} est de : {self.__credit} points.")
        else:
            print("Veuillez entrer un nombre de credit supérieur à 0")

    def student_eval(self):
        if self.__credit > 90:
            print("Niveau = Excellent")
        elif self.__credit > 80:
            print("Niveau = Trés bien")
        elif self.__credit > 70:
            print("Niveau = Bien")
        elif self.__credit > 60:
            print("Niveau = Passable")
        elif self.__credit <= 60:
            print("Niveau = Insuffisant")

    def show(self):
        print(f"Nom = {self.__name}")
        print(f"Prénom = {self.__surname}")
        print(f"ID = {self.__id_student}")
        print(f"Name = {self.__name}")

john_doe = Student("Doe", "John", 16137, 0)
john_doe.add_credit(85)
john_doe.show()
john_doe.student_eval()