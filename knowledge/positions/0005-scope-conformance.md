# 0005 — Scope-ellenőrzés (scope conformance): a PR nem csinál többet, mint amit az AC-k kérnek

Állapot: 📌 elfogadva · 2026-10-16

## Kérdés

A 0004 szerint a sorok száma nem számít. Mi akadályozza meg, hogy egy PR többet változtasson, mint
amit az AC-k leírnak? A bizonyíték (0003) csak azt igazolja, hogy az AC-k teljesültek, azt nem,
hogy más nem változott.

## Álláspont

1. **Kell scope-ellenőrzés.** Egy független reviewer a diff minden részét visszavezeti egy AC-re.
   Az AC-ket és a diffet a Builder beszámolója *előtt* olvassa. Ami nem vezethető vissza, az
   kéretlen változás (scope drift).
2. **A kéretlen változás nem maradhat a PR-ban.** Vagy kikerül belőle, vagy külön munkadarab lesz a
   Backlogban, és arról ember dönt (K1, 0002).
3. **A gyár által javasolt munkadarab nem kerülheti ki a K1-et.** Akkor sem mehet egyenesen a Ready
   oszlopba, ha az ágens AC-t is írt hozzá.
4. **A 0004 negyedik feltétele bővül:** alacsony kockázatú csak az a PR, amelyben nincs kéretlen változás.
   Az AC eléréséhez szükséges mellékváltozás (teszt, átnevezés, kis előkészítő módosítás)
   megengedett, de ha a közös magot érinti, a 3. feltétel (hatókör) emberhez küldi.
5. **Az erózió ellen:** a Backlogban álló refaktor-munkadarabok száma és kora a tanuló hurok
   mérőszáma. Ha nő, a gyár refaktor-kört javasol, és arról ember dönt.

## Miért

- A méret-küszöb elhagyása után ez fogja meg azt a változtatást, amit senki nem kért.
- A kéretlen „rendbetétel” a közös kódban viselkedést változtathat úgy, hogy az e2e zöld marad.
- A 0001 elve: a gyár javasol, az ember dönt. A mellékesen észrevett munka javaslat, nem feladat.
- 🔍 A super-review már így dolgozik: *Scope drift* és *Over-engineering* találati osztály, előbb AC
  és diff, utána a Builder beszámolója, a refaktor a Backlogba megy (`experiments.md`).

## Mi szólt ellene

- Ha minden mellékes javítás külön munkadarabra megy, a kód nem javul, csak a Backlog nő. A
  scope-ellenőrzés így gyorsíthatja is az architektúra erózióját. Erre válasz az 5. pont.
- A „visszavezethető egy AC-re” ítélet ágensé, és lehet engedékeny. Védelem: a reviewer független,
  és a 0004 szerinti 10%-os emberi mintavétel ezt is ellenőrzi.
- Plusz egy review-kör PR-onként. Ez ágensidő, nem emberi idő, ezért vállalható.

## Mi változtatná meg

- Ha a refaktor-munkadarabok tartósan felgyűlnek, és az emberi refaktor-körök nem győzik, akkor
  megengedhető lesz egy szűk, előre definiált „cserkész” mellékváltozás (például elnevezés,
  holt kód törlése a módosított fájlban), de csak levél-modulban.
