# 0005 — Scope-ellenőrzés (scope conformance): a PR nem csinál többet, mint amit az AC-k kérnek

Állapot: 📌 elfogadva · 2026-10-16 · módosítva 2026-10-18 (minden gyár-javaslat szándék-javaslat,
K0-n megy át)

## Kérdés

A 0004 szerint a sorok száma nem számít. Mi akadályozza meg, hogy egy PR többet változtasson, mint
amit az AC-k leírnak? A bizonyíték (0003) csak azt igazolja, hogy az AC-k teljesültek, azt nem,
hogy más nem változott.

## Álláspont

1. **Kell scope-ellenőrzés.** Egy független Reviewer a diff minden diffrészét visszavezeti egy
   AC-re. Az AC-ket és a diffet a Builder beszámolója *előtt* olvassa. Ami nem vezethető vissza, az
   kéretlen változás (scope drift).
2. **A kéretlen változás nem maradhat a PR-ban.** Vagy kikerül belőle (újramunka), vagy
   szándék-javaslat lesz belőle a backlogban.
3. **Minden gyár-javaslat szándék-javaslat.** A review-lelet, az átcsúszott hiba, az elakadás, a
   telemetria és a tanuló hurok javaslata egyaránt szándékként kerül a backlogba. K0-n megy át
   (I-0002-5), utána K1-en és K2-n, mint bármelyik szándék. Munkadarab csak tervből jöhet. A
   szándék *származik* éle a javaslat forrására mutat.
4. **Megengedett mellékváltozás:** ami az AC eléréséhez kell (teszt, átnevezés, kis előkészítő
   módosítás). Ha a közös magot érinti, a 0004 3. feltétele (hatókör) emberhez küldi. Ha kéretlen
   változás van, a PR nem alacsony kockázatú (0004, 4. feltétel).
5. **Az erózió ellen:** a backlogban álló refaktor-szándékok száma és kora mérőszám. Ha nő, a gyár
   refaktor-kört javasol (szándék-javaslat), és arról ember dönt (K0).

## Megkötések

- **I-0005-1** A PR minden diffrészéből *teljesít* él vezet a munkadarab egy AC-jéhez.
- **I-0005-2** A scope-ítéletet hozó futás független a commitot előállító futástól.
- **I-0005-3** A scope-ítéletet hozó futás előbb *használta* az AC-ket és a diffet, és csak utána a
  Builder beszámolóját (az időbélyegek sorrendje).
- ~~**I-0005-4**~~ Visszavonva (2026-10-18): a review-ból nem lesz munkadarab, ezért az I-0002-5
  elég.

Mérőszám: a refaktor-szándékok száma és kora a backlogban.

## Miért

- A méret-küszöb elhagyása után ez fogja meg azt a változtatást, amit senki nem kért.
- A kéretlen „rendbetétel” a közös kódban viselkedést változtathat úgy, hogy az e2e zöld marad.
- A 0001 elve: a gyár javasol, az ember dönt. A mellékesen észrevett munka javaslat, nem feladat.
- Ha a javaslatból egyenesen munkadarab lenne, megkerülné a K0-t, a K1-et és a K2-t, és a terv nem
  volna a felbontás egyetlen helye.
- 🔍 A super-review már majdnem így dolgozik: van *Scope drift* és *Over-engineering* találati
  osztálya, előbb az AC-t és a diffet olvassa, a refaktor a Backlogba megy (`experiments.md`).

## Mi szólt ellene

- Ha minden mellékes javítás külön szándék lesz, a kód nem javul, csak a backlog nő. Így a
  scope-ellenőrzés gyorsíthatja is az architektúra erózióját. Erre válasz az 5. pont.
- Egy kis javításból is teljes kör lesz (K0, K1, K2). Válasz: a K0 kötegelhető, és a kis szándékok
  kategóriájában a K1 és a K2 szabályra kerülhet (0002).
- A „visszavezethető egy AC-re” ítélet ágensé, és lehet engedékeny. Védelem: a Reviewer független,
  és a szabály által elfogadott PR-ok mintavétele (0002) ezt is ellenőrzi.
- Plusz egy review-kör PR-onként. Ez ágensidő, nem emberi idő, ezért vállalható.

## Mi változtatná meg

- Ha a refaktor-szándékok tartósan felgyűlnek, és a refaktor-körök nem győzik, akkor megengedhető
  lesz egy szűk, előre definiált „cserkész” mellékváltozás (például elnevezés, holt kód törlése a
  módosított fájlban), de csak levél-modulban.
