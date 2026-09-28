note1: float
note2: float
note3: float
note4: float
note5: float
moyenne: float

note1 = float(input("Veuillez entrez la note #1: "))
note2 = float(input("Veuillez entrez la note #2: "))
note3 = float(input("Veuillez entrez la note #3: "))
note4 = float(input("Veuillez entrez la note #4: "))
note5 = float(input("Veuillez entrez la note #5: "))

moyenne = (note1 + note2 + note3 + note4 + note5) /5

print(f'{moyenne:.2}')
