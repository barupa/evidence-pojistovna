from evidence import Evidence
from pojisteny import Pojisteny
from globalni import nacti_pouze_pismena, nacti_pouze_cisla

def main():
    evidence = Evidence()
    pojisteny = Pojisteny()


    while True:
        print("*****************************")
        print("     Evidence pojištěnců     ")
        print("*****************************")
        print("Dostupné akce:               ")
        print("1 - Přidat nového pojištěnce ")
        print("2 - Vypsat všechny pojištěnce")
        print("3 - Vyhledat pojištěného     ")
        print("4 - Konec                    ")
        print("*****************************")
        print("Jakou akci chceš vykonat?")
        akce=input()

        if akce == "1":
            __jmeno__ = nacti_pouze_pismena("Zadejte jméno pojištěnce: ")
            __prijmeni__ = nacti_pouze_pismena("Zadejte příjmení pojištěnce: ")
            __vek__ = nacti_pouze_cisla("Zadejte věk pojištěnce: ") 
            __tel_cislo__ = nacti_pouze_cisla("Zadejte telefonní číslo pojištěnce: ")
        elif akce == "2":
            print("jede to")
        elif akce == "3":
            print("jede to")
        elif akce == "4":   
            print("jede to")
            break
        else: 
            print("Neplatná operace")

if __name__ == "__main__":
    main()

