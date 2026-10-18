# Fogalmi modell

📌 Elfogadva 2026-10-18. A fogalomtár (`glossary.md`) ábécérendben sorolja a szavakat, ez a jegyzet
a viszonyukat mutatja: mi micsoda, hány az egyhez, ki mit csinál vele. A teljes típuslista a
`positions/0006-grafmodell.md` fájlban van; az alábbi lánc a *származik* élek nézete, nem maga a
modell.

## 1. Munkatermékek: ami végigmegy a soron

```
szándék ─1:1─ spec ─1:1─ terv ─1:N─ munkadarab ─1:1─ PR ─1:N─ bizonyíték
```

| Fogalom | Ki hozza létre | Mi van benne |
|---|---|---|
| szándék | ember, vagy a gyár javasolja (szándék-javaslat, 0005) | mit akar elérni és miért |
| spec | Planner; K1 jóváhagyás | probléma, felhasználói szintű AC, kockázat, és mi *nincs* benne |
| terv | Planner; K2 jóváhagyás | megközelítés, felbontás munkadarabokra, függőségek |
| munkadarab | a terv terméke | a gyártás egysége: saját, technikai AC, egy branch, egy PR |
| PR | Builder | a változtatás |
| bizonyíték | QA, függetlenül a Buildertől | AC-nként, a commithoz kötve (0003) |

- 📌 **A felbontás egyetlen helye a terv.** Munkadarab csak a tervből jön. A gyár minden más
  javaslata szándék-javaslat, és K0-n megy át (0005). A felbontást a K2 előtti gap elemzés akkor
  is ellenőrzi, ha a K2-n szabály dönt (0008).
- 📌 A „kártya” neve **munkadarab**: ami állomásról állomásra halad. A board kártyája csak a
  megjelenése.
- 💭 A szándék : spec arány egyelőre 1:1. Hogy nagy szándéknál 1:N kell-e, az nyitott kérdés
  (`questions.md`).

## 2. Szereplők: aki dolgozik vagy ítél

- **ember**: szándékot ad, kapunál dönt vagy szabályt hagy jóvá, mintát néz, elakadást old fel.
- **ágens**: munkavégző. Modell, eszközök és utasítás egy szerephez.
- **szabály**: determinisztikus kiértékelő kód, amely ítéletet hoz (például a K3 alacsony
  kockázatnál, 0004).

A skill és a munkafolyamat nem szereplő, hanem konfiguráció: a skillt az ágens tölti be, a
munkafolyamat a vezérlés leírása (az állomások és a kapuk sorrendje).

## 3. Állomás és sáv

- **állomás**: egy lépés a soron. Négy van: tervezés, build, ellenőrzés, landing (0008). *Mit*
  csinálunk. Az állomások sorrendjét a munkafolyamat adja.
- **sáv (lane)**: szerepkör. *Ki* csinálja. Egy sávban több állomás lehet, és egy állomáson több sáv
  is dolgozhat (tervezés: Planner és Reviewer; ellenőrzés: QA és Reviewer).
- A sáv nem csak vizualizáció. A függetlenségi szabályok sávok között élnek (E3).
- Az ember is sáv: az ő pontjai a kapuk, a mintavétel és az elakadás feloldása.

## 4. Döntési pontok: ahol a munka megáll

- **kapu**: döntési pont. Mindig van rajta ítélet; a kapu-konfiguráció szerint ember vagy szabály
  hozza (0002).
- **kiválasztás**: döntés arról, melyik szándékon dolgozzon a gyár, és milyen sorrendben (K0).
- **jóváhagyás**: döntés, *mielőtt* a munka elindul. K1 (spec), K2 (terv).
- **elfogadás**: döntés az *eredményről*, a landing előtt. K3.
- **kategória** és **kockázat**: a kategória szerint állítjuk a kapukat (0002). A K3-on a szabály
  csak alacsony kockázatnál fogad el, különben ember dönt (0004).
