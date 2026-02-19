
class magassag:
    pass

f=open("nem az/diak.txt","r",encoding="utf-8")
adatok=f.read()

print(adatok)

adatok=adatok.split("\n")
db=0
print(f"Az diakok száma: {len(adatok)} fő")
max_cm = 0
legmagasabbak = []

for sor in adatok:
    if sor.strip():
        nev, cm = sor.strip().split(";")
        cm = int(cm)
        if cm > max_cm:
            max_cm = cm
            legmagasabbak = [nev]
        elif cm == max_cm:
            legmagasabbak.append(nev)
print(f"Legmagasabb diák: {legmagasabbak[0]} ({max_cm} cm)")

csokkeno_sorrend = []
for sor in adatok:
    if sor.strip():
        nev, cm = sor.strip().split(";")
        csokkeno_sorrend.append((nev, int(cm)))

csokkeno_sorrend.sort

for nev, cm in csokkeno_sorrend:
   print(f"{nev}: {cm} cm")
f.close()