# Irányelvek

📌 2026-10-18. Rövid, emberi mondatok, amelyekből az álláspontok és a megkötések következnek.
Minden gyár-irányelv mellett ott áll, mely megkötések valósítják meg. Ha egy irányelvnek nincs
megkötése, az rés (visszavezethetőség az elvek szintjén).

## A gyár irányelvei

| # | Irányelv | Honnan | Megkötések |
|---|---|---|---|
| E1 | **A gyár javasol és végrehajt, az ember dönt és validál.** | 0001 | I-0002-5 |
| E2 | **Az ember mindig validált elemet kap átnézésre.** Egy kapu kikapcsolása nem kapcsolja ki a független ellenőrzést: minden kapu előtt eval és review jön. Az ember e fölé kerül, nem helyette van. | 0008 | I-0008-4 |
| E3 | **Senki nem minősíti a saját munkáját.** | 0003, 0004, 0005 | I-0003-3, I-0004-3, I-0005-2 |
| E4 | **Az autonómia úgy nő, hogy az ember tételek helyett szabályokról dönt.** A szabályt mindig ember hagyja jóvá, a gyár csak javasolhat. | 0001 | I-0002-4, I-0004-4 |
| E5 | **A kockázat csak felfelé módosítható ágens által.** | 0004 | I-0004-2 |
| E6 | **Semmi nem íródik felül; minden változás új verzió.** | 0006 | I-0002-2, I-0003-2, I-0007-5 |
| E7 | **Előre ugrani nem lehet.** Elakadás után a munka ugyanott vagy korábban folytatódik. | 0007 | I-0007-4 |
| E8 | **A szabályt soha nem élesíti a gyár maga.** Szabály minden, ami a gyár működését meghatározza: kapu-kapcsolás, küszöb, mintavételi arány, kemény lista, újramunka-korlát, skill, ágens-utasítás, munkafolyamat. A gyár javasolhat változtatást, de érvénybe csak emberi jóváhagyással lép. | 0001, 0004 | I-0002-4, I-0004-4, I-0004-6 |

### Az autonómia létrája (E4)

Minden kapu ugyanazt a létrát járhatja be, kategóriánként:

1. az ember tételenként dönt;
2. szabály dönt, az ember mintát néz;
3. szabály dönt, a gyár javasolja a szabály módosítását, és az ember hagyja jóvá.

A szabályt soha nem élesíti a gyár maga (E8). Ez a K0-ra is igaz: a K0 lehet „nem kötelező
tételenként”, ha ember által írt szabály választ (például: minden átcsúszott hiba javítása
automatikusan kiválasztott). A célválasztás így embernél marad. Ha a gyár maga választana célt és
maga írná a szabályt, az L5 lenne, amit a 0001 kizár.

## A munkánk elvei

Ezek a beszélgetésre és a jegyzetekre vonatkoznak, nem a gyár működésére. Ezért nincs megkötésük.

| # | Elv | Honnan |
|---|---|---|
| M1 | **Mindenki ugyanazt értse alatta.** Minden használt fogalom definícióval szerepel a fogalomtárban. | `CLAUDE.md`, `glossary.md` |
| M2 | **Egyszerűség (KISS).** Ha egy lépés elhagyható vagy összevonható, elhagyjuk vagy összevonjuk. | 0008 |
| M3 | **A működési modell vezérel.** Minden döntést megkötés, ítélet vagy mérőszám formájában fogalmazunk meg. | 0006 |
