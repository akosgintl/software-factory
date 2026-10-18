# 0001 — Mit értünk szoftvergyár alatt

Állapot: 📌 elfogadva · 2026-10-16 · kiegészítve 2026-10-18 (az autonómia iránya)

## Kérdés

A „szoftvergyár” szónak több jelentése van (folyamat, platform, autonóm termelés). Melyiket
használjuk, és mi a határa?

## Álláspont

A szoftvergyár olyan rendszer, amely **emberi szándékból (intent) PR-t állít elő**. Az autonóm
termelés (C) jelentést használjuk, emberi végső kapuval.

1. **A kimenet a változtatás, nem a termék.** Az ismétlődő egység: intent → PR.
2. **Hogy mit építünk, arról az ember dönt.** A gyár nem választ célt.
3. **Az ember validál.** Korai fázisban sok ponton, a bizalom növekedésével kevesebb ponton, de a
   végén mindig.
4. **Építőelemek:** skillek, ágensek, munkafolyamatok (workflow).
5. **Tanuló hurok.** A gyár folyamatosan elemzi az eredményeit és a hatékonyságát, és változtatást
   javasol a saját működésére. A javaslatról az ember dönt.

Egy mondatban: **a gyár javasol és végrehajt, az ember dönt és validál.**

6. **Az autonómia úgy nő, hogy az ember tételek helyett szabályokról dönt.** A szabályt mindig
   ember hagyja jóvá, a gyár csak javasolhat. Így a K0 is lehet „nem kötelező tételenként”, ha
   ember által írt szabály választ; a célválasztás embernél marad (`elvek.md`, E4).

## Miért

- A „gyártás” szó szoros értelmében (másolás, build, deploy) régóta automatikus. Ami ismétlődik és
  iparosítható, az a változtatás.
- Az ágens cserélhető munkavégző, ezért gyárat most lehet igazán építeni. Az előző két hullámban
  (Cusumano, Greenfield–Short) a munkavégző ember volt, és ő nem szabványosítható.
- A felelősség az embernél marad: ő választja a célt, és ő fogadja el az eredményt.
- Tanuló hurok nélkül a rendszer csak automatizálás. Gyárrá az teszi, hogy javítja a saját
  folyamatát.

## Mi szólt ellene

- A „dark factory” irány szerint a végső emberi review is elhagyható. Mi ezt elvetjük, legalábbis
  most.
- A végső emberi validálás nagy átbocsátásnál szűk keresztmetszet lesz. Nyitott kérdés, hogy mit
  validál az ember: a diffet, vagy az eredményt a szándékhoz képest.
- A felfedező munkára (amikor még nem tudjuk, mit kell építeni) a gyár kevésbé alkalmas. Ezért a
  gyár egy szoftverszervezet része, nem az egész.

## Mi változtatná meg

- Ha a mért adatok szerint egy változtatás-kategóriában a végső emberi validálás hosszú ideig nem
  talál hibát, és közben szűk keresztmetszet, akkor abban a kategóriában újra kell gondolni a 3.
  pontot.
- Ha a gyár jobban választ célt, mint az ember (például telemetria alapján), az a 2. pontot
  gyengítené. Ma ezt nem tartjuk valószínűnek.
