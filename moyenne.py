n = int(input("Il y'a combient d'etudiant?"))
somme = 0
meilleure = 0
if n > 0:       
 for i in range(1, n+1):
    note = float(input("Entrez la note :"))
    somme = somme + note
    if note > meilleure:
        meilleure = note
        moyenne = somme/n
        print("La moyenne est :",moyenne)
        print("La meilleure note est:", meilleure)