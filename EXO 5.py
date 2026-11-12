from datetime import datetime

class CompteBancaire:
    def __init__(self, titulaire, solde):
        self.__solde = solde
        self.__titulaire = titulaire
        self.__historique = []

    # Getter solde (lecture seule)
    @property
    def solde(self):
        return self.__solde

    # Getter + Setter titulaire
    @property
    def titulaire(self):
        return self.__titulaire

    @titulaire.setter
    def titulaire(self, nom):
        if len(nom) >= 2:
            self.__titulaire = nom
        else:
            print("Nom invalide")

    # Ajouter historique
    def ajouter_historique(self, operation):
        date = datetime.now()
        self.__historique.append(f"{date} - {operation}")

    # Dépôt
    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
            self.ajouter_historique(f"Dépôt de {montant}")
        else:
            print("Montant invalide")

    # Retrait
    def retirer(self, montant):
        if montant <= 0:
            print("Montant invalide")
        elif montant > 1000:
            print("Max 1000 par retrait")
        elif montant > self.__solde:
            print("Solde insuffisant")
        else:
            self.__solde -= montant
            self.ajouter_historique(f"Retrait de {montant}")

    # Historique
    def afficher_historique(self):
        print("Historique :")
        for op in self.__historique[-10:]:
            print(op)

    # Virement
    def virement(self, autre_compte, montant):
        if montant > 0 and montant <= self.__solde:
            self.__solde -= montant
            autre_compte.__solde += montant
            self.ajouter_historique(f"Virement envoyé {montant}")
            autre_compte.ajouter_historique(f"Virement reçu {montant}")
        else:
            print("Virement impossible")


# Test
c1 = CompteBancaire("Alice", 2000)
c2 = CompteBancaire("Bob", 500)

c1.deposer(300)
c1.retirer(200)
c1.virement(c2, 400)

c1.afficher_historique()
c2.afficher_historique()
