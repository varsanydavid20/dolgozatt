fajl = open("lotto.txt", "r")
szamok = {}
sorok = 0

# Fájl olvasása és számok számlálása
for sor in fajl:
    sorok += 1
    szamok_sor = sor.strip().split()
    for szam in szamok_sor:
        if szam in szamok:
            szamok[szam] += 1
        else:
            szamok[szam] = 1

fajl.close()

"""1.

print("=" * 50)
print(f"1. Hány hét sorsolása van benne?")
print(f"   {sorok} hét sorsolása található a fájlban")
print()

rendezett = sorted(szamok.items(), key=lambda x: x[1], reverse=True)
"""


"""2.

print("=" * 50)
print("2. A nyerőszámok (gyakoriság szerint):")
print("-" * 50)
for szam, gyakorisag in rendezett:
    print(f"{szam}: {gyakorisag} alkalommal")
print()
"""


"""3.

print("=" * 50)
print("3. A leggyakoribb szám:")
leggyakoribb_szam = rendezett[0][0]
leggyakoribb_gyakorisag = rendezett[0][1]
print(f"   A '{leggyakoribb_szam}' szám a leggyakoribb ({leggyakoribb_gyakorisag} alkalommal)")
print()
"""


"""4.

print("=" * 50)
print("4. Add meg az 5 számot!")
tipp = []
for i in range(5):
    while True:
        try:
            szam = input(f"   {i+1}. szám: ")
            tipp.append(szam)
            break
        except:
            print("   Hibás bemenet, próbáld újra!")

talalaatok = 0
for szam in tipp:
    if szam in szamok:
        talalaatok += 1

print()
print("=" * 50)
print(f"   Az ön tippje: {', '.(tipp)}")
print(f"   Találat: {talalaatok} szám")
for szam in tipp:
    if szam in szamok:
        print(f"{szam}: {szamok[szam]} alkalommal húzták")
    else:
        print(f"{szam}: nem fordult elő")
print()
"""



"""5.

print("=" * 50)
print("5. A tuti tipp (leggyakoribb 5 szám):")
tuti_tipp = rendezett[:5]
tuti_szamok = [szam for szam, gyakorisag in tuti_tipp]
print(f"   {', '.join(tuti_szamok)}")

with open("tipp.txt", "w") as tip_fajl:
    tip_fajl.write("TUTI TIPP\n")
    tip_fajl.write("=" * 30 + "\n")
    tip_fajl.write("A leggyakoribb 5 szám:\n")
    for i, (szam, gyakorisag) in enumerate(tuti_tipp, 1):
        tip_fajl.write(f"{i}. {szam} ({gyakorisag} alkalommal)\n")
    tip_fajl.write("\nTipp szamok: " + " ".join(tuti_szamok) + "\n")

print("   A tipp.txt fájl elkészült!")
print("=" * 50)
"""