def nacti_pouze_pismena(prompt):
    while True:
        vstup = input(prompt).strip()
        if vstup.isalpha():
            return vstup
        else:
            print("Vstup můžou být pouze písmena!!!")

def nacti_pouze_cisla(prompt):
    while True:
        vstup = input(prompt).strip()
        if vstup.isdigit():
            return vstup
        else:
            print("Vstup může být pouze číslo!!!")
