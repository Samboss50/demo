nb: int

#nb = int(input("Entrez 1 pour pile, 2 pour face: "))

#if nb == 1:
#    print("Pile")
#elif nb == 2:
#    print("Face")
#else:
#    print("Tata")

#match nb:
#    case 1:
#        print("Pile")
#    case 2:
#        print("Face")
#    case _:
#        print("Tata")

nb = int(input("Entrez le résultat du lancé du dé: "))

match nb:
    case 1 | 2:
        print("Échec")
    case 3:
        print("Bof")
    case 4 | 5:
        print("Ok")
    case 6:
        print("Parfait")
    case _:
        print("Invalide")

