import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class Part:
    def __init__(self, name, materials):
        self.name = name
        self.materials = materials

    def change_materials(self, new_materials):
        self.materials = new_materials

    def __str__(self):
        return f"{self.name} est constitué de {self.materials}"

class Ship:
    def __init__(self, name):
        self.name = name
        self.__parts = {}
        self.memory = []

    def add_part(self, part):
        self.__parts[part.name] = part
        self.memory.append(f"Ajout de {part.name}")

    def display_state(self):
        return "\n".join(str(part) for part in self.__parts.values())

    def replace_part(self, part_name, new_part):
        if part_name in self.__parts:
            self.__parts[part_name] = new_part
            self.memory.append(
                f"Remplacement de {part_name} par {new_part.name}"
            )

    def change_part(self, part_name, new_material):
        if part_name in self.__parts:
            self.__parts[part_name].change_materials(new_material)
            self.memory.append(
                f"Changement du matériau de {part_name} en {new_material}"
            )

    def show_history(self):
        return "\n".join(self.memory)

class RacingShip(Ship):
    def __init__(self, name, max_speed):
        super().__init__(name)
        self.max_speed = max_speed

    def display_speed(self):
        return f"Vitesse maximale : {self.max_speed} nœuds"

class ShipApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestion du bateau")
        self.geometry("500x500")

        # Objet métier
        self.ship = RacingShip("Black Python", 45)
        self.ship.add_part(Part("Mât", "Bois"))
        self.ship.add_part(Part("Coque", "Acier"))
        self.ship.add_part(Part("Voile", "Tissu"))

        # Zone d'affichage
        self.output = ctk.CTkTextbox(self, width=450, height=200)
        self.output.pack(pady=10)

        # Boutons
        self.create_buttons()

    def create_buttons(self):
        ctk.CTkButton(
            self, text="Afficher l'état du bateau",
            command=self.show_state
        ).pack(pady=5)

        ctk.CTkButton(
            self, text="Changer le matériau d'une pièce",
            command=self.change_material
        ).pack(pady=5)

        ctk.CTkButton(
            self, text="Remplacer une pièce",
            command=self.replace_part
        ).pack(pady=5)

        ctk.CTkButton(
            self, text="Afficher la vitesse max",
            command=self.show_speed
        ).pack(pady=5)

        ctk.CTkButton(
            self, text="Afficher l'historique",
            command=self.show_history
        ).pack(pady=5)

    def show_state(self):
        self.output.delete("1.0", "end")
        self.output.insert("end", self.ship.display_state())
    def change_material(self):
        part = ctk.CTkInputDialog(
            text="Nom de la pièce :", title="Modifier matériau"
        ).get_input()
        material = ctk.CTkInputDialog(
            text="Nouveau matériau :", title="Modifier matériau"
        ).get_input()
        self.ship.change_part(part, material)
        self.show_state()
    def replace_part(self):
        old = ctk.CTkInputDialog(
            text="Pièce à remplacer :", title="Remplacer"
        ).get_input()
        new = ctk.CTkInputDialog(
            text="Nom nouvelle pièce :", title="Remplacer"
        ).get_input()
        mat = ctk.CTkInputDialog(
            text="Matériau :", title="Remplacer"
        ).get_input()
        self.ship.replace_part(old, Part(new, mat))
        self.show_state()
    def show_speed(self):
        self.output.delete("1.0", "end")
        self.output.insert("end", self.ship.display_speed())
    def show_history(self):
        self.output.delete("1.0", "end")
        self.output.insert("end", self.ship.show_history())

def menu():
    ship = RacingShip("Black Python", 45)

    ship.add_part(Part("Mât", "Bois"))
    ship.add_part(Part("Coque", "Acier"))
    ship.add_part(Part("Voile", "Tissu"))

    while True:
        print("""
======== MENU ========
1. Afficher l'état du bateau
2. Changer le matériau d'une pièce
3. Remplacer une pièce
4. Afficher la vitesse max
5. Afficher l'historique
0. Quitter
======================
""")

        choice = input("Choix : ")

        if choice == "1":
            ship.display_state()

        elif choice == "2":
            name = input("Nom de la pièce : ")
            material = input("Nouveau matériau : ")
            ship.change_part(name, material)

        elif choice == "3":
            old_name = input("Nom de la pièce à remplacer : ")
            new_name = input("Nom de la nouvelle pièce : ")
            new_material = input("Matériau : ")
            ship.replace_part(old_name, Part(new_name, new_material))

        elif choice == "4":
            ship.display_speed()

        elif choice == "5":
            ship.show_history()

        elif choice == "0":
            print("Fin du programme")
            break

        else:
            print("Choix invalide")

if __name__ == "__main__":
    app = ShipApp()
    app.mainloop()