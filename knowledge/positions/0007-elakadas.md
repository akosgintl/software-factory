# 0007 — Elakadás: a kivételkezelés

Állapot: 📌 elfogadva · 2026-10-18

## Kérdés

Az ember „a hurok fölött” áll, és kivételnél lép be. Mi a kivétel, ki jelezheti, és mi történik
utána?

## Álláspont

1. **Az elakadás munkatermék.** Egy állomás-futás vagy a várt kimenetet állítja elő (terv, commit,
   bizonyíték, ítélet), vagy egy elakadást.
2. **Bármelyik sáv jelezhet elakadást** (andon zsinór).
3. **Az elakadás oda mutat, ahol a hiba van**, nem feltétlenül a munkadarabra. Ha a QA azt találja,
   hogy két AC ellentmond egymásnak, az elakadás a specre *vonatkozik*.

Invariánsok:

- **I-0007-1** Minden állomás-futás lezárul: vagy a várt kimenettel, vagy elakadással.
- **I-0007-2** Ha egy munkadarabra vagy annak forrására (terv, spec) elakadás vonatkozik, a
  munkadarab nem mehet tovább, amíg az elakadásra nem vonatkozik emberi ítélet.
- **I-0007-3** Egy munkadarabon legfeljebb 3 újramunka-kör lehet (build → ellenőrzés → vissza). A
  következő futás kötelezően elakadással zárul. A 3 konfiguráció, a tanuló hurok javasolhat
  változtatást.

Mérőszám:

- **elakadási arány** állomásonként és kategóriánként. Megmutatja, hol gyenge a gyár.

## Miért

- Kivételkezelés nélkül az ágens vagy végtelen hurokba kerül, vagy csendben gyenge munkát ad le.
- Ha az elakadás a specre mutat, a spec új verziót kap, és az I-0002-2 miatt minden ráépülő
  jóváhagyás érvénytelen lesz. A visszalépést nem kell külön szabályként kitalálni, a meglévő
  invariánsból következik.

## Mi szólt ellene

- Goodhart: ha az elakadási arány „rossz” jel, a gyár megtanul nem elakadni, és gyenge munkát ad le
  helyette. Védelem: az elakadás információ, nem hiba. A rossz jel a merge utáni átcsúszott hiba.
  Kevés elakadás és sok átcsúszott hiba együtt azt jelenti, hogy a gyár hallgat.

## Mi változtatná meg

- Ha az emberi idő nagy része elakadások feloldására megy el, akkor vagy a kapuk előtti munka
  gyenge (spec, terv), vagy a 3-as korlát túl szigorú.
