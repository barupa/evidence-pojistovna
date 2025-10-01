from evidence import Evidence
from pojisteny import Pojisteny
from globalni import Globalni

def main():
    evidence = Evidence()
    globalni = Globalni()

print("*****************************")
print("     Evidence pojištěnců     ")
print("*****************************")
print("Dostupné akce:               ")
print("1 - Přidat nového pojištěnce ")
print("2 - Vypsat všechny pojištěnce")
print("3 - Vyhledat pojištěného     ")
print("4 - Konec                    ")
print("*****************************")
print("Jakou operaci chcete vykonat?")
akce=input()
if (akce == "1"):
    print("jede to")
elif (akce == "2"):
    print("jede to")
elif (akce == "3"):
    print("jede to")
elif (akce == "4"):   
    print("jede to")
else: 
    print("Neplatná operace")
    print("Jakou operaci chcete vykonat?")
    akce = input ()

