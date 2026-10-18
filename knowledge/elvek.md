# Irányelvek

📌 2026-10-18. Rövid, emberi mondatok, amelyekből az álláspontok és a megkötések következnek. A
visszavezethetőség itt is kétirányú: minden irányelv mellett ott állnak a megkötései, és minden
megkötés legalább egy irányelvhez tartozik. Ha valamelyik hiányzik, az rés.

## A gyár irányelvei

| # | Irányelv | Honnan | Megkötések |
|---|---|---|---|
| E1 | **A gyár javasol és végrehajt, az ember dönt és validál**: tételenként, vagy az általa jóváhagyott szabályon át. | 0001 | I-0002-3, I-0002-5 |
| E2 | **Az ember mindig validált elemet kap.** Minden kapu előtt független eval és review jön, akkor is, ha a kapun szabály dönt. Az ember e fölé kerül, nem helyette van. | 0008 | I-0008-4 |
| E3 | **Senki nem minősíti a saját munkáját.** | 0003, 0004, 0005 | I-0003-3, I-0004-3, I-0005-2, I-0005-3, I-0008-4 |
| E4 | **Az autonómia úgy nő, hogy az ember tételek helyett szabályokról dönt**, és a szabály ítéleteiből mindig mintát néz. | 0001, 0002 | I-0002-6 |
| E5 | **Ember nélkül csak az alacsony kockázat megy át, és a kockázatot ágens csak emelheti.** | 0004 | I-0004-1, I-0004-2 |
| E6 | **Semmi nem íródik felül; minden változás új verzió**, és a régi verzióra hozott ítélet nem érvényes az újra. | 0006 | I-0006-1, I-0002-2, I-0003-2, I-0007-5 |
| E7 | **Előre ugrani nem lehet.** Elakadás után a munka ugyanott vagy korábban folytatódik. | 0007 | I-0007-4 |
| E8 | **A konfigurációt soha nem élesíti a gyár maga.** Konfiguráció minden, ami a gyár működését meghatározza: kapu-konfiguráció, küszöb, mintavételi arány, korlát, kemény lista, a szabályok kódja, skill, ágens-utasítás, munkafolyamat. A gyár javasolhat változtatást, de érvénybe csak emberi jóváhagyással lép. | 0001, 0004 | I-0002-4 |
| E9 | **Minden visszavezethető, mindkét irányban:** szándék ↔ spec AC ↔ munkadarab AC ↔ diffrész ↔ bizonyíték. Ezért az elfogadó az eredményt nézi a bizonyíték alapján, nem a diffet. | 0002, 0003, 0005 | I-0002-1, I-0003-1, I-0003-4, I-0005-1 |
| E10 | **A gyár inkább megáll, mint hogy csendben gyenge munkát adjon le.** Bármelyik sáv jelezhet elakadást, és sérült megkötés sem mehet át csendben. | 0006, 0007 | I-0007-1, I-0007-2, I-0007-3, I-0007-6 |
| E11 | **A main-be pontosan az kerül, amit ellenőriztek és elfogadtak.** | 0008 | I-0008-1, I-0008-2, I-0008-3 |

### Az autonómia létrája (E4)

Minden kapu, a K0 is, ugyanezt a létrát járja be, kategóriánként:

1. az ember tételenként dönt;
2. szabály dönt, az ember mintát néz;
3. szabály dönt, az ember mintát néz, a gyár javasolja a szabály módosítását, és az ember hagyja
   jóvá.

Kezdetben, és minden új kategóriában, minden kapu az 1. fokon áll. Fel és le a mért átcsúszási
arány viszi (0002). Példa a K0 2. fokára: ember által jóváhagyott szabály szerint minden
átcsúszott hiba javítása automatikusan kiválasztott. A célt így is az ember választja. Ha a gyár
maga választana célt és maga írná a szabályt, az L5 lenne, amit a 0001 kizár.

### Megkötés-nyilvántartás

A megkötések az álláspontokban vannak, a táblázat fenti oszlopa mindegyiket felsorolja (27 élő
megkötés). Az `I-` előtag az „invariáns” szóból maradt, a jelentése megkötés. Visszavont
azonosítók, amelyeket nem osztunk ki újra: I-0004-4, I-0004-5, I-0004-6, I-0005-4.

## A munkánk elvei

Ezek a beszélgetésre és a jegyzetekre vonatkoznak, nem a gyár működésére. Ezért nincs megkötésük.

| # | Elv | Honnan |
|---|---|---|
| M1 | **Mindenki ugyanazt értse alatta.** Minden használt fogalom definícióval szerepel a fogalomtárban. | `CLAUDE.md`, `glossary.md` |
| M2 | **Egyszerűség (KISS).** Ha egy lépés elhagyható vagy összevonható, elhagyjuk vagy összevonjuk. | 0008 |
| M3 | **A működési modell vezérel.** Minden döntést megkötés, ítélet vagy mérőszám formájában fogalmazunk meg. | 0006 |
| M4 | **Egy állítás egy helyen él.** A szabály az álláspontban van, a fogalomtár csak definiál, a többi hely hivatkozik. | konzisztencia-vizsgálat, 2026-10-18 |
