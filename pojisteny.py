class Pojisteny:
    def __init__(self, jmeno: str, prijmeni: str, vek: int, telefon: str):
        if not jmeno.strip() or not prijmeni.strip():
            raise ValueError("Jméno a příjmení nesmí být prázdné.")
        self.jmeno = jmeno.strip().capitalize()
        self.prijmeni = prijmeni.strip().capitalize()
        self.vek = vek
        self.telefon = telefon.strip()

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni} \t {self.vek} \t {self.telefon}"