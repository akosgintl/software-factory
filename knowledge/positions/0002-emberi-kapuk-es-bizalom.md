# 0002 — Emberi kapuk és bizalom

Állapot: 📌 elfogadva · 2026-10-16 · módosítva 2026-10-18 (K0: a szándék kiválasztása)

## Kérdés

Hol lép be az ember az intent → PR folyamatba, mit validál, és hogyan csökkenhet a beavatkozás?

## Álláspont

A folyamat:

```
szándék ──[K0: kiválasztás]──▶ ágens ──▶ spec ──[K1: spec]──▶ ágens ──▶ terv ──[K2: terv]──▶ ágensek (build, QA, review) ──▶ PR ──[K3: elfogadás]
```

0. **Az ember kiválasztja, melyik szándékon dolgozzon a gyár, és milyen sorrendben (K0).** Ez
   prioritás, nem ellenőrzés. A gyár által javasolt szándékra is kell. A K0 soha nem kapcsolható
   ki, mert a 0001 2. pontja (a célt az ember választja) ezen áll. Kötegelhető: nem
   szándékonként, hanem a backlog rendszeres átnézésekor.
1. **A szándékból az ágens ír specifikációt.** Az ember jóváhagyja (K1): jól értette-e a
   szándékot.
2. **A specifikációból az ágens ír tervet.** Az ember jóváhagyja (K2).
3. **A végén az ember az eredményt validálja a szándékhoz képest** (K3): bizonyíték, teljesült AC.
   A diffet csak kockázat szerint nézi meg.
4. **A bizalmat mérjük, javítjuk, és a kapukat ennek alapján ki- és bekapcsoljuk.** A korai fázisban
   minden kapu él. A K0 és a K3 mindig él.

## Miért

- A diff átnézése nem skálázódik. Az eredmény elfogadása igen.
- A hibát a legolcsóbb korán elkapni: a félreértett szándékot K1-nél, a rossz megközelítést K2-nél.
- A bizalom kategóriánként más (változtatás-típus, kockázat, kódterület), ezért a kapukat is
  kategóriánként kell kapcsolni.

## Mi szólt ellene

- Három emberi kapu sok várakozás. Ha mindhárom mindig él, az ember lesz a szűk keresztmetszet.
- K2 ugyanazt a „hogyan” kérdést validálja, mint a diff review. Ezt az ember a végén már nem
  akarja nézni. 💭 Valószínűleg K2 kapcsolható ki elsőként.
- 💭 Ha az építés olcsó, néha olcsóbb megépíteni és megmutatni, mint a specifikációt átnézni
  (például UI-nál).

## Mi változtatná meg

- Ha a mérés szerint egy kapu hosszú ideig semmit nem fog meg, és az átcsúszott hibák sem
  szaporodnak, akkor az a kapu abban a kategóriában kikapcsolható. Ha az átcsúszási arány nő, visszakapcsoljuk.
