# 0007 — Elakadás: a kivételkezelés

Állapot: 📌 elfogadva · 2026-10-18 · módosítva 2026-10-18 (hová megy vissza a munka)

## Kérdés

Az ember „a hurok fölött” áll, és kivételnél lép be. Mi a kivétel, ki jelezheti, és mi történik
utána?

## Álláspont

1. **Az elakadás munkatermék.** Egy állomás-futás vagy a várt kimenetet állítja elő (terv, commit,
   bizonyíték, ítélet), vagy egy elakadást.
2. **Bármelyik sáv jelezhet elakadást** (andon zsinór).
3. **Az elakadás oda mutat, ahol a hiba van** (*vonatkozik* él), nem feltétlenül a munkadarabra.
   Ha a QA azt találja, hogy két AC ellentmond egymásnak, az elakadás a specre vonatkozik.
4. **Az elakadást ember oldja fel** (feloldás). Az elakadás jelzője javasol célt. Az alapértelmezés:
   ott folytatódik, ahol elakadt. Az ember bármelyik korábbi pontot választhatja:

   | Döntés | Hová megy vissza | Mi lesz érvénytelen |
   |---|---|---|
   | folytat | ugyanoda | semmi |
   | build | a munkadarab újra buildbe | a PR bizonyítékai és a PR-ra vonatkozó ítéletek |
   | terv | tervezés, a terv új verziója | K2, a terv összes még nem merge-ölt munkadarabja |
   | spec | tervezés, a spec új verziója | K1, K2 és minden, ami belőlük származik |
   | szándék | backlog, újra K0 | minden |
   | lezár | sehová, a szándék lezárul | — |

   Előre ugrani nem lehet. A már merge-ölt munkadarabokat nem lehet visszacsinálni; az új
   tervnek számolnia kell velük.

## Megkötések

- **I-0007-1** Egy állomás-futás legfeljebb T ideig lehet nyitott. Ha addig nem zárul a várt
  kimenettel, elakadással zárul. A T konfiguráció, állomásonként.
- **I-0007-2** Ha egy munkadarabra vagy annak forrására (terv, spec, szándék) elakadás vonatkozik,
  a munkadarab nem mehet tovább, amíg az elakadásra nem vonatkozik ember által hozott feloldás.
- **I-0007-3** Egy munkadarabon legfeljebb N újramunka-kör lehet (build → ellenőrzés → vissza). A
  következő futás kötelezően elakadással zárul. Az N konfiguráció, alapból 3.
- **I-0007-4** A feloldás célja ugyanaz az állomás vagy egy korábbi. Előre nem mutathat.
- **I-0007-5** Visszaküldéskor a cél munkatermék új verziót kap. A belőle származó, még nem
  merge-ölt munkatermékekre vonatkozó ítéletek és bizonyítékok érvénytelenek. (Levezetett: az
  I-0002-2-ből és az I-0003-2-ből következik.)
- **I-0007-6** Visszaküldéskor az újramunka-számláló újraindul, mert a munkadarab új verziója új
  munka.

Mérőszám:

- **elakadási arány** állomásonként és kategóriánként. Megmutatja, hol gyenge a gyár.

## Miért

- Kivételkezelés nélkül az ágens vagy végtelen hurokba kerül, vagy csendben gyenge munkát ad le.
- Ha az elakadás a specre mutat, a spec új verziót kap, és az I-0002-2 miatt minden ráépülő ítélet
  érvénytelen lesz. A visszalépést nem kell külön szabályként kitalálni, a meglévő megkötésből
  következik.
- Az I-0007-1 korábban „minden futás lezárul” volt. Ez liveness, ezért időkorláttal lett megkötés
  (0006, 4a).

## Mi szólt ellene

- Goodhart: ha az elakadási arány „rossz” jel, a gyár megtanul nem elakadni, és gyenge munkát ad le
  helyette. Védelem: az elakadás információ, nem hiba. A rossz jel a merge utáni átcsúszott hiba.
  Kevés elakadás és sok átcsúszott hiba együtt azt jelenti, hogy a gyár hallgat.

## Mi változtatná meg

- Ha az emberi idő nagy része elakadások feloldására megy el, akkor vagy a kapuk előtti munka
  gyenge (spec, terv), vagy az újramunka-korlát túl szigorú.
