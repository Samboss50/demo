nombre: int = 10

if nombre >= 0:
    print("YEAH")
    print("positif")

else :
    print("négative")

print("fin")



note: int = 72
cote: str

if note >= 90:
    cote = "A"

elif note >= 80 and note < 90:
    cote = "B"

elif note >= 70:
    cote = "C"

elif note >= 60:
    cote = "D"

else:
    cote = "E"

print(cote)


a: int = 2
b: int = 5
min: int

if a < b:
    min = a
else:
    min = b

min = a if a < b else b

