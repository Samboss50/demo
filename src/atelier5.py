jour: int

jour = int(input("Entrez un nombre entre 1 à 7: "))

match jour:
    case 1:
        print("Dimanche")
    case 2:
        print("Lundi")
    case 3:
        print("Mardi")
    case 4:
        print("Mercredi")
    case 5:
        print("Jeudi")
    case 6:
        print("Vendredi")
    case 7:
        print("Samedi")
    case _:
        print("Invalide")



