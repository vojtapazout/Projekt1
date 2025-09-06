uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "Mike": "password123",
    "liz": "pass123"
}

jmeno = input("Zadej uživatelské jméno: ")
heslo = input("Zadej heslo: ")

if uzivatele.get(jmeno) == heslo:
    print(f"Ahoj {jmeno}, vítej v aplikaci! Můžeš pokračovat v analýze textů.")
else:
    print("Uživatelské jméno nebo heslo nejsou v pořádku. Ukončuji program.")
    exit()

texty = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',

    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',

    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

print("Vyber text podle čísla (0, 1, 2):")
volba = input("Zadej číslo textu: ")

if not volba.isdigit():
    print(" Neplatný vstup, musíš zadat číslo.")
    exit()

index = int(volba)
if index < 0 or index >= len(texty):
    print(" Číslo mimo rozsah dostupných textů.")
    exit()

text = texty[index]
slova = text.split()

pocet_slov = len(slova)
zacina_velkym = sum(1 for slovo in slova if slovo[0].isupper())
velkymi = sum(1 for slovo in slova if slovo.isupper())
malymi = sum(1 for slovo in slova if slovo.islower())
cisla = [int(slovo) for slovo in slova if slovo.isdigit()]
pocet_cisel = len(cisla)
soucet_cisel = sum(cisla)

print("\n Výsledky analýzy:")
print(f"Počet slov: {pocet_slov}")
print(f"Slov začínajících velkým písmenem: {zacina_velkym}")
print(f"Slov psaných VELKÝMI písmeny: {velkymi}")
print(f"Slov psaných malými písmeny: {malymi}")
print(f"Počet čísel: {pocet_cisel}")
print(f"Součet čísel: {soucet_cisel}")

print("\n Graf četnosti délek slov:")
delky = {}
for slovo in slova:
    delka = len(slovo)
    delky[delka] = delky.get(delka, 0) + 1

for delka in sorted(delky):
    print(f"{delka:2} | {'*' * delky[delka]} ({delky[delka]})")
print("\n Děkuji za použití aplikace. Měj hezký den!")