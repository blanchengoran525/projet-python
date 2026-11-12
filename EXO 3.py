# Classe de base
class Animal:
    def __init__(self, nom, age, poids_kg):
        self.nom = nom
        self.age = age
        self.poids_kg = poids_kg

    def manger(self):
        print(self.nom, "mange")

    def dormir(self):
        print(self.nom, "dort")

    def cri(self):
        return "..."

    def __str__(self):
        return f"{self.nom}, {self.age} ans, {self.poids_kg} kg"


# Classe Mammifere
class Mammifere(Animal):
    def __init__(self, nom, age, poids_kg, est_domestique):
        super().__init__(nom, age, poids_kg)
        self.est_domestique = est_domestique

    def __str__(self):
        return super().__str__() + f", domestique: {self.est_domestique}"


# Classes spécifiques
class Chien(Mammifere):
    def cri(self):
        return "Wouf"

    def rapporter(self):
        print(self.nom, "rapporte un objet")


class Chat(Mammifere):
    def cri(self):
        return "Miaou"

    def ronronner(self):
        print(self.nom, "ronronne")


class Lion(Mammifere):
    def cri(self):
        return "Rugissement"

    def chasser(self):
        print(self.nom, "chasse")


class Oiseau(Animal):
    def __init__(self, nom, age, poids_kg, peut_voler):
        super().__init__(nom, age, poids_kg)
        self.peut_voler = peut_voler

    def cri(self):
        return "Cui-cui"


# Création des animaux
zoo = [
    Chien("Rex", 5, 20, True),
    Chat("Mimi", 3, 5, True),
    Lion("Simba", 7, 190, False),
    Oiseau("Titi", 2, 1, True),
    Animal("Bizarre", 4, 10)
]

# Afficher les cris
print("Cris des animaux :")
for animal in zoo:
    print(animal.nom, ":", animal.cri())

# Filtrer les mammifères
print("\nMammifères :")
for animal in zoo:
    if isinstance(animal, Mammifere):
        print(animal)
