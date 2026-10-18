# 0003 — A vég a PR, bizonyítékkal

Állapot: 📌 elfogadva · 2026-10-16 · módosítva 2026-10-16 (alacsony kockázatnál szabály fogad el) ·
pontosítva 2026-10-18 (bizonyíték nem UI-változásnál)

## Kérdés

Hol van a „vég”, ahol mindig van elfogadás (K3, 0002): a PR merge vagy a release? És mi alapján
fogadunk el?

## Álláspont

1. **A vég a PR.** Implementáció → PR → K3 elfogadás → landing. Alapesetben ember fogad el,
   alacsony kockázatnál szabály (`positions/0004-alacsony-kockazat.md`).
2. **A PR bizonyítékot hoz.** Nem elég a unit és az integrációs teszt. Kell:
   - e2e teszt a futó rendszeren;
   - ha az AC felhasználói felületet érint, képernyőkép vagy felvétel a futásról.

   A gyár saját konfigurációját változtató PR-nál a futó rendszer maga a gyár: a bizonyíték egy
   eval-futás a változott konfigurációval.

   A bizonyíték négy tulajdonsága:
   - **AC-nként:** minden AC mellett ott a saját bizonyítéka.
   - **A commithoz kötött:** a head SHA-ról készült. Ha a kód változik, elavul.
   - **Független:** nem a Builder állítja elő, hanem a QA (`glossary.md`: független).
   - **Valódi környezet:** preview környezetben készül (PR-onként egy, a merge-ig él).
3. Az elfogadó a bizonyítékot nézi a szándékhoz és az AC-hez képest. A diffet csak kockázat szerint
   (0002).

## Megkötések

- **I-0003-1** A munkadarab minden AC-jére *igazol* legalább egy bizonyíték.
- **I-0003-2** A bizonyítékot előállító futás *használta* a PR aktuális head commitját. Ha a head
  változik, a bizonyíték elavul.
- **I-0003-3** A bizonyítékot előállító futás független a commitot előállító futástól.
- **I-0003-4** Minden bizonyíték preview környezetben készült. A bizonyítékok között van e2e
  eredmény, és felhasználói felületet érintő AC-nél képernyőkép vagy felvétel is.

## Miért

- A unit és az integrációs teszt azt mutatja, hogy a részek működnek. Azt nem, hogy a felhasználó
  oldaláról teljesült-e a szándék.
- A képernyőkép és az e2e teszt az embernek gyorsan olvasható bizonyíték. A K3 akkor skálázódik, ha
  egy PR elfogadása perceket vesz igénybe, nem órákat.
- A független bizonyítékot a Builder nem tudja „megrendezni” (Goodhart-hatás).

## Mi szólt ellene

- A release mint vég jobban skálázódna: az ember csomagot fogadna el, nem minden PR-t. Ezt most
  elvetjük.
- Az e2e teszt lassú, drága, és lehet flaky (`questions.md`).
- 💭 Hogy a bizonyíték preview környezetben készült, és hogy egy AC felhasználói felületet érint,
  egy szereplő állítása (attribútum). A gráf csak azt rögzíti, ki állította (0006, `questions.md`).
- 💭 Hogy az elfogadó a diffet csak kockázat szerint nézi: a gráf rögzítheti, hogy *használta* a
  diffet, azt nem, hogy meg is nézte.

## Mi változtatná meg

- Ha a K3-ra fordított emberi idő PR-onként nem csökkenthető, és az ember a szűk keresztmetszet,
  akkor újra kell nézni a release mint vég lehetőségét.
