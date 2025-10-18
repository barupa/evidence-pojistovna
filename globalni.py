def nacti_pouze_pismena(prompt):
    while True:
        vstup = input(prompt).strip()
        if vstup.isalpha():
            return vstup
        else:
            print("Vyplněná hodnota musí obsahovat písmena.")

def nacti_pouze_cisla(prompt):
    while True:
        vstup = input(prompt).strip()
        if vstup.isdigit():
            return vstup
        else:
            print("Vyplněná hodnota může být pouze číslo bez mezer.")
