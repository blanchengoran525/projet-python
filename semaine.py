jours=["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
result = input("Entrez un jour:").lower()
if result in jours:
    print("Jour num", jours.index(result)+1)
else:
    print("Jour invalide")
    