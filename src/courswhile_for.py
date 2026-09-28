#nb: int = 1
#resultat: str = ''

#while nb <= 10:
    #resultat += str(nb) + " - "
    #resultat += f"{nb}"
    #if nb < 10:
       # resultat += " - "
    #nb += 1

#print

SEUIL : int = 1000

somme: int = 0
nb: int = 1

while somme <= SEUIL:
    somme += nb
    nb += 1

print(f"Réponse: {somme}")