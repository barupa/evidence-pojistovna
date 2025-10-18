class Pojisteny:
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno.strip().capitalize()
        self.prijmeni = prijmeni.strip().capitalize()
        self.vek = vek
        self.telefon = telefon.strip()

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni} \t {self.vek} \t {self.telefon}"