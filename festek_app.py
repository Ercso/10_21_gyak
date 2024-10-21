"""2. Feladat: Festék mennyiségének számítása
Készítsünk programot, amely egy szoba falainak kifestéséhez szükséges festék mennyiségét számolja ki.
A program kérje be a szoba szélességét, hosszát és magasságát méterben, valamint azt, hogy hány liter festéket vásároltunk már.
Tegyük fel, hogy 1 liter festék 10 négyzetmétert fed le.
Számolja ki, hogy hány liter festékre van szükség a szoba kifestéséhez, és közölje, hogy elegendő-e a festék, vagy szükség van-e további mennyiség beszerzésére."""


szelesseg = float(input("Add meg a fal szélességét (pl 10.1) m-ben: "))
hossz = float(input("Add meg a fal hosszát (pl 10.1) m-ben: "))
magassag = float(input("Add meg a fal magasságát (pl 10.1) m-ben: "))
festek_vasarolt = float(input("Add meg hány liter festéked van már (pl 10.1) l-ben: "))

fal1 = (magassag * szelesseg) * 2
fal2 = (magassag * hossz) * 2
szoba = fal1 + fal2
kell = szoba / 10
kell_meg = kell - festek_vasarolt
if kell > festek_vasarolt:
    print(f"Ez még nem elég festék. Szükséged van {kell_meg} festékre.")
else:
    print("Elegendő festéked van.")

