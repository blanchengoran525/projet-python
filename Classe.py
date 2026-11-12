class voiture:
    def __init__(self, marque, couleur, vitesse):
        self.marque = marque
        self.couleur = couleur
        self.vitesse = vitesse
        self.__kilometrage = 0 #attribut privé

    def rouler(self,km):
         self.__kilometrage += km
         print(f'{self.marque} a parcouru{km} km')

    def afficher_km(self):
        return self.__kilometrage
    #instacier et utiliser une classe
ma_voiture = voiture("Toyota", "Rouge", 120)
voiture2 = voiture("Honda", "Bleue", 150)
ma_voiture.rouler(50)
voiture2.rouler(60)
print(ma_voiture.afficher_km())
#print(ma_voiture.__kilometrage)
print(voiture2.afficher_km())