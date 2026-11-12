mot=input("Entrez un mot:")
voy="aeiouyAEIOUY"
compt=0
for lettre in mot:
    if lettre in voy:
        compt += 1
        print("Il ya", compt,"voyelles")