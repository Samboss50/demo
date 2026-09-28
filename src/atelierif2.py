titre: str
prenom: str
nom: str

titre = input("Veuillez entrez votre genre (M,m,F,f,N,n): ")
prenom = input("Veuillez entrez votre prenom: ")
nom = input("Veuillez entrez votre nom: ")

if titre == ("F" or "f"):
    print("Bonjour madame")

elif titre == ("M" or "m"):
    print("Bonjour monsieur")

elif titre == ("N" or "n"):
    print("Bonjour")

else:
    print("Erreur veuillez recommencer et entrer une lettre appropriée")

print(prenom)
print(nom)

