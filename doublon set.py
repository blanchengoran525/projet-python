nbr = input("Entre une liste de nombre")
liste = nbr.split()
liste_sans_doublons = list(set(liste))
print("liste sans doublons :", liste_sans_doublons)