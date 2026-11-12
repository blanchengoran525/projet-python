notes = []
for i in range(5):
    note = float(input("Entrez une note :"))
    notes.append(note)
print("La liste des notes est:",notes)
moyenne = sum(notes)/len(notes)
max_note = max(notes)
min_note = min(notes)
print("La moyenne est:", moyenne)
print("La note maximale est:",max_note)
print("La note minimale est:", min_note)