"""1. Páros és páratlan számok szétválogatása (1-től 20-ig)
Feladat: Írd ki külön a páros és a páratlan számokat 1-től 20-ig.

Páros számok: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20
Páratlan számok: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19"""
def elsofeladat():

    parosak = []
    paratlanok = []

    for i in range(1, 21):
        if i % 2 == 0:
            parosak.append(i)
        else:
            paratlanok.append(i)
    print(f"Páros számok: {parosak}")
    print(f"Páratlan számok: {paratlanok}")

"""2. Számok faktoriálisa
Feladat: Számold ki egy adott szám faktoriálisát!

Ha az adott szám 5, a faktoriálisa: 5! = 5 × 4 × 3 × 2 × 1 = 120
"""
szam = 5

for i in range(1, szam, +1):

"""3. Számok összegének és átlagának kiszámolása
Feladat: Számold ki az 1-től egy adott számig lévő számok összegét és átlagát!
Ha az adott szám 10:
Összeg: 1 + 2 + 3 + ... + 10 = 55
Átlag: 55 ÷ 10 = 5.5
"""

"""4. Egymásba ágyazott for ciklusok: szorzótábla megjelenítése
Feladat: Készítsd el az 1-től 10-ig tartó szorzótáblát!

Szorzótábla 1-től 10-ig:
1 × 1 = 1, 1 × 2 = 2, ..., 1 × 10 = 10
2 × 1 = 2, 2 × 2 = 4, ..., 2 × 10 = 20
...
10 × 1 = 10, 10 × 2 = 20, ..., 10 × 10 = 100
"""

"""5. Fibonacci-sorozat generálása
Feladat: Írd ki a Fibonacci-sorozat első 10 számát!

Fibonacci-sorozat első 10 száma: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34"""
#elsofeladat()