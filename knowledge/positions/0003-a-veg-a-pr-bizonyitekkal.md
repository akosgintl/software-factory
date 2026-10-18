# 0003 — A vég a PR, bizonyítékkal

Állapot: 📌 elfogadva · 2026-10-16 · módosítva 2026-10-16 (automatikus merge alacsony kockázatnál)

## Kérdés

Hol van a „vég”, ahol mindig ember validál (K3, lásd 0002): a PR merge vagy a release? És mi
alapján validál?

## Álláspont

1. **A vég a PR.** Implementáció → PR. Alapesetben ember fogadja el. **Alacsony kockázatnál lehet
   automatikus merge.** Az alacsony kockázat definíciója: `positions/0004-alacsony-kockazat.md`.
2. **A PR bizonyítékot hoz.** Nem elég a unit és az integrációs teszt. Kell:
   - teszt a futó rendszeren, end-to-end (e2e) is,
   - képernyőkép (vagy felvétel) a futásról.

   A bizonyíték négy tulajdonsága:
   - **AC-nként:** minden AC mellett ott a saját bizonyítéka.
   - **A commithoz kötött:** a head SHA-ról készült; ha a kód változik, elavul.
   - **Független:** nem a Builder állítja elő, hanem egy másik lane.
   - **Valódi környezet:** preview környezetben készül (PR-onként egy, a merge-ig él).
3. Az ember a bizonyítékot nézi a szándékhoz és az AC-hez képest. A diffet csak kockázat szerint
   (0002).

## Miért

- A unit és az integrációs teszt azt mutatja, hogy a részek működnek. Azt nem, hogy a felhasználó
  oldaláról teljesült-e a szándék.
- A képernyőkép és az e2e teszt az embernek gyorsan olvasható bizonyíték. A K3 akkor skálázódik, ha
  egy PR elfogadása perceket vesz igénybe, nem órákat.

## Mi szólt ellene

- A release mint vég jobban skálázódna: az ember csomagot fogadna el, nem minden PR-t. Ezt most
  elvetjük.
- Az e2e teszt lassú, drága, és hajlamos a véletlenszerű hibára (flaky).

## Mi változtatná meg

- Ha a K3-ra fordított emberi idő PR-onként nem csökkenthető, és az ember a szűk keresztmetszet,
  akkor újra kell nézni a release mint vég lehetőségét.
