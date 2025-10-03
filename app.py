from evidence import Evidence
from pojisteny import Pojisteny
from globalni import nacti_pouze_pismena, nacti_pouze_cisla

def main():
    evidence = Evidence()

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

        if akce == "1": ##
            __jmeno__ = nacti_pouze_pismena("Zadejte jméno pojištěnce: ")
            __prijmeni__ = nacti_pouze_pismena("Zadejte příjmení pojištěnce: ")
            __vek__ = nacti_pouze_cisla("Zadejte věk pojištěnce: ") 
            __tel_cislo__ = nacti_pouze_cisla("Zadejte telefonní číslo pojištěnce: ")
            __pojisteny__ = Pojisteny(__jmeno__,__prijmeni__,__vek__,__tel_cislo__)
            evidence.pridej_pojisteneho(__pojisteny__)
            print("Pojištěnec byl úspěšně přidán do evidence")

        elif akce == "2": ##
            pojisteni = evidence.vypis_vsechny()
            if pojisteni:
                for p in pojisteni:
                    print(p)
            else:
                print("Evidence je prázdná")
        
        elif akce == "3": ##
            jmeno = input("Zadejte jméno hledaného: ").strip()
            prijmeni = input("Zadejte příjmení hledaného: ").strip()
            evidence.najdi_pojisteneho(jmeno, prijmeni)
        elif akce == "4": ##
            print("Konec programu.")
            break
        else:
            print("Neplatná volba, zkuste znovu.")

if __name__ == "__main__":
    main()

