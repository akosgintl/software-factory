# Hol tartunk

Utolsó frissítés: 2026-10-18

## Fókusz

Egy AI-natív szoftvergyárat írunk le (0001). Nyolc álláspont van: 0001 definíció és AI-natív, 0002
kapuk (K0–K3) és mért bizalom, 0003 a vég a PR, bizonyítékkal, 0004 alacsony kockázat, 0005
scope-ellenőrzés, 0006 gráfmodell, 0007 elakadás, 0008 négy állomás (tervezés, build, ellenőrzés,
landing; mellékállapot: elakadt).

A gyárat típusos, időbeli gráfként írjuk le, és minden döntést megkötés, ítélet vagy mérőszám
formában fogalmazunk meg (0006). Minden kapun mindig van ítélet; ember vagy ember által jóváhagyott
szabály hozza, mintavétellel (0002). Az irányelvek az `elvek.md` fájlban vannak (E1–E11, M1–M4),
és mind a 27 megkötés visszavezethető rájuk. A kulcs: az autonómia úgy nő, hogy az ember tételek
helyett szabályokról dönt.

## Javasolt következő lépés

A váz konzisztens (konzisztencia-vizsgálat, 2026-10-18). Következő jelöltek: a szándék-szintű
elfogadás (több munkadarabra bomlott szándék), vagy a tanuló hurok (mit mér a gyár, és hogyan véd
a Goodhart-hatás ellen).

## Futó szálak

| Szál | Hol | Állapot |
|---|---|---|
| Definíció, AI-natív | `positions/0001-mit-ertunk-szoftvergyar-alatt.md` | 📌 elfogadva |
| Kapuk és bizalom | `positions/0002-emberi-kapuk-es-bizalom.md` | 📌 elfogadva |
| A vég és a bizonyíték | `positions/0003-a-veg-a-pr-bizonyitekkal.md` | 📌 elfogadva |
| Alacsony kockázat | `positions/0004-alacsony-kockazat.md` | 📌 elfogadva |
| Scope-ellenőrzés | `positions/0005-scope-conformance.md` | 📌 elfogadva |
| Gráfmodell, típuslista | `positions/0006-grafmodell.md` | 📌 elfogadva |
| Elakadás | `positions/0007-elakadas.md` | 📌 elfogadva |
| Négy állomás | `positions/0008-negy-allomas.md`, ábra: https://claude.ai/artifact/QfdY4btjwQMcAwXPBguZ2H | 📌 elfogadva |
| Irányelvek és megkötés-nyilvántartás | `elvek.md` | 📌 elfogadva |
| Fogalmi modell | `topics/fogalmi-modell.md` | 📌 elfogadva |
| Fogalomtár | `glossary.md` | 📌 minden használt fogalom definícióval |
| Folyamat-összevetés (saját és publikus gyárak) | `topics/folyamat-osszevetes.md` | 🔍 |
| A négy gyár-kísérlet | `experiments.md` | 🔍 a super-board és a warpdotdev-factory kapuit megnéztük; a fable- és az opus-factory csak az összevetésben |

## Utolsó napló

[`sessions/2026-10-18-fogalmi-modell.md`](sessions/2026-10-18-fogalmi-modell.md)
