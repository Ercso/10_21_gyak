"""1. Feladat: Ajándékcsomagoló szalag számítás
Készítsünk programot, amely ajándékok csomagolásához szükséges szalag hosszát számolja ki.
A szalag hosszának úgy kell elegendőnek lennie, hogy kétszer körbeérje az ajándék körvonalát (téglalap alapú csomag esetén), és a masni készítéséhez további 50 cm szükséges.
A program kérje be az ajándék hosszát, szélességét és magasságát (cm-ben), az ajándékok számát, valamint a rendelkezésre álló szalag hosszát (méterben).
Számítsa ki, hogy hány méter szalagra van szükség a megadott számú ajándék csomagolásához, és közölje a felhasználóval, hogy elegendő-e a szalag."""
def festekszamlalo():

    hossz = float(input("Add meg a csomag hosszát (pl. 10.1) cm-ben: "))
    szelesseg = float(input("Add meg a csomag szélességét (pl. 10.1) cm-ben: "))
    magas = float(input("Add meg a csomag magasságát (pl. 10.1) cm-ben: "))
    szalag = float(input("Add meg a rendelkezésre álló szalag hosszát (pl 10.1) m-ben "))
    ajandek = int(input("Add meg az ajándékok számát (pl 1) db-ban:"))

    kerulet1 = (szelesseg +  magas) * 2
    kerulet2 = (hossz +  magas) * 2

    szalag_one_ajandek = kerulet1 + kerulet2 + 50

    szukseges_szaLag_cmben = szalag_one_ajandek * ajandek
    szukseges_szaLag_meterben = szukseges_szaLag_cmben / 100

    print(f"Az ajándék csomagolásához szükséges szalag {szukseges_szaLag_meterben} méter")

    if szalag < szukseges_szaLag_meterben:
        print(f"A rendelkezésre álló szalag nem elegendő. Szükség van még {szukseges_szaLag_meterben-szalag}.")
    else:
        print("A rendelkezésre álló szalag ELEGENDŐ")

festekszamlalo()
