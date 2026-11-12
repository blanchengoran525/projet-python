notes = []
for i in range(5):
  note = float(input("entrez une notes"+str(i+1)+ " : "))
  notes.append(note)
print("les notes sont:", notes)
moyenne = sum(notes)/len(notes)
print("la moyenne est:",moyenne)