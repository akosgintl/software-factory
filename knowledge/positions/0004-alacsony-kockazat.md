# 0004 — Alacsony kockázat: mikor merge-ölhet a gyár ember nélkül

Állapot: 📌 elfogadva · 2026-10-16 · módosítva 2026-10-18 (a gyár saját szabályai kemény kategória, E8)

## Kérdés

A 0003 szerint alacsony kockázatnál lehet automatikus merge. Mi az alacsony kockázat?

## Álláspont

Kockázat = mi romolhat el × mennyire látjuk × mennyire vonható vissza.

Egy PR akkor alacsony kockázatú, ha **mind az öt feltétel teljesül**. Ha bármelyik nem, ember dönt.

1. **Nincs kemény kategória:** pénz, auth és jogosultság, adat (séma, migráció, törlés), személyes
   adat, publikus API vagy szerződés, infrastruktúra és titkok, új függőség, **a gyár saját
   szabályai és működése** (konfiguráció, küszöb, kemény lista, skill, ágens-utasítás,
   munkafolyamat; E8).
2. **Egy reverttel visszavonható:** nincs külső mellékhatás, nincs olyan adatírás, amit a revert
   nem hoz vissza.
3. **Kicsi hatókör:** a változtatás nem a közös magot érinti, kevés hívója van (fan-in). **A sorok
   száma nem számít.**
4. **Teljes bizonyíték:** minden AC-hez bizonyíték (0003), az e2e zöld, a változott kódot teszt fedi,
   és nincs kéretlen változás (0005).
5. **Jó előélet:** a kategória és a kódterület mért átcsúszási aránya a küszöb alatt van.

Három szabály:

- **A kockázat csak felfelé módosítható.** Az ágens emelheti, csökkenteni nem. A Builder nem
  minősíti a saját munkáját.
- **A kemény kategóriák listáját csak ember változtatja.** A tanuló hurok az 5. feltétel küszöbét
  javasolhatja, az 1. listát nem.
- **Mintavételezés:** az automatikusan merge-ölt PR-ok 10%-át utólag ember nézi meg. Az arány
  módosítható. Ebből jön az átcsúszási arány az 5. feltételhez.

## Miért

- Az ember nem a diffet nézi (0002), ezért a sorok száma nem az ő terhét méri. A kockázatot az
  méri, hogy mit érint a változtatás, és mennyire látjuk az eredményét.
- Mintavétel nélkül az automatikusan merge-ölt kategóriákról nincs adat, és a bizalom vakon nő.
- A „csak felfelé” szabály és az emberi kézben tartott kemény lista véd a Goodhart-hatás ellen.

## Mi szólt ellene

- A sorok száma a hibavalószínűség durva, de olcsó jelzője. Elvetettük, mert a hatókör és a
  bizonyíték jobban mér.
- Egy nagy PR könnyen többet változtat, mint amit az AC-k leírnak. Ezt a bizonyíték nem fedi le.
  Pótlék: scope-ellenőrzés, lásd `positions/0005-scope-conformance.md`.

## Mi változtatná meg

- Ha a mintavétel azt mutatja, hogy a nagy, de „kis hatókörű” PR-ok átcsúszási aránya magasabb,
  akkor a méret visszakerül jelzőként.
