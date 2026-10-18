# 0006 — Gráfmodell: most leíró, de a működési modell vezérel

Állapot: 📌 elfogadva · 2026-10-18 · módosítva 2026-10-18 (három forma, ítélet bármely
szereplőtől, időbeli gráf; a próba: `topics/invariansok.md`)

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
   - **invariáns**: a gráfon gépi úton ellenőrizhető szabály (például: a diff minden darabjából
     *teljesít* él vezet egy AC-hez);
   - **ítélet**: csomópont, amelyet egy szereplő hoz: ember, ágens vagy szabály. A gráf azt
     rögzíti, hogy ki ítélt, miről, és melyik verzióról. Azt nem, hogy jól ítélt-e. Az invariánsok
     mondják meg, melyik ítéletet ki hozhatja;
   - **mérőszám**: lekérdezés a gráfon (például átcsúszási arány kapunként és kategóriánként). A
     küszöbe konfiguráció, amely emberi ítélettel változik.
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
- Az álláspontok invariánsként ellenőrizhetők lesznek, nem csak prózában leírt szabályok.
- A B mint mérce nem hagyja, hogy a beszélgetés olyan elvekre jusson, amelyeket a gyár nem tud
  betartatni.

## Mi szólt ellene

- A sima gráf túl szabad: ha bármi bármivel összeköthető, semmit nem döntöttünk el. Ezért típusos
  gráf, zárt csomópont- és éltípus-listával.
- Korai formalizálás: lassíthatja a gondolkodást. Ezért A-val kezdünk, és B csak a mérce.
- A tartalom minősége (jól érti-e a spec a szándékot) nem gráfszabály. Erre az ítélet-csomópont a
  válasz: a gráf az ítélet tényét és felelősét rögzíti, a tartalmát nem.
- Az ágens saját állítása (például „preview környezetben készült”, „reverttel visszavonható”) csak
  annyit ér, amennyit az állító. Az invariáns csak azt garantálja, ki állította. Ez a modell
  határa; nyitott kérdés, hogyan tehető ellenőrizhetővé.

## Mi változtatná meg

- Ha a fontos szabályaink többsége nem fogalmazható meg invariánsként vagy döntés-csomópontként,
  akkor a gráfmodell rossz absztrakció.
- Ha a működési gráf fenntartása többe kerül, mint amennyi hibát a szabályai megfognak.
