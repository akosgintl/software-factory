# 0006 — Gráfmodell: most leíró, de a működési modell vezérel

Állapot: 📌 elfogadva · 2026-10-18 · módosítva 2026-10-18 (három forma, ítélet bármely
szereplőtől, időbeli gráf; a próba: `topics/megkotesek.md`) · pontosítva 2026-10-18 (mi a
megkötés)

## Kérdés

Hierarchiaként (1:N, 1:1) vagy gráfként írjuk le a gyárat? És mire való a leírás: arra, hogy így
gondolkodjunk róla (leíró modell), vagy arra, hogy a gyár ténylegesen így tartsa nyilván a munkát
(működési modell)?

## Álláspont

1. **A gyárat típusos gráfként írjuk le.**
   - Csomópontok: **munkatermék** (szándék, spec, AC, terv, munkadarab, commit, bizonyíték,
     döntés), **tevékenység** (egy állomás egy futása), **szereplő** (ember, ágens).
   - Típusos élek: például *származik*, *teljesít*, *igazol*, *jóváhagy*, *elfogad*, *függ*,
     *előállította*, *okozta*.
   - Megkötések az éleken. A kardinalitás itt marad meg, mint tervezési döntés (például egy
     munkadarabhoz egy PR tartozik).
2. **A hierarchia nézet, nem modell.** A *származik* élekből nagyjából fa rajzolható, ez jól mutat
   a boardon.
3. **Most leíró modellel dolgozunk (A).** A gráf a jegyzetekben él.
4. **A működési modell (B) a mérce.** Minden döntést úgy fogalmazunk meg, hogy működési szabállyá
   válhasson. Három formája lehet:
   - **megkötés**: a gráfról szóló állítás, amely (1) bármely pillanatban eldönthető kizárólag
     a gráfból, determinisztikus kóddal, ember és ágens ítélete nélkül; (2) mindig igaz kell
     legyen; (3) a szerkezetről szól (ki, mit, miről, mikor, melyik verzión), nem a tartalom
     minőségéről. Például: a diff minden darabjából *teljesít* él vezet egy AC-hez. Ha LLM
     ellenőrizné, az ítélet lenne, nem megkötés;
   - **ítélet**: csomópont, amelyet egy szereplő hoz: ember, ágens vagy szabály. A gráf azt
     rögzíti, hogy ki ítélt, miről, és melyik verzióról. Azt nem, hogy jól ítélt-e. A megkötések
     mondják meg, melyik ítéletet ki hozhatja;
   - **mérőszám**: lekérdezés a gráfon (például átcsúszási arány kapunként és kategóriánként). A
     küszöbe konfiguráció, amely emberi ítélettel változik.
4a. **A megkötés négy fajtája.** Szerkezeti (minden X-hez tartozik Y), őrfeltétel (egy esemény
   csak akkor történhet meg, ha…), jogosultsági (ezt az ítéletet csak ez a szereplő hozhatja),
   sorrendi (ez előbb történt, mint az). A csak bővülő gráfban minden őrfeltétel szerkezeti
   megkötéssé válik, ezért utólag is ellenőrizhető. Ami csak „egyszer megtörténik” (liveness),
   vagy csak időablakra igaz (statisztikai), az nem megkötés: az előbbiből időkorláttal lesz
   megkötés, az utóbbi mérőszám küszöbbel.
4b. **Ha egy megkötés sérül:** ahol lehet, **megelőző** (a lépés nem történik meg), ahol nem,
   **észlelő** (utólag kiderül, és elakadás lesz belőle). Csendben átmenni soha nem lehet.
4c. **A megkötés alakja rögzített, a paramétere konfiguráció.** Például a „legfeljebb N
   újramunka-kör” alakja csak az álláspont módosításával változik, az N-et a gyár javasolhatja,
   és ember élesíti (E8).
5. **Ami egyik formába sem fér bele, az figyelmeztető jel.** Vagy még nem elég pontos, vagy rejtett
   ítélet, amit ki kell mondani, és szereplőt kell rendelni hozzá.
6. **A gráf időbeli, és csak bővülhet.** Semmit nem írunk felül: minden változás új csomópont
   vagy él (új verzió, új ítélet). Az állapot (Backlog, Ready, Done) a gráfból levezetett nézet,
   nem tárolt adat.
7. **Két gráf van:** a munka gráfja és a kód függőségi gráfja. A kockázat hatókör-feltétele (0004)
   a kettőt köti össze.
8. **A W3C PROV (Entity, Activity, Agent) próbakő, nem kötelező szókincs.** Arra használjuk, hogy
   észrevegyük, ha kihagytunk valamit.

## Miért

- A valódi viszonyok nem fák. Az átcsúszott hiba egy PR-ból új szándékot szül, ez kör. A kéretlen változásból
  egy másik munkadarabból származó új munkadarab lesz. A bizonyíték egyszerre kötődik AC-hez és
  commithoz.
- A folyamat az élekben él: a kapcsolat jelentése fontosabb, mint a darabszám.
- Az álláspontok megkötésként ellenőrizhetők lesznek, nem csak prózában leírt szabályok.
- A B mint mérce nem hagyja, hogy a beszélgetés olyan elvekre jusson, amelyeket a gyár nem tud
  betartatni.

## Mi szólt ellene

- A sima gráf túl szabad: ha bármi bármivel összeköthető, semmit nem döntöttünk el. Ezért típusos
  gráf, zárt csomópont- és éltípus-listával.
- Korai formalizálás: lassíthatja a gondolkodást. Ezért A-val kezdünk, és B csak a mérce.
- A tartalom minősége (jól érti-e a spec a szándékot) nem gráfszabály. Erre az ítélet-csomópont a
  válasz: a gráf az ítélet tényét és felelősét rögzíti, a tartalmát nem.
- Az ágens saját állítása (például „preview környezetben készült”, „reverttel visszavonható”) csak
  annyit ér, amennyit az állító. A megkötés csak azt garantálja, ki állította. Ez a modell
  határa; nyitott kérdés, hogyan tehető ellenőrizhetővé.

## Mi változtatná meg

- Ha a fontos szabályaink többsége nem fogalmazható meg megkötésként vagy döntés-csomópontként,
  akkor a gráfmodell rossz absztrakció.
- Ha a működési gráf fenntartása többe kerül, mint amennyi hibát a szabályai megfognak.
