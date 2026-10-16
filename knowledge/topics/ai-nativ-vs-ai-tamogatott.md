# AI-natív és AI-támogatott szoftvergyár

Kiinduló keret. Minden állítás 💭 hipotézis, amíg meg nem vitatjuk.

## A szoftvergyár mint ötlet

💭 A szoftvergyár régi ötlet. Lényege, hogy a szoftverfejlesztést ismételhető, mérhető, iparszerű
folyamattá szervezzük, egyedi kézművesség helyett. Két korábbi hullám:

- **Japán szoftvergyárak (1970-80-as évek).** Hitachi, Toshiba, NEC, Fujitsu. Szabványos folyamat,
  újrahasznosítás, minőségmérés. Cusumano könyve dolgozza fel (lásd `sources.md`).
- **Microsoft Software Factories (2004 körül).** Modellvezérelt fejlesztés, domain-specifikus
  nyelvek, termékcsaládok. Greenfield és Short könyve (lásd `sources.md`).

💭 Mindkét hullám ugyanott akadt el. A folyamatot lehetett szabványosítani, a munkát végző embert
nem. Az AI-hullám új eleme, hogy a munkát végző „munkás” maga is szabványosítható, másolható és
párhuzamosítható.

## A két pólus

| Szempont | AI-támogatott | AI-natív |
|---|---|---|
| Ki a fő munkavégző | ember, AI-eszközzel | ágens, ember a rendszer körül |
| Az ember helye | a hurokban (in the loop), minden lépésnél | a hurok fölött (on the loop), kivételeknél és kapuknál |
| A munka egysége | fejlesztői feladat | specifikáció elfogadási feltételekkel (AC) |
| A folyamat | a meglévő (Scrum, emberi code review), AI-val gyorsítva | az ágensekre tervezve: lane-ek, kapuk, bizonyíték |
| Szűk keresztmetszet | emberi figyelem és gépelés | specifikáció minősége és ellenőrzési kapacitás |
| Mit mérünk | fejlesztői produktivitás | átfutás kártyánként, újramunka aránya, emberi érintés merge-enként |
| A dokumentáció olvasója | ember | elsősorban ágens (AGENTS.md, skillek, ellenőrizhető AC) |

## Spektrum, nem kettősség

💭 Az önvezető autók szintjeihez hasonló skála segíthet:

| Szint | Név | Az ember szerepe | Példa |
|---|---|---|---|
| L0 | kézi | mindent ő csinál | — |
| L1 | kiegészítés | gépel, az AI sort vagy blokkot javasol | autocomplete |
| L2 | pár | beszélget, az AI fájlokat ír, az ember minden lépést lát | chat, pair programming |
| L3 | feladat-ágens | feladatot ad, minden PR-t átnéz | egy ágens, egy ticket, emberi review |
| L4 | kapuzott folyamat | specifikációt ír és szabályt állít, csak a kivételeknél lép be | build, QA, review lane-ek, merge gate |
| L5 | önirányító | célt és határt ad, a backlogot is ágensek töltik | telemetriából ticket, ágens prioritizál |

💭 Az AI-támogatott sáv nagyjából L1–L3, az AI-natív L4–L5. A határ L3 és L4 között van. Ott
fordul meg, hogy az ember a munka része vagy a rendszer tervezője.

💭 A repó super-board kísérlete L4 körül áll, L5 elemekkel (a `super-collect` telemetriából tölti a
backlogot). Lásd `experiments.md`.

## Feszültségek, amelyeket érdemes végiggondolni

- **Hová kerül a szűk keresztmetszet?** Ha az ágens gyorsan ír kódot, a lassú rész a specifikáció,
  az ellenőrzés és a döntés lesz.
- **Bizalom.** Mi helyettesíti azt, hogy „egy ember látta”? Bizonyíték alapú QA, független
  ellenőrző, kontradiktórius review, kockázat alapú merge kapu.
- **Entrópia.** Sok kis helyi változtatás gyorsabban erodálhatja az architektúrát, mint az emberi
  csapat. Ki őrzi az egészet?
- **Gazdaságosság.** Token- és számítási költség az emberi idővel szemben. Hol fordul át?
- **Az ember szerepe.** Milyen képesség marad értékes: specifikáció, ízlés, szabályalkotás,
  kivételkezelés?
