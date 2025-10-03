from pojisteny import Pojisteny

class Evidence:
    def __init__(self):
        self._pojisteni: list[Pojisteny] = [
            Pojisteny("Pavel", "Jetel", 35, "777777777"),
            Pojisteny("Pavel", "Letěl", 35, "777777777"),
            Pojisteny("Pavel", "Plevel", 35, "777777777"),
            Pojisteny("Pavel", "Level", 35, "777777777"),
            Pojisteny("Pavel", "Neger", 35, "777777777"),
            Pojisteny("Pavel", "Seděl", 35, "777777777"),
            Pojisteny("Pavel", "Hleděl", 35, "777777777"),
            Pojisteny("Pavel", "Přijel", 35, "777777777"),
            Pojisteny("Pavel", "Vletěl", 35, "777777777"),
        ]

    def pridej_pojisteneho(self, pojisteny: Pojisteny) -> None:
        self._pojisteni.append(pojisteny)

    def vypis_vsechny(self) -> list[Pojisteny]:

        return self._pojisteni

    def najdi_pojisteneho(self, jmeno: str, prijmeni: str):
        nalezeni = [
            p for p in self._pojisteni
            if p.jmeno.lower() == jmeno.lower() and p.prijmeni.lower() == prijmeni.lower()
        ]
        if nalezeni:
            for p in nalezeni:
                print(p)
        else:
            print("Pojištěný nebyl nalezen.")