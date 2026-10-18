# 0001 — Mit értünk szoftvergyár alatt

Állapot: 📌 elfogadva · 2026-10-16 · kiegészítve 2026-10-18 (az autonómia iránya; a gyár AI-natív)

## Kérdés

A „szoftvergyár” szónak több jelentése van (folyamat, platform, autonóm termelés). Melyiket
használjuk, mi a határa, és AI-natív vagy AI-támogatott legyen?

## Álláspont

A szoftvergyár olyan rendszer, amely **emberi szándékból (intent) PR-t állít elő**. Az autonóm
termelés jelentést használjuk, emberi döntéssel és validálással.

1. **A kimenet a változtatás, nem a termék.** Az ismétlődő egység: szándék → PR.
2. **Hogy mit építünk, arról az ember dönt.** A gyár nem választ célt, csak javasolhat.
3. **Az ember validál.** Minden kapun van ítélet, és a végén mindig van elfogadás (K3, 0002).
   Kezdetben az ember tételenként dönt. A bizalom növekedésével egyre több tételt az általa
   jóváhagyott szabály dönt el, és az ember mintát néz.
4. **Építőelemek:** ágensek, skillek, munkafolyamatok (workflow) és szabályok.
5. **Tanuló hurok.** A gyár folyamatosan elemzi az eredményeit és a hatékonyságát, és változtatást
   javasol a saját működésére. A javaslatról az ember dönt (E8).
6. **Az autonómia úgy nő, hogy az ember tételek helyett szabályokról dönt** (E4). A célválasztás
   is átadható szabálynak, ha a szabályt ember hagyta jóvá. A célt így is az ember választja.
7. **A gyár AI-natív.** A folyamatot az ágensekre tervezzük, nem egy meglévő, emberközpontú
   folyamatot gyorsítunk AI-val. Az ember a hurok fölött áll (human on the loop): kapunál,
   mintavételnél és elakadásnál lép be, nem minden lépésnél.

Egy mondatban: **a gyár javasol és végrehajt, az ember dönt és validál.**

### AI-natív, nem AI-támogatott

| Szempont | AI-támogatott (elvetjük) | AI-natív (ezt építjük) |
|---|---|---|
| Fő munkavégző | ember, AI-eszközzel | ágens |
| Az ember helye | a hurokban (in the loop), minden lépésnél | a hurok fölött (on the loop): kapu, mintavétel, elakadás |
| A munka egysége | fejlesztői feladat | munkadarab, AC-vel és bizonyítékkal |
| A folyamat | a meglévő (Scrum, emberi code review), AI-val gyorsítva | az ágensekre tervezve: sávok, kapuk, bizonyíték |
| Szűk keresztmetszet | emberi figyelem és gépelés | a spec minősége és az ellenőrzési kapacitás |
| Mit mérünk | fejlesztői produktivitás | átfutás munkadarabonként, újramunka, emberi idő PR-onként |
| A dokumentáció olvasója | ember | elsősorban ágens (AGENTS.md, skillek, ellenőrizhető AC) |

### Autonómia-szintek

| Szint | Név | Az ember szerepe |
|---|---|---|
| L0 | kézi | mindent ő csinál |
| L1 | kiegészítés | gépel, az AI sort vagy blokkot javasol (autocomplete) |
| L2 | pár | beszélget, az AI fájlokat ír, az ember minden lépést lát |
| L3 | feladat-ágens | feladatot ad, minden PR-t átnéz |
| L4 | kapuzott folyamat | szándékot ad, kapunál dönt vagy szabályt hagy jóvá, mintát néz, elakadásnál lép be |
| L5 | önirányító | a célt és a szabályokat is a gyár adja magának |

Az AI-támogatott sáv L1–L3, az AI-natív L4-nél kezdődik. A határon fordul meg, hogy az ember a
munka része vagy a rendszer tervezője. **A mi gyárunk L4, tanuló hurokkal.** Az L5-öt a 2. pont és
az E8 kizárja. A skála rokona Dan Shapiro „five levels” skálája (`sources.md`).

## Megkötések

A 0001-nek nincs saját megkötése. Az irányelvei (E1, E4, E8, `elvek.md`) a 0002-es megkötéseken
keresztül valósulnak meg.

## Miért

- A szoftvergyár régi ötlet: a fejlesztést ismételhető, mérhető, iparszerű folyamattá szervezni.
  Két korábbi hullám volt: a japán szoftvergyárak az 1970–80-as években (Hitachi, Toshiba, NEC,
  Fujitsu; Cusumano), és a Microsoft Software Factories 2004 körül (modellvezérelt fejlesztés,
  domain-specifikus nyelvek; Greenfield–Short). Mindkettő ugyanott akadt el: a folyamatot lehetett
  szabványosítani, a munkát végző embert nem. Az ágens szabványosítható, másolható és
  párhuzamosítható munkavégző, ezért gyárat most lehet igazán építeni.
- A „gyártás” szoros értelmében (másolás, build, deploy) régóta automatikus; Reeves szerint a kód
  maga a terv, a fordító a gyár. Ami ismétlődik és iparosítható, az a változtatás.
- A felelősség az embernél marad: ő választja a célt (közvetlenül vagy szabállyal), és ő fogadja el
  az eredményt (közvetlenül, vagy szabállyal és mintavétellel).
- Tanuló hurok nélkül a rendszer csak automatizálás. Gyárrá az teszi, hogy javítja a saját
  folyamatát.
- AI-natív, mert az AI-támogatott folyamatban az ember marad a szűk keresztmetszet. Ha az ágens
  gyorsan ír kódot, a lassú rész a spec, az ellenőrzés és a döntés. Ezt csak az ágensekre tervezett
  folyamat tudja kezelni. Rokon gondolat: „Humans steer. Agents execute.” (OpenAI, Harness
  engineering).

## Mi szólt ellene

- A „dark factory” irány (például StrongDM) szerint az emberi döntés és validálás is elhagyható.
  Mi ezt elvetjük, legalábbis most.
- A végső emberi validálás nagy átbocsátásnál szűk keresztmetszet. Válasz: az ember az eredményt
  nézi, nem a diffet (0002, 0003), és alacsony kockázatnál szabály fogad el, mintavétellel (0004).
- A felfedező munkára (amikor még nem tudjuk, mit kell építeni) a gyár kevésbé alkalmas. Ezért a
  gyár egy szoftverszervezet része, nem az egész.

## Mi változtatná meg

- Ha a gyár jobban választ célt, mint az ember (például telemetria alapján), az a 2. pontot
  gyengítené. Ma ezt nem tartjuk valószínűnek.
- Ha egy munkafajtánál az ágensekre tervezett folyamat tartósan lassabb vagy rosszabb, mint az
  ember AI-eszközzel, ott a 7. pont nem igaz, és az a munka a gyáron kívül marad.
