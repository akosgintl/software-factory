# 0002 — Emberi kapuk és bizalom

Állapot: 📌 elfogadva · 2026-10-16 · módosítva 2026-10-18 (K0; minden kapun ember vagy szabály dönt,
mintavétellel)

## Kérdés

Hol lép be az ember a szándék → PR folyamatba, mit validál, és hogyan csökkenhet a beavatkozás?

## Álláspont

```
szándék ─[K0: kiválasztás]─▶ spec ─[K1: jóváhagyás]─▶ terv ─[K2: jóváhagyás]─▶ build, ellenőrzés ─▶ PR ─[K3: elfogadás]─▶ landing
```

A teljes folyamat a 0008-ban van.

0. **K0: melyik szándékon dolgozzon a gyár, és milyen sorrendben.** Ez prioritás, nem ellenőrzés.
   A gyár által javasolt szándékra is kell (0005). Kötegelhető: nem szándékonként, hanem a backlog
   rendszeres átnézésekor.
1. **K1: a szándékból az ágens specet ír**, és jóváhagyják: jól értette-e a szándékot.
2. **K2: a specből az ágens tervet ír**, és jóváhagyják: a megközelítést és a felbontást
   munkadarabokra.
3. **K3: a végén az eredményt fogadják el a szándékhoz képest**, a bizonyíték alapján (0003). A
   diffet csak kockázat szerint nézik meg.
4. **Minden kapun mindig van ítélet. Hogy ki hozza, azt a kapu-konfiguráció mondja meg,
   kapunként és kategóriánként:**
   - **ember dönt** tételenként, vagy
   - **szabály dönt**, és az ember mintát néz.

   Kezdetben, és minden új kategóriában, minden kapun ember dönt. A kapu a mért bizalom alapján
   kerül szabályra, és ugyanígy kerül vissza emberhez (autonómia létrája, `elvek.md`). Kikapcsolt
   kapu nincs. A K3 szabályát a 0004 adja.
5. **Mintavétel:** a szabály által hozott kapu-ítéletek egy részét utólag ember nézi meg, mind a
   négy kapun (K0–K3), minden kategóriában. Az arány kapunként konfiguráció, alapból 10%. Ebből
   jön a szabály-ítéletek átcsúszási aránya.

## Megkötések

- **I-0002-1** Minden munkadarabtól a *származik* élek egy olyan tervhez és spechez vezetnek,
  amelynek az aktuális verziójára K2, illetve K1 jóváhagyó ítélet *vonatkozik*.
- **I-0002-2** Minden ítélet egy munkatermék egy verziójára *vonatkozik*. Ha a munkaterméknek *új
  verziója* van, a régi ítélet nem érvényes rá.
- **I-0002-3** Minden merge-ölt PR head commitjára *vonatkozik* egy K3 elfogadás.
- **I-0002-4** A konfiguráció minden új verziójára ember jóváhagyó ítélete *vonatkozik*, mielőtt
  érvénybe lép (E8).
- **I-0002-5** Spec csak olyan szándékra készülhet, amelyre K0 kiválasztó ítélet *vonatkozik*.
- **I-0002-6** Kapu-ítéletet szabály csak akkor hozhat, ha az érvényes kapu-konfiguráció az adott
  kapun és kategóriában szabályt ír elő, és csak az ott megnevezett szabály. Minden más esetben
  ember hozza.

Mérőszámok:

- **átcsúszási arány** kapunként és kategóriánként: a bizalom mérőszáma. Ennek alapján kerül egy
  kapu szabályra, vagy vissza emberhez.
- **mintavételi arány** kapunként: a szabály által hozott ítéletek közül hánynak van utólagos
  emberi mintavételi ítélete, időablakra. Ha a konfigurált arány alá esik, a gyár riaszt.

## Miért

- A diff átnézése nem skálázódik. Az eredmény elfogadása igen.
- A hibát a legolcsóbb korán elkapni: a félreértett szándékot K1-nél, a rossz megközelítést
  K2-nél.
- A bizalom kategóriánként más (változtatás-típus, kódterület), ezért a kapukat is kategóriánként
  állítjuk.
- Ha egy kaput egyszerűen ki lehetne kapcsolni, a rajta átcsúszott hibát semmi nem mérné. A
  szabály-ítélet és a mintavétel ezt méri. Mintavétel nélkül a bizalom vakon nőne.

## Mi szólt ellene

- Négy kapu sok várakozás. Ha mindegyiken ember dönt, az ember lesz a szűk keresztmetszet. Erre
  válasz a 4. pont.
- A K2 ugyanazt a „hogyan” kérdést validálja, mint a diff review. 💭 Valószínűleg a K2 kerülhet
  elsőként szabályra. A terv a felbontás egyetlen helye, de a felbontást a K2 előtti gap elemzés
  (0008) akkor is ellenőrzi, ha a K2-n szabály dönt.
- 💭 Ha az építés olcsó, néha olcsóbb megépíteni és megmutatni, mint a specet átnézni (például
  UI-nál).

## Mi változtatná meg

- Ha egy kapun a szabály-ítéletek átcsúszási aránya a küszöb fölé nő, a kapu abban a kategóriában
  visszakerül emberhez.
- Ha a mintavétel emberi ideje megközelíti a tételenkénti döntését, abban a kategóriában a szabály
  nem éri meg.
