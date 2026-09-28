#print(f"{4:02d}")


#nom: str = "Fernand"

#print(f"Bonjour {nom:>12}")

#PI: float = 3.141592653
#taxes: float = 0.05
#print(f'{PI:.2f} et {taxes:.0%}')


#a: int = 3
#b: str = "ABC"

#coucou: str = f"Bonjour {a} et {b}"

#print(f"Bonjour {a} et {b}")

#print(a, b, sep=' - ', end='.')
#print("coucou")


nombre: int = -1
message: str

nombre = int(input("Entrez un nombre: "))

if nombre > 0:
    message = "est positif"
elif nombre < 0:
    message = "est négatif"
else:
    message = "est égal à zéro"

print(f"Le nombre {nombre} {message}")