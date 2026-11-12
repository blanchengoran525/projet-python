class CompteBancaire: 
   def __init__(self, titulaire): 
      self.titulaire = titulaire 
      self.__montant = 0 

      def deposer(self, montant): 
       self.__montant += montant

      def retirer(self, montant): 
        if montant <= self.__montant:
          self.__montant -= montant
        else: 
          print('Solde insuffisant') 
      def afficher_solde(self): 
        print(f'solde de {self.titulaire} : {self.__montant}') 
 # Tests 
   c1 = CompteBancaire ('Alice') 
   c2 = CompteBancaire ('Bob')
 
   c1.deposer(1000) 
   c1.retirer(200) 
   c1.afficher_solde() 

   c2.deposer(500) 
   c2.retirer(700) 
   c2.afficher_solde()